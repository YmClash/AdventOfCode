from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import UnstructuredFileLoader
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings
import pickle


with open('Universelle des droit des humain.txt','r') as fichier :
    data = fichier.read()


print(f'Data Loading..')

loader = UnstructuredFileLoader(data)
raw_documents = loader.load()

print(f'Data Loading...done')


print("Extract & Splitting Data...")
data_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=600,
    chunk_overlap=100,
    length_function=len,
)

doc = data_splitter.split_documents(raw_documents)

print(f'print("Extract & Splitting Data...done...')

print(f'print("Extract & Splitting Data...done...')

print("Creating a Vector Database ")

embeddings = OpenAIEmbeddings()
vector_DB = FAISS.from_documents(doc,embeddings)

with open('vector_DB', 'wb') as datastore:
    pickle.dump(vector_DB,datastore)





