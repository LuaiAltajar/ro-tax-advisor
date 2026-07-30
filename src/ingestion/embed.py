from sentence_transformers import SentenceTransformer
from typing import List
from parse import chunk

link = 'https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2016.htm'

def embed(chunks: List):
    """
    @param chunks Chunks of text
    @return List / Numpy array of embeddings 
    """
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    embeddings = model.encode(chunks)

    return embeddings

