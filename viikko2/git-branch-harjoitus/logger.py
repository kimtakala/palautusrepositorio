'very informative line'
from datetime import datetime

def logger(viesti):
    'it does the logging'
    print(f"{datetime.now()}: {viesti}")
