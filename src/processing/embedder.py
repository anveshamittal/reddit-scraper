from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings  
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.processing.chunker import chunks  # your chunked Reddit text

from tenacity import retry, wait_random_exponential, stop_after_attempt

@retry(wait=wait_random_exponential(min=2, max=10), stop=stop_after_attempt(3))
def embed_chunks(chunks):
    # load HF model (no API key needed)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # create FAISS vector store
    index = FAISS.from_texts(chunks, embeddings)
    index.save_local("data/faiss_index")

    # test search
    return index

embeddings=embed_chunks(chunks)
