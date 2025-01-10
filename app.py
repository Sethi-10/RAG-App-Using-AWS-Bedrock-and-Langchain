import json
import os
import boto3
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFDirectoryLoader

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock", region_name="us-east-1")

# Initialize Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock)

# Load PDF files and split into chunks
def data_ingestion():
    loader = PyPDFDirectoryLoader("data")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    docs = text_splitter.split_documents(documents)
    return docs

# Vector embedding and vector store
def get_vector_store(docs):
    vectorstore_faiss = FAISS.from_documents(
        docs,
        embedding=bedrock_embeddings
    )
    vectorstore_faiss.save_local("faiss_index")

from langchain_aws import BedrockLLM

# Initialize the Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Instantiate the LLM

titan_llm = BedrockLLM(
    model_id="amazon.titan-text-lite-v1",
    client=bedrock,
    model_kwargs={"temperature": 0.7}
)

llama_llm = BedrockLLM(
    model_id="meta.llama3-8b-instruct-v1:0",
    client=bedrock,
    model_kwargs={"max_tokens": 512}
)

# Prompt template for LLM
prompt_template = """
Human: Use the following pieces of context to provide a 
concise answer to the question at the end but summarize with 
at least 250 words and include detailed explanations. If you don't know the answer, 
just say that you don't know; do not try to make up an answer.

<context>
{context}
</context>

Question: {question}

Assistant:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)


def get_response_llm(llm,vectorstore_faiss,query):
    qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore_faiss.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    ),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)
    answer = qa.invoke({"query": query})
    return answer['result']


import streamlit as st
def main():
    st.set_page_config(page_title="Chat PDF with AWS Bedrock", layout="wide")
    
    st.header("Chat with PDF using AWS Bedrock💁")

    user_question = st.text_input("Ask a Question from the PDF Files")
   
    
    with st.sidebar:
        st.title("Update Or Create Vector Store:")
        
        if st.button("Vectors Update"):
            with st.spinner("Processing..."):
                docs = data_ingestion()
                get_vector_store(docs)
                st.success("Vector store updated successfully")
                


    if st.button("Titan Output"):
        with st.spinner("Processing..."):
            faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
            llm=titan_llm
            
            #faiss_index = get_vector_store(docs)
            st.write(get_response_llm(llm,faiss_index,user_question))
            st.success("Response generated using Amazon Titan")

    if st.button("Llama2 Output"):
        with st.spinner("Processing..."):
            faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
            llm=llama_llm
            
            #faiss_index = get_vector_store(docs)
            st.write(get_response_llm(llm,faiss_index,user_question))
            st.success("Response generated using Llama2.e")
    

if __name__ == "__main__":
    main()
