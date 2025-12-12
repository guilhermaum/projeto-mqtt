from datetime import datetime

def get_date_time_as_long():
    formatted = datetime.now().strftime("%d%m%Y%H%M")
    return int(formatted)