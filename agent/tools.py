appointments = []

def check_availability(doctor, date):

    slots = ["10:00 AM", "2:00 PM", "4:30 PM"]

    return ", ".join(slots)


def book_appointment(patient, doctor, date, time):

    for a in appointments:

        if a["doctor"] == doctor and a["time"] == time:
            return "That slot is already booked."

    appointment = {
        "patient": patient,
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)

    return "Appointment confirmed."


def cancel_appointment(session_id):

    return "Your appointment has been cancelled."


def reschedule_appointment(session_id):

    return "Let's find a new slot for your appointment."