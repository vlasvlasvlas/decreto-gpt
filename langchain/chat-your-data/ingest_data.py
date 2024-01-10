from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import UnstructuredFileLoader
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle


print("Loading data...")
loader = UnstructuredFileLoader("../../dnu_a_texto.txt")
raw_documents = loader.load()


print("Splitting text...")
text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=600,
    chunk_overlap=100, #superponer bordes del texto para que no se pierda información
    length_function=len,    
)

documents = text_splitter.split_documents(raw_documents)


print("Creating vectorstore...")
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(documents, embeddings) #https://ai.meta.com/tools/faiss/
with open("vectorstore.pkl", "wb") as f:
    pickle.dump(vectorstore, f)
