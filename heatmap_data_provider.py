from geopy.geocoders import Nominatim
import pandas as pd
import re
from statistics import mode 

CSV_PATH = "assets\\population_pol_2019-07-01.csv"

def getHeatmapData():
    df = pd.read_csv(CSV_PATH).sample(n=10000, random_state=1).sample(axis=1, n=3, random_state=1)
    return df