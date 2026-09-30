# @Author: Dhaval Patel Copyrights Codebasics Inc. and LearnerX Pvt Ltd.

from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path
from prompt import PROMPT, EXAMPLE_PROMPT
from langchain_classic.chains import RetrievalQAWithSourcesChain
from langchain_classic.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from prompt import PROMPT, EXAMPLE_PROMPT





load_dotenv()

# Constants
CHUNK_SIZE = 1000
EMBEDDING_MODEL = "thenlper/gte-small"
VECTORSTORE_DIR = Path(__file__).parent / "resources/vectorstore"
COLLECTION_NAME = "real_estate"

llm = None
vector_store = None


def initialize_components():
    global llm, vector_store

    if llm is None:
        llm = ChatGroq(model="openai/gpt-oss-20b", temperature=0.9, max_tokens=500)

    if vector_store is None:
        ef = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"trust_remote_code": True}
        )

        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=ef,
            persist_directory=str(VECTORSTORE_DIR)
        )


def process_urls(urls):
    """
    This function scraps data from a url and stores it in a vector db
    :param urls: input urls
    :return:
    """
    yield "Initializing Components"
    initialize_components()

    yield "Resetting vector store...✅"
    vector_store.reset_collection()

    yield "Loading data...✅"
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    yield "Splitting text into chunks...✅"
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=CHUNK_SIZE
    )
    docs = text_splitter.split_documents(data)
    print("Chunks:", len(docs))
    print("First chunk:", docs[0].page_content[:1000])

    yield "Add chunks to vector database...✅"
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(docs, ids=uuids)

    print("Done adding docs to vector database...✅")

def generate_answer(query):
    if not vector_store:
        raise RuntimeError("Vector database is not initialized ")
    qa_chain = load_qa_with_sources_chain(llm, chain_type="stuff",
                                          prompt=PROMPT,
                                          document_prompt=EXAMPLE_PROMPT)
    chain = RetrievalQAWithSourcesChain(combine_documents_chain=qa_chain, retriever=vector_store.as_retriever(),
                                            reduce_k_below_max_tokens=True, max_tokens_limit=8000,
                                            return_source_documents=True)
    result = chain.invoke({"question": query}, return_only_outputs=True)
    sources_docs = [doc.metadata['source'] for doc in result['source_documents']]

    # Remove duplicate URLs
    sources_docs = list(dict.fromkeys(sources_docs))
    
    return result['answer'], sources_docs


'''if __name__ == "__main__":
    urls = [
        "https://www.pbs.org/newshour/economy/in-2024-us-home-sales-fell-to-the-lowest-level-in-nearly-30-years-as-prices-and-mortgages-soar"
    ]

    process_urls(urls)
    answer, sources = generate_answer("The average rate on a 30-year mortgage")
    print(f"Answer: {answer}")
    print(f"Sources: {sources}")'''