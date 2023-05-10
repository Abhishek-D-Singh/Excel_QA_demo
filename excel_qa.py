# -*- coding: utf-8 -*-
"""Excel_QA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qU1_H_vaeCDQ1VqYPmxL1tbj-aEkeiIN

Installation of libraries[langchain,openai,openpyxl]
"""

#!pip -q install langchain openai

#!pip install openpyxl

#"""Importing required libraries[OS for storing API KEY and Pandas for reading excel file]"""
import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import tempfile
import os

#os.environ["OPENAI_API_KEY"] = "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"

import pandas as pd

#"""Using files functionality from collab to read file locally in variable xls file"""

#from google.colab import files
#uploaded = files.upload()

#"""Converting the file to csv format to parse through pandas library"""
user_api_key = st.sidebar.text_input(
    label="#### Your OpenAI API key 👇",
    placeholder="Paste your openAI API key, sk-",
    type="password")

uploaded_file = st.sidebar.file_uploader("upload", type="xlsx")
if uploaded_file is not None :
# Read the XLS file using pandas and openpyxl as the engine
    data_df = pd.read_excel(uploaded_file, engine='openpyxl')
    csv_file = data_df.to_csv(index=False)
    buffer = io.StringIO(csv_file)
    csv =  pd.read_csv(filepath_or_buffer = buffer, header = 1)

# Save the data as a CSV file


"""Importing langchain agents and llms"""

from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

"""Calling langchain csv agent to pass the csv file for QA"""

agent = create_csv_agent(OpenAI(temperature=0), 
                         'csv', 
                         verbose=True)

agent.run("how many rows are there?")

agent.run("What are the column names?")

agent.run("For the Campaign C631079 and INTERNAL ORDER 901829794, what is DME FSItem SAP ?")
#if uploaded_file :
 #   with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
  #      tmp_file.write(uploaded_file.getvalue())
   #     tmp_file_path = tmp_file.name
#xls_file = r'/content/Sample_Excel.xlsx'
#output_csv = 'Sample_Excel.csv'
