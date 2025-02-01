from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def get_document_splits(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    splits = text_splitter.split_documents(docs)
    return splits
