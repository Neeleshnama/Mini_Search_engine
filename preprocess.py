from modules import *
from loader import *


def drop_nan(data):
    d = load_data()
    d.dropna(inplace=True)
    return d
