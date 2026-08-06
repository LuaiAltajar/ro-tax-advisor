import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent 
sys.path.append(str(ROOT_DIR))

from ingestion.embed import embed
from ingestion.vectorstore import load_vectorstore


def document_search(question, top=5):
    database = load_vectorstore(store_name='vector_db')

    vector_question = embed([question])[0]

    results = database.similarity_search_by_vector(embedding=list(vector_question.tolist()), k = top)

    text = []
    metadata = []

    for elem in results:
        text.append(elem.page_content)
        metadata.append(elem.metadata)

    return text, metadata
