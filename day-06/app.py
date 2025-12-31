from langchain_core.runnables import RunnableParallel
from chains.classifier import build_classifier
from chains.extractor import build_extractor
from chains.final_merge import build_merger

RESUME_TEXT = """
Aaryan Bajaj is a software engineer with 2 years of experience.
Worked with Python, FastAPI, PostgreSQL.
"""

def main():
    classifier = build_classifier()
    extractor = build_extractor()
    merger = build_merger()

    # Parallel execution DAG
    dag = RunnableParallel(
        classification=classifier,
        extraction=extractor
    ) | merger

    result = dag.invoke(RESUME_TEXT)

    print(result)

if __name__ == "__main__":
    main()