# -*- coding: utf-8 -*-
"""Main Contextual Knowledge.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b_LHGoYP1op-2_rVqKxV_ep38akh9drI
"""

!pip install spacy
!python -m spacy download en_core_web_lg

from typing import Dict, List, Any, Union
import json
import requests
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import spacy
from datetime import datetime

import requests
import spacy
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import json
from datetime import datetime
from typing import List, Dict, Any

class DocumentProcessor:
    def __init__(self):
        # Initialize models and pipelines
        self.nlp = spacy.load("en_core_web_lg")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def process_json_from_github(self, github_url: str) -> List[Dict[str, Any]]:
        """Fetch JSON from GitHub and process the documents inside it"""
        json_data = self._fetch_json_from_github(github_url)
        processed_documents = []

        for doc in json_data:
            content = doc.get("text", "")  # Assuming the JSON structure has "text" field
            processed = self._process_content(content)
            processed['source_file'] = github_url  # Store source for reference
            processed_documents.append(processed)

        return processed_documents

    def _fetch_json_from_github(self, url: str) -> List[Dict[str, Any]]:
        """Fetch JSON file from a GitHub raw URL"""
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Failed to fetch JSON from GitHub: {response.status_code}")

    def _process_content(self, content: str) -> Dict[str, Any]:
        """Process document content"""
        doc = self.nlp(content)

        # Generate embeddings for the whole document
        embeddings = self.embedder.encode(content)

        # Extract key information
        processed = {
            'summary': self._generate_summary(content),
            'key_topics': self._extract_topics(content),
            'embeddings': embeddings.tolist(),
            'entities': self._extract_entities(doc),
            'key_points': self._extract_key_points(doc),
            'metadata': {
                'length': len(content),
                'processing_timestamp': datetime.now().isoformat()
            }
        }

        return processed

    def _generate_summary(self, text: str) -> str:
        """Generate document summary"""
        chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]
        summaries = [self.summarizer(chunk, max_length=min(150, len(chunk) - 1), min_length=5, do_sample=False)[0]['summary_text'] for chunk in chunks]
        return ' '.join(summaries)

    def _extract_topics(self, text: str) -> List[Dict[str, float]]:
        """Extract topics using zero-shot classification"""
        candidate_labels = [
            "methodology", "results", "discussion", "background",
            "conclusion", "analysis", "recommendations"
        ]

        if not text.strip():
            text = "This is an article with no content"  # Add default content to prevent errors

        try:
            result = self.classifier(text, candidate_labels)
        except Exception as e:
            print(f"Error classifying text: {e}")
            result = {"labels": ["unknown"], "scores": [1.0]}  # Default result in case of error

        return [{'topic': label, 'confidence': score} for label, score in zip(result['labels'], result['scores'])]

    def _extract_entities(self, doc) -> List[Dict[str, str]]:
        """Extract named entities"""
        return [{'text': ent.text, 'label': ent.label_, 'start': ent.start_char, 'end': ent.end_char} for ent in doc.ents]

    def _extract_key_points(self, doc) -> List[str]:
        """Extract key points from document"""
        return [sent.text for sent in doc.sents if self._is_important_sentence(sent)]

    def _is_important_sentence(self, sent) -> bool:
        """Determine if a sentence contains important information"""
        important_indicators = [
            "significant", "important", "key", "main",
            "conclude", "found", "results", "therefore"
        ]
        return any(indicator in sent.text.lower() for indicator in important_indicators)

    def save_to_json(self, processed_documents: List[Dict[str, Any]], output_path: str):
        """Save processed documents to JSON"""
        with open(output_path, 'w') as f:
            json.dump(processed_documents, f, indent=2)


# Example usage
def process_documents_from_github(github_json_url: str) -> List[Dict[str, Any]]:
    """Process documents from GitHub"""

    processor = DocumentProcessor()  # Create an instance of DocumentProcessor
    processed_docs = processor.process_json_from_github(github_json_url)

    return processed_docs

# Example Usage:
github_json_url = "https://raw.githubusercontent.com/Shrestha-Bhandari/scrap_data/refs/heads/main/scraped_data.json"  # Replace with actual URL
processed_docs = process_documents_from_github(github_json_url)
print(processed_docs)

from google.colab import files
import json

def save_to_json_and_download(processed_documents: List[Dict[str, Any]], output_path: str):
    """Save processed documents to JSON and download the file"""
    # Save the processed documents to a local .json file
    with open(output_path, 'w') as f:
        json.dump(processed_documents, f, indent=2)

    # Now download the file
    files.download(output_path)  # This triggers the download in Google Colab

#processed_documents = [...]  # Your processed documents
save_to_json_and_download(processed_docs ,'processed_docs.json')