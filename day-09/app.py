from dotenv import load_dotenv
load_dotenv()

from router import build_router

def main():
    router = build_router()

    print(router("What is FastAPI?"))
    print(router("Summarize my resume against this JD"))
    print(router("Design a fault-tolerant trading system"))

if __name__ == "__main__":
    main()