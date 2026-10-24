from geopy.distance import geodesic
from datetime import datetime


def calculate_distance(user_location , spot1):
    dis = round(geodesic(user_location , spot1).km,2)
    return dis


current_time = datetime.now().strftime("%H:%M")

def is_open_spot(row):
    open_time = row['opening_time']
    close_time = row['closing_time']

    is_open = open_time <= current_time <= close_time
    if is_open:
        return 'Open'
    else:
        return 'Close'