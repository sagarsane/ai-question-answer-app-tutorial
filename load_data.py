from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import DirectoryLoader
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import key_param
from mongo_setup import collection

loader = DirectoryLoader( './sample_files', glob='./*.txt', show_progress=True )
data = loader.load()

embeddings = OpenAIEmbeddings( openai_api_key=key_param.openai_api_key)

vectorStore = MongoDBAtlasVectorSearch.from_documents( data, embeddings, collection=collection )