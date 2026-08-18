import os
from phoenix.evals import HallucinationEvaluator, RelevanceEvaluator, OpenAIModel, QAEvaluator

def _build_model():
    return OpenAIModel(model=os.getenv("MODEL_NAME", "gpt-4o-mini"))


def functie_de_evaluare():
    pass