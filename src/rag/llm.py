from langchain_openai import ChatOpenAI
from rag import document_search


def question_answer(question):
    text, metadata = document_search(question)

    context = ""
    for fragment in text:
        context = context + fragment + "\n\n---\n\n"

    prompt = f"""Ești un asistent fiscal expert în legislația din România.
                Răspunde la întrebare folosind DOAR informațiile furnizate mai jos.

                CONTEXT DIN CODUL FISCAL:
                {context}

                ÎNTREBARE:
                {question}"""


    llm = ChatOpenAI(model="gpt-4o-mini")
    answer = llm.invoke(prompt)
    return answer.content


