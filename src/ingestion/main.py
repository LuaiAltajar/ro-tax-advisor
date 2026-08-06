from parse import chunk
from embed import embed, link
from vectorstore import save_embeddings

chunks, metadata = chunk(link)
embeddings = embed(chunks)

save_embeddings (embeddings)
