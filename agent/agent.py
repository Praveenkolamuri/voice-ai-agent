from agent.tools import (
    check_availability,
    book_appointment,
    cancel_appointment,
    reschedule_appointment
)

from memory.session_memory import get_context, save_context

def process_request(text, session_id):

    context = get_context(session_id)

    text = text.lower()

    if "book" in text:

        slots = check_availability("cardiologist", "tomorrow")

        save_context(session_id, {"intent": "booking"})

        return f"Available slots are {slots}. Which time would you like?"

    if "cancel" in text:

        return cancel_appointment(session_id)

    if "reschedule" in text:

        return reschedule_appointment(session_id)

    return "Sorry, I couldn't understand. Could you repeat?"