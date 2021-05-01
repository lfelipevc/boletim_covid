import pandas as pd
import os
files = os.listdir("../boletins/csv")
files.sort()
tables = [pd.read_csv("../boletins/csv/"+f) for f in files]
tobitos = map(lambda x: x[['bairro', 'obitos']], tables)
