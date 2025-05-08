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
<P>This project addresses the challenges faced by policy analysts who spend excessive time analyzing raw data by integrating AI and LLM-based techniques to evaluate public health policies. By leveraging a fine-tuned LLaMA 3.2B model and structured datasets, our system provides a scalable, evidence-driven framework that transforms complex socioeconomic data into meaningful insights. The platform enables policy analysts to quickly perform general analysis, comparative analysis, and predictive analysis of public health policies and their socioeconomic impacts, bridging the gap between policy design and on-ground realities.


### 🫧 Background

<P>Policy analysts often spend excessive time buried in raw data and documents when evaluating public health policies. The direct and indirect socioeconomic impacts of these policies remain uncertain and hard to quantify using traditional methods. Our end-to-end lifecycle solution addresses this challenge by:

1. Ingesting raw data from multiple sources
2. Converting it to meaningful context for LLM learning
3. Fine-tuning LLaMA 3.2B on this specialized dataset
4. Providing an intuitive interface for general, comparative, and predictive analysis

This enables analysts to quickly detect trends, understand policy implications, and identify inequities without manual data processing. </P>


## 💻 System Architecture

The system consists of four main components:

1. **Data Collection**
   - Research papers
   - Census data
   - Policy outcomes

2. **Data Processing & Feature Engineering**
   - Text extraction
   - Data cleaning
   - Feature engineering
   - Training dataset creation

3. **Model Fine-tuning**
   - LLaMA 3.2B with LoRA adaptation
   - LLaMA 3.2B with QLoRA adaptation
   - Cross-encoder reranker (ms-marco-MiniLM-L-6-v2)

4. **Evaluation & Deployment**
   - Metrics: Accuracy, Perplexity, ROUGE Score, Inference Speed, Policy Relevance
   - StreamlitGradio interface for interactive use

## ✍🏼 Methodology  
![image](https://github.com/user-attachments/assets/297e116f-861c-4f73-92e6-ed4517a6a702)

## 📋 Requirements

### High-Level Requirements

1. Analyze socioeconomic impacts of public health policies through AI-powered insights
2. Provide intuitive visualization tools for policy impact analysis
3. Support real-time misinformation detection and trend monitoring
4. Enable comparative analysis across different demographic groups and regions
5. Generate evidence-based policy recommendations

### Functional Requirements

1. **Data Processing**
   - Ingest and process structured data from US Census, World Bank, and KFF
   - Extract meaningful information from unstructured policy documents
   - Clean and normalize datasets for consistent analysis
   - Create and maintain FAISS vector database for semantic search

2. **Analysis Capabilities**
   - Perform general analysis of public health policies
   - Generate comparative analysis between policies and regions
   - Provide predictive analysis for policy outcomes
   - Detect and summarize misinformation trends
   - Track public sentiment related to policies

3. **User Interface**
   - Dynamic policy querying through Streamlit/Gradio
   - Interactive visualization of policy impacts
   - Customizable reporting features
   - Multi-level access for different user types

### Non-Functional Requirements

1. **Performance**
   - Support response times under 2 seconds for queries
   - Handle concurrent users with minimal latency
   - Optimize memory usage during inference

2. **Scalability**
   - Support expansion to additional policy domains
   - Scale to accommodate growing datasets
   - Allow for model updates and improvements

3. **Security**
   - Ensure data privacy and compliance with regulations
   - Provide secure access controls
   - Maintain audit logs of system usage

4. **Reliability**
   - Ensure high availability of the system
   - Implement error handling and recovery mechanisms
   - Regular backups of datasets and model weights



---



## 🛠️ Technologies Used

- **Programming Language**: Python
- **LLM Model**: LLaMA 3.2B Parameters
- **Fine-tuning**: LoRA technique
- **Data Pipeline**: AWS Platform
- **Libraries**: Hugging Face Transformers
- **Vector Database**: FAISS for high-speed semantic search
- **Frontend**: Streamlit interface

## 📊 Data Sources

### Structured Data
- US Census socioeconomic indicators (income, employment, education, healthcare access)
- World Bank data
- KFF (Kaiser Family Foundation) health policy data

### Unstructured Data
- Public health policy documents
- Research papers summarizing policy impacts




## Installation Instructions

```bash
git clone https://github.com/UNH-TCOE-ECECS/Team07-Orange/.git
cd socioeconomic-policy-analysis
```
