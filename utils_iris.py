import seaborn as sns


def iris_data(unknowns = [113, 62, 41, 91, 125]):
    
    iris = sns.load_dataset('iris')
    correctAnwsers = {}
    for i in range(len(unknowns)):
        correctAnwsers[i+1] = iris.loc[unknowns[i], 'species']
    iris.loc[unknowns, 'species'] = "nieznane"
    #move unknowns to the end of the dataframe (as to make symbol 'x' for unknown in plotly)
    iris['id'] = ''
    for i in range(len(unknowns)):
        iris.iloc[-(i+1)], iris.iloc[unknowns[i]] = iris.iloc[unknowns[i]], iris.iloc[-(i+1)]
        iris.loc[iris.shape[0]-(i+1), 'id'] = str(i+1)
      
    return iris, correctAnwsers