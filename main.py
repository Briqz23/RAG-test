from langchain.documents_loaders import DirectoryLoader

DATA_PATH = 'data'

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob='*.md')
    documents = loader.load()
    return loader.load()