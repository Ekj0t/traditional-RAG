from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyMuPDFLoader

# Text Loader
# document_loader = TextLoader("./data/textFiles/springBoot.txt", encoding="utf8")
# document = document_loader.load()
# print(document)

# PDF Loader
# pdf_loader = PyMuPDFLoader("./data/pdfFiles/Sartre-The-Wall-reading.pdf")
# pdf_document = pdf_loader.load()
# print(pdf_document)

#Directory Loader
# dir_loader = DirectoryLoader(
#     "./data/textFiles",   # Directory path
#     glob = "**/*.txt",    # File type to find
#     loader_cls = TextLoader   # Loader class to use
# )
# dir = dir_loader.load()
# print(dir)