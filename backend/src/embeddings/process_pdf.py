from utils.text_splitter import get_document_splits
from langchain_community.document_loaders import PyPDFLoader

async def extract_text_from_pdf(path: str):
    """Extract text from a PDF file"""
    loader = PyPDFLoader(path)
    pages = []
    async for page in loader.alazy_load():
        print(page)
        print(type(page))
        pages.append(page)
    return pages