from sentence_transformers import SentenceTransformer
from typing import List
from .parse import chunk


link = 'https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2016.htm'

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def embed(chunks: List):
    """
    @param chunks Chunks of text
    @return List / Numpy array of embeddings 
    """

    embeddings = model.encode(chunks)

    return embeddings

