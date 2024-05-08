from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
ollama = Ollama(model="llama2")
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] ="true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please response to the user queries"),
    ("user", "Question: {question}")
])

#intialize streamlit
st.title('ChatBot')
input_text = st.text_input("Search the topic u want")

#ollama llama2 LLM
llm = Ollama(model="llama2")
output_parser = StrOutputParser
chain = prompt|llm|output_parser