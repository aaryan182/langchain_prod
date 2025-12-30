# app.py
from chain import build_chain

RESUME_TEXT = """
Aaryan Bajaj is a software engineer with 2 years of experience.
He has worked extensively with Python, FastAPI, PostgreSQL, and Redis.
"""

def main():
    chain = build_chain()

    result = chain.invoke(
        {"resume": RESUME_TEXT}
    )

    # This is now a Pydantic object
    print("Parsed object:", result)
    print("Skills:", result.skills)
    print("Experience:", result.years_of_experience)

if __name__ == "__main__":
    main()
