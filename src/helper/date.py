from datetime import datetime

def str_to_datetime(str_to_cast: str):
    try:
        return datetime.strptime(str_to_cast, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            return datetime.strptime(str_to_cast, "%Y-%m-%d")
        except ValueError:
            raise ValueError("impossible to cast {} to a datetime".format(str_to_cast))
