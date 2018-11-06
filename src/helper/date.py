from datetime import datetime

def str_to_datetime(str_to_cast: str):
    if str_to_cast is None:
        return None
    try:
        str_to_cast = str_to_cast
        return datetime.strptime(str_to_cast, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            return datetime.strptime(str_to_cast, "%Y-%m-%d")
        except ValueError:
            raise ValueError("impossible to cast {} to a datetime".format(str_to_cast))

def datetime_to_str(datetime_to_cast: datetime):
    if datetime_to_cast is None:
        return None
    try:
        # remove ms if they exist
        return datetime_to_cast.isoformat(' ')
    except ValueError:
        raise ValueError("impossible to cast {} to a string".format(datetime_to_cast))
