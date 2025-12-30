from chain import build_chain

RESUME_TEXT = """
Software engineer with 2 years experience.
Worked on backend systems using Python and FastAPI.
"""

def main():
    chain_v1 = build_chain("prompts/resume_summary_v1.yaml")
    chain_v2 = build_chain("prompts/resume_summary_v2.yaml")

    print("V1 OUTPUT:\n", chain_v1.invoke({"resume": RESUME_TEXT}).content)
    print("\nV2 OUTPUT:\n", chain_v2.invoke({"resume": RESUME_TEXT}).content)

if __name__ == "__main__":
    main()