# RAG Application with AWS Bedrock and LangChain

## Overview
Welcome to the **RAG App**, an advanced Retrieval-Augmented Generation (RAG) application leveraging AWS Bedrock, LangChain, and cutting-edge language models like Amazon Titan and Meta Llama. This project demonstrates a seamless pipeline for document ingestion, vector embedding, and answer generation, wrapped in a user-friendly Streamlit interface.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Key Technologies Used](#key-technologies-used)
- [Application Workflow](#application-workflow)
- [Installation](#installation)
- [Usage](#usage)
- [Snapshots](#snapshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction
This repository contains a powerful **Retrieval-Augmented Generation (RAG)** application built using **AWS Bedrock** and **LangChain**. The application is designed to process data, create vector embeddings, store them efficiently, and generate accurate answers to user queries using state-of-the-art language models like **Amazon Titan** and **Meta's Llama**.


## Features
- **Data Ingestion**: Load and process PDF files, splitting them into manageable chunks.
- **Vector Embeddings**: Utilize the **Amazon Titan Embedding Model** to generate high-quality vector embeddings of the document data.
- **Vector Storage**: Store and manage vector embeddings using the **FAISS (Facebook AI Similarity Search)** library and use it for efficient **similarity search** and clustering of vectors.
- **Language Models**: Generate responses using:
  - **Amazon Titan LLM**
  - **Meta Llama LLM** (via AWS Bedrock API)
- **Streamlit Interface**: An interactive UI built using **Streamlit** to make querying seamless and intuitive.

---

## Key Technologies Used

### Libraries and Frameworks
- **LangChain**: For orchestrating the RAG pipeline.
- **AWS Bedrock**: For embedding generation and LLM inference.
- **FAISS**: To efficiently store and retrieve vector embeddings.
- **Streamlit**: For creating a user-friendly web interface.
- **PyPDF**: Handles PDF file ingestion and splitting.
- **boto3**: AWS SDK for Python to interact with AWS services.

---

## Application Workflow

1. **Data Ingestion**:
   - PDF files are loaded and processed using the **PyPDF** library.
   - Documents are split into smaller chunks for embedding generation.

2. **Vector Embeddings**:
   - Create vector embeddings for text chunks using **Amazon Titan Embedding Model**.

3. **Vector Store**:
   - The FAISS library is employed to create and manage vector stores for efficient retrieval.

4. **Query Processing**:
   - Accept user queries via the **Streamlit** interface.
   - Retrieve relevant chunks from the vector store based on similarity.
   - Use **LangChain** to process the retrieved data and construct the final prompt.

5. **Answer Generation**:
   - Pass the constructed prompt to **Amazon Titan LLM** or **Meta Llama LLM** (via Bedrock API).
   - Display the generated answer in the Streamlit app.

---
## Snapshots
![alt text](<SS 1.png>)
![alt text](<Screenshot 2025-01-10 at 8.17.09 PM.png>)
![alt text](<Screenshot 2025-01-10 at 8.17.28 PM.png>)
![alt text](<Screenshot 2025-01-10 at 8.17.56 PM.png>)
![alt text](<Screenshot 2025-01-10 at 8.18.17 PM.png>)
![alt text](<Screenshot 2025-01-10 at 8.18.52 PM.png>)
![alt text](<Screenshot 2025-01-10 at 8.24.26 PM.png>)
![alt text](<Screenshot 2025-01-10 at 8.24.40 PM.png>)
![alt text](<Screenshot 2025-01-10 at 8.25.26 PM.png>)    
---
## Installation

### Prerequisites
- Python 
- AWS account with Bedrock access

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure AWS credentials:
   ```bash
   aws configure
   ```
   Ensure you have the necessary permissions to access AWS Bedrock.
4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

---

## Usage
1. Place your PDF files in the `data/` folder.
2. Launch the application.
```
streamlit run app.py
```
3. Enter your query in the Streamlit interface.
4. Select the desired model (**Amazon Titan** or **Meta Llama**) for answer generation.
5. View the results in the app.

---


## Future Enhancements
- Add support for additional LLMs.
- Implement real-time feedback for query improvements.
- Enhance the Streamlit UI for better user experience.
- Optimize vector storage and retrieval for larger datasets.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- [AWS Bedrock](https://aws.amazon.com/bedrock/)
- [LangChain](https://langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
