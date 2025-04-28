# Socio-economic Analysis of Public Health Policies

## About  
**Term:** Spring 2025  
**Team:** Team 7-Orange  
- **Yash Nayi**  
- **Parin Patel**  
- **Shrestha Bhandari**

## Keywords  
MLOps · Python · LLM · NLP · Data Science · Policy Analysis

---
## 💻 Project Abstract:  
<P>Public health policies play a crucial role in shaping healthcare access and outcomes, yet their socioeconomic impact is often unclear. This project leverages data science and NLP techniques to analyze how public health policies affect different socioeconomic groups. By integrating structured datasets , we aim to build an AI-driven system that evaluates policy effectiveness. A fine-tuned language model  will summarize policies, detect misinformation, and correlate policy implementation with socioeconomic indicators.


### 🫧 Background

This project investigates whether public health policies reduce or reinforce socioeconomic disparities by analyzing their intended impact, real-world effects, and public perceptions. Policies such as Medicaid expansion, vaccination programs, and mental health funding aim to improve healthcare access and outcomes, but their socioeconomic impact remains uncertain. To address this, we will analyze policy documents using NLP-based summarization to understand their objectives, leverage structured datasets (income, healthcare access, employment rates) to measure actual effects, and assess public sentiment through social media and news analysis to detect perceptions and misinformation. Finally, we will develop an AI model to correlate policies with socioeconomic indicators, generating data-driven reports and recommendations.

## High Level Requirement
<P>To effectively measure the socioeconomic impact of public health policies, the project requires a robust system integrating data acquisition, processing, and AI modeling. First, structured and unstructured data sources must be gathered, including health statistics, economic indicators, policy documents, and public sentiment data. Data processing will involve cleaning, feature engineering, and pipeline automation to ensure scalability. An LLM/SLM will be fine-tuned for policy summarization, misinformation detection, and sentiment analysis, while predictive models will assess policy effectiveness by correlating socioeconomic indicators. The system will be designed for scalability and integration, ensuring efficient handling of large datasets and adaptability for further expansion. </P>


### 📋 Functional Requirements

<P>We are currently focusing on the World Bank as our primary data source, the system must be designed to efficiently extract, preprocess, and analyze datasets available through the World Bank Open Data portal. This includes key socioeconomic indicators such as income distribution, healthcare access, employment rates, education levels, and poverty metrics. The system should support API-based data retrieval, automated updates to ensure real-time insights, and structured storage for seamless integration with our analytical models. Given the structured nature of World Bank data, preprocessing will involve handling missing values, standardizing formats, and ensuring compatibility with NLP and machine learning pipelines for summarization, comparative analysis, and predictive modeling of policy impacts. </P>


## 📈 High-Level Requirements  
1. **Data Acquisition**  
   - World Bank Open Data (income distribution, health access, employment, education) via API  
   - Policy document collection (federal/state health policy PDFs & text)  
   - Social media & news streams for public sentiment  
2. **Data Processing & Pipelines**  
   - Automated ETL: ingestion → cleaning → feature engineering  
   - Scalable storage (relational or NoSQL) for structured & unstructured data  
3. **Modeling & Analysis**  
   - Fine-tune LLM (e.g. GPT/FLAN) for policy summarization & misinformation detection  
   - Train classifiers/regressors to correlate policy interventions with socioeconomic metrics  
   - Sentiment analysis pipeline (e.g. spaCy, Transformers)  
4. **Reporting & Visualization**  
   - Automated report generation with key insights & recommendations  
   - Dashboards for interactive exploration of policy impacts  
5. **Scalability & Maintainability**  
   - Modular, containerized microservices (Docker)  
   - CI/CD with MLOps tooling (MLflow, Prefect/Apache Airflow)  

---

## 📋 Functional Requirements  
- **World Bank API Integration**  
  - Retrieve and update socioeconomic indicators on a schedule  
- **Policy Document Ingestion**  
  - PDF/text extraction → cleaning → storage  
- **NLP Services**  
  - Summarization endpoint  
  - Misinformation detection endpoint  
  - Sentiment analysis endpoint  
- **Correlation Engine**  
  - Statistical analysis module to compute effect sizes and significances  
- **Dashboard & Reports**  
  - Web-based UI (Streamlit/Flask or React) showing:  
    - Time-series of indicators vs. policy dates  
    - Geographic heatmaps of impact  
    - Top misinfo topics  

---

## ✅ Non-Functional Requirements  
- **Performance:**  
  - Summarization requests < 5 s  
  - Batch jobs complete -daily within 2 hours  
- **Security:**  
  - Secure API keys via environment variables  
  - HTTPS endpoints with token‐based auth  
- **Reliability & Monitoring:**  
  - 99.5% service uptime  
  
- **Portability:**  
  - Dockerized components for multi-cloud deployment (AWS/GCP)  

---

## ✍🏼 Methodology  
![image](https://github.com/user-attachments/assets/297e116f-861c-4f73-92e6-ed4517a6a702)

###  ✅ Non functional Requirements

Other minor requirements and considerations like Cloud deployable solution etc.


### 📦 Required Resources
- Hardware & OS: Linux dev machine (or cloud VM)
- IDE: JupyterLab, VS Code
- Version Control: Git/GitHub
- Model Tool: HuggingFace 
- Languages & Frameworks:
- Python 3.10+
- PyTorch, Transformers, scikit-learn
- Fine-Tuning Tech: PEFT, LoRA, QLoRA (4-bit Quantization)

🧪 Test Cases
- World Bank API returns latest indicator data within expected schema.
- Policy Extractor correctly parses text from a sample PDF.
- Summarizer produces coherent 3–5 sentence abstracts.
- Misinformation Detector flags injected fake statements with ≥ 85% precision.
- Correlation Module reproduces known effect estimates on synthetic data.
- Dashboard loads within 3 s and updates when new data arrives.


## Installation Instructions

```bash
git clone https://github.com/UNH-TCOE-ECECS/Team07-Orange/.git
cd socioeconomic-policy-analysis
```
