import numpy as np
import pandas as pd

def get_random_time_series(b=40, N=8):
    a = 1.8 + np.random.randn(1)[0] * 0.1
    b = 50 + np.random.randn(1)[0] * 5
    x = np.array(range(1, N + 1)) + np.random.randn(N) * 5
    y = a*x + b
    return y

def get_data(seed=42):
	np.random.seed(seed)
	company_1_dict = {'Company': 'Firma 1',
	                  'Year': list(range(2010, 2018)),
	                  'Product A': get_random_time_series(40, 8),
	                  'Product B': get_random_time_series(42, 8)}
	company_1_df = pd.DataFrame(company_1_dict)

	company_2_dict = {'Company': 'Firma 2',
	                  'Year': list(range(2010, 2018)),
	                  'Product A': get_random_time_series(45, 8),
	                  'Product B': get_random_time_series(43, 8)}
	company_2_df = pd.DataFrame(company_2_dict)

	company_3_dict = {'Company': 'Firma 3',
	                  'Year': list(range(2010, 2018)),
	                  'Product A': get_random_time_series(38, 8),
	                  'Product B': get_random_time_series(37, 8)}
	company_3_df = pd.DataFrame(company_3_dict)

	company_4_dict = {'Company': 'Firma 4',
	                  'Year': list(range(2010, 2018)),
	                  'Product A': get_random_time_series(41, 8),
	                  'Product B': get_random_time_series(39, 8)}
	company_4_df = pd.DataFrame(company_4_dict)

	frames = [company_1_df, company_2_df, company_3_df, company_4_df]

	data_df = pd.concat(frames)

	return data_df