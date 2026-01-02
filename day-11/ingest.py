from vectorstore import build_vectorstore

def ingest_documents(path: str):
    with open(path, "r") as f:
        text = f.read()
        
    chunks = [
        text[i:i+100]
        for i in range(0,len(text), 300)
    ]
    
    return build_vectorstore(chunks)