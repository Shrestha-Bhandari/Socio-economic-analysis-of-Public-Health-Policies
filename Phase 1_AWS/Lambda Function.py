import boto3
import urllib.request
import json
import os

# AWS S3 Configuration
S3_BUCKET_NAME = "worldbank-datasets-bucket"  # Change this if needed
JSON_FILE_PATH = "data link/datasets.json"  # Updated path to JSON in S3
TMP_DIR = "/tmp/"  # AWS Lambda's temporary storage

# Initialize AWS S3 client
s3_client = boto3.client("s3")

def read_dataset_urls():
    """Read dataset URLs from the JSON file stored in S3."""
    try:
        obj = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=JSON_FILE_PATH)
        data = json.loads(obj["Body"].read().decode("utf-8"))
        return data.get("datasets", [])  # Return the list of dataset URLs
    except Exception as e:
        print(f"Error reading JSON file from S3: {str(e)}")
        return []

def download_file(url):
    """Download file from the given URL."""
    try:
        filename = url.split("/")[-1].split("?")[0] + ".csv"
        file_path = os.path.join(TMP_DIR, filename)

        # Use urllib instead of requests
        urllib.request.urlretrieve(url, file_path)
        print(f"Downloaded {filename} successfully.")

        return file_path, filename
    except Exception as e:
        print(f"Error downloading file {url}: {str(e)}")
        return None, None

def upload_to_s3(file_path, filename):
    """Upload the downloaded file to S3."""
    try:
        s3_key = f"raw_data/{filename}"  # Store under 'raw_data/' folder in S3
        s3_client.upload_file(file_path, S3_BUCKET_NAME, s3_key)
        print(f"Uploaded {filename} to S3: {s3_key}")
    except Exception as e:
        print(f"Error uploading {filename} to S3: {str(e)}")

def lambda_handler(event, context):
    """AWS Lambda entry point."""
    try:
        dataset_urls = read_dataset_urls()

        for url in dataset_urls:
            file_path, filename = download_file(url)
            if file_path and filename:
                upload_to_s3(file_path, filename)

        return {"statusCode": 200, "message": "Data ingestion completed successfully!"}
    
    except Exception as e:
        print(f"Lambda Error: {str(e)}")
        return {"statusCode": 500, "message": "Error processing request."}
