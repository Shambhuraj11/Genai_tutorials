import streamlit as st 
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os 
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2')
os.environ['LANGCHAIN_ENDPOINT'] = os.getenv('LANGCHAIN_ENDPOINT')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
groq_api_key= os.environ['GROQ_API_KEY']

def get_llm_response(Question:str):
    llm = ChatGroq(model="llama3-8b-8192")
    response = llm.invoke(Question)
    return response.content

# Initilize Streamlit app

st.set_page_config(page_title="Q&A Demo wuth Groq llama-3-8b")

st.header("Langchain Application")

input = st.text_input("Type question here: ", key="input")

submit = st.button("Ask Question")

if submit:
    response = get_llm_response(input)
    if response:
        st.subheader("The response is")
        st.write(response)

    
