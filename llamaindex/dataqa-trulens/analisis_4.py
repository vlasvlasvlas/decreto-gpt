import utils
import os
import openai
import sys 
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")
openai.api_key
os.environ['OPENAI_API_KEY'] = api_key
#
# examples
# https://github.com/kevintsai/Building-and-Evaluating-Advanced-RAG-Applications/blob/main/L4-Auto-merging_Retrieval.ipynb
#
# SimpleDirectoryReader is a class that reads all the files in a directory and returns a list of documents
# It will select the best file reader based on the file extensions
# https://docs.llamaindex.ai/en/stable/examples/data_connectors/simple_directory_reader.html
#
# Load all (top-level) files from directory
# ,input_dir="/" 
# ,input=files="/asdf.pdf"
# ,required_exts=[".pdf", ".txt", ".md"] <- extensions to read
# ,recursive=True
# docs = reader.load_data()
# print(f"Loaded {len(docs)} docs")
#

# llamaindex
from llama_index import SimpleDirectoryReader,VectorStoreIndex,ServiceContext,Document
from llama_index.llms import OpenAI
#from langchain_community.llms import OpenAI

documents = SimpleDirectoryReader(
    input_files=["data/Analisis_Decreto_de_Necesidad_y_Urgencia_Bases_para_la_Reconstrucción.pdf"],
    
).load_data()

print(type(documents), "\n")
print(len(documents), "\n")
print(type(documents[0]))
print(documents[0])
print(f"Loaded {len(documents)} pages docs") # pages

# basic RAG pipeline
# Document is a class that represents a document



document = Document(text="\n\n".join([doc.text for doc in documents]))



# llm declare
# bge-small-en-v1.5 is a model that was trained on the BGE dataset
# https://huggingface.co/BAAI/bge-small-en-v1.5
# FlagEmbedding can map any text to a low-dimensional dense vector which can be used for tasks like retrieval, classification, clustering, or semantic search. And it also can be used in vector databases for LLMs.

llm = OpenAI(model="gpt-4-1106-preview", temperature=0.0)
service_context = ServiceContext.from_defaults(
    llm=llm, embed_model="local:BAAI/bge-small-en-v1.5"
)

index = VectorStoreIndex.from_documents([document],
                                        service_context=service_context)

query_engine = index.as_query_engine()

# query
response = query_engine.query(
    """
    Contexto: Eres el mejor analista de documentos de leyes con un IQ de 150. Tienes que ser minucioso y necesito que revises la totalidad de las paginas del documento, sin dejar nada por fuera. Se experto en el tema y no me falles.
    Pregunta: devolver en forma de items la totalidad de los temas que trata el documento presentado de forma minuciosa.
    Forma de respuesta: El texto suministrado es en español y la respuesta la necesito en español.
    """
)

print(str(response))
