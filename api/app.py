from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")
os.environ['OPENAI_API_KEY'] = openai_api_key

# Set the OpenAI API key environment variable
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Initialize the FastAPI app with metadata
app = FastAPI(
    title="Creative Writing Service",
    version="1.0",
    description="An API server for generating creative writing pieces using AI models."
)

# Initialize the OpenAI and Ollama models
openai_model = ChatOpenAI()
ollama_model = Ollama(model="llama2")

# Define the prompt templates for essays and poems
essay_prompt = ChatPromptTemplate.from_template("Create a concise essay on '{topic}' within 100 words.")
poem_prompt = ChatPromptTemplate.from_template("Craft a simple poem about '{topic}' suitable for a child, capped at 100 words.")

# Register the OpenAI route for generic queries
add_routes(app, openai_model, path="/openai")

# Register the route for generating essays
add_routes(app, essay_prompt | openai_model, path="/essay")

# Register the route for generating poems with the Ollama model
add_routes(app, poem_prompt | ollama_model, path="/poem")

# Run the server using Uvicorn if the script is the main program
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000,reload=True)
