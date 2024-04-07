# import requests
# import streamlit as st

# def get_openai_response(input_text):
#     response=requests.post("http://localhost:8000/essay/invoke",
#     json={'input':{'topic':input_text}})

#     return response.json()['output']['content']

# def get_ollama_response(input_text):
#     response=requests.post(
#     "http://localhost:8000/poem/invoke",
#     json={'input':{'topic':input_text}})

#     return response.json()['output']

#     ## streamlit framework

# st.title('Langchain Demo With LLAMA2 API')
# input_text=st.text_input("Write an essay on")
# input_text1=st.text_input("Write a poem on")

# if input_text:
#     st.write(get_openai_response(input_text))

# if input_text1:
#     st.write(get_ollama_response(input_text1))


import requests
import streamlit as st

# Set the backend service URLs
OPENAI_ESSAY_URL = "http://localhost:8000/essay"
OLLAMA_POEM_URL = "http://localhost:8000/poem"

# Streamlit interface for essay input
st.title('Creative Writing Assistant')
input_text_essay = st.text_input("Enter a topic for the essay:")
if input_text_essay:
    response = requests.post(OPENAI_ESSAY_URL, json={'input': {'topic': input_text_essay}})
    if response.ok:
        st.write("### Essay")
        st.write(response.json()['output']['content'])
    else:
        st.error(f"Failed to get the essay: {response.text}")

# Streamlit interface for poem input
input_text_poem = st.text_input("Enter a topic for the poem:")
if input_text_poem:
    response = requests.post(OLLAMA_POEM_URL, json={'input': {'topic': input_text_poem}})
    if response.ok:
        st.write("### Poem")
        st.write(response.json()['output']['content'])
    else:
        st.error(f"Failed to get the poem: {response.text}")
