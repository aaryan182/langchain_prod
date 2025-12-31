from langchain_core.runnables import RunnableLambda
from schema import FinalResult

def build_merger():
    def merge(results):
        return FinalResult(
            classification=results["classification"],
            extraction=results["extraction"]
        )

    return RunnableLambda(merge)