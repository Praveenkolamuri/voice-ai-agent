from datetime import datetime

def validate_slot(date, time):

    now = datetime.now()

    if datetime.strptime(date, "%Y-%m-%d") < now:
        return False

    return True