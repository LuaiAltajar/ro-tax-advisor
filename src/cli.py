from src.ingestion.embed import embed
from src.ingestion.parse import chunk
from src.ingestion.vectorstore import save_embeddings
from src.rag.llm import question_answer

def run_cli(question: str):
    return question_answer(question)

if __name__ == '__main__':
    # INPUT_FILE = 'input/Legea nr.227_2015.html'
    # chunks = chunk(INPUT_FILE)
    # embeddings = embed(chunks)
    # save_embeddings(embeddings, 'tmp/vector_db')
    question = input("Intrebarea: ").strip()
    print(run_cli(question))
    