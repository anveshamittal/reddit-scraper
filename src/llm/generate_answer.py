from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from dotenv import load_dotenv
import os

load_dotenv()

def generate_persona():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    index = FAISS.load_local("data/faiss_index", embeddings, allow_dangerous_deserialization=True)

    results = index.similarity_search("profile summary", k=20)
    docs = [Document(page_content=r.page_content) for r in results]

    llm = ChatOpenAI(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        default_query={"api-version": "preview"}
    )

    prompt = PromptTemplate.from_template("""
You are a profiler bot. Given the following Reddit comments by one user, infer a detailed persona.

Include:
- probable age group
- interests and hobbies
- personality traits
- profession (if any)
- tone and writing style
- political/social views (if evident)
- anything else worth noting

Reddit Comments:
{context}

Persona Summary:
""")

    parser = StrOutputParser()
    summarizer = create_stuff_documents_chain(llm, prompt, output_parser=parser)

    result = summarizer.invoke({"context": docs})
    return result

persona = generate_persona()
