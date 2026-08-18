import os
from langchain_groq import ChatGroq
from .rag import document_search
from dotenv import load_dotenv

load_dotenv()

def question_answer(question):
    text, metadata = document_search(question)

    context = ""
    for fragment in text:
        context = context + fragment + "\n\n---\n\n"

    prompt = f"""Esti un asistent fiscal expert in legistatia din Romania.
                Raspunde la intrebare folosind doar informatiile furnizate mai jos.
                Adauga surse.

                CONTEXT DIN CODUL FISCAL:
                {context}

                INTREBARE:
                {question}"""


    llm = ChatGroq(
                    model="openai/gpt-oss-120b"
                    ,groq_api_key=os.getenv("GROQ_API_KEY")
                   )
    answer = llm.invoke(prompt)
    return answer.content


