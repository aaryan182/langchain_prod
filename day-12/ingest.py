from vectorstore import build_vectorstore

def ingest_documents(path: str):
    with open(path, "r") as f:
        text = f.read()

    # Slightly larger chunks for better semantic coherence
    chunk_size = 400
    overlap = 50

    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])

    return build_vectorstore(chunks)