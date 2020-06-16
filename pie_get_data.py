import pandas as pd


def get_pie_data(year):
    df =  pd.DataFrame({
        'brand': ['Golf', 'Mustang', 'Octavia', 'Multipla', 'Focus']*3,
        'price': [20000, 60000, 15000, 10000, 30000, 18000, 65000, 17000, 10000, 35000, 21000, 50000, 14000, 11000, 34000],
        'year': [*[2014] * 5, *[2015] * 5, *[2016] * 5]
    })
    return df.loc[df['year'] == year]

def get_year_price_sum(year):
    return sum(get_pie_data(year)['price'])