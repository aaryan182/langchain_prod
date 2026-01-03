TEST_CASES = [
    {
        "question": "What is the API rate limit?",
        "expected_behavior": "answer",
        "must_contain": "100 requests per minute"
    },
    {
        "question": "How long do password resets last?",
        "expected_behavior": "answer",
        "must_contain": "15 minutes"
    },
    {
        "question": "Do you support OAuth?",
        "expected_behavior": "abstain",
        "must_contain": None
    }
]
