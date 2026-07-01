import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

def process_all_pdfs(pdf_directory):
    all_documents = []

    pdf_directory = Path(pdf_directory)

    pdf_files = list(pdf_directory.rglob("*.pdf"))

    print(f"Found {len(pdf_files)} PDF files to process.")

    for pdf_file in pdf_files:
        print(f"Processing {pdf_file.name}")

        try:
            loader = PyPDFLoader(str(pdf_file))
            documents = loader.load()

            for doc in documents:
                doc.metadata["source"] = str(pdf_file)
                doc.metadata["file_type"] = "pdf"
            
            all_documents.extend(documents)

            print(f"✓ Loaded {len(documents)} pages.")

        except Exception as e:
            print(f"Error processing {pdf_file.name}: {e}")
    
    print(f"Total pages loaded: {len(all_documents)}")

    return all_documents

all_pdf_documents = process_all_pdfs("./data")
print(all_pdf_documents)


