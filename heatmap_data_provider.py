from geopy.geocoders import Nominatim
import pandas as pd
import re
from statistics import mode 

CSV_PATH = "assets\\heatmapdata.csv"
df = pd.read_csv(CSV_PATH)

def getHeatmapData():
    global df
    df = pd.read_csv(CSV_PATH)
    return df

def getBestVoivodeship():
    global df
    return df['Voivodeship'].value_counts().index[0]