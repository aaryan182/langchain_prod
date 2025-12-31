from langchain.memory import ConversationBufferMemory

def build_short_term_memory():
    """
    Short term memory:
    - Only recent conversation
    - Used for continuity
    - Never persisted long term
    """
    return ConversationBufferMemory(
        return_messages = True,
        memory_key = "chat_history"
    )