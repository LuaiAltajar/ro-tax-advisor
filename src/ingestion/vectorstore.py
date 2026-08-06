from langchain_chroma import Chroma
from .parse import chunk
from .embed import link


def save_embeddings(embeddings, store_name='vector_db'):
    """
    @param embeddings List/Numpy array of embeddings
    @return None
    """
    chunks, metadata = chunk(link)

    ids = []
    for i in range(len(chunks)):
        ids.append(f"id_{i}")

    vector_db = Chroma(persist_directory=store_name)

    vector_db.add_texts(texts=chunks,embeddings=embeddings, metadatas=metadata, ids=ids)


def load_vectorstore(store_name='vector_db'):
    return Chroma(persist_directory=store_name)