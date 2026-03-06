session_store = {}

def save_context(session_id, context):

    session_store[session_id] = context


def get_context(session_id):

    return session_store.get(session_id, {})