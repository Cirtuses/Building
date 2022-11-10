import execute
import pandas as pd
import numpy as np



#df = execute.read_database('database.xlsx', 0)
a = [1999,	1	,1	,80,	3,	1]
# obj = 'case' + str(7)
# #a.insert(0, obj)
# print(a)
# print(type(a))
# df = pd.read_excel('database.xlsx', 0)
# print(df)
case = {'name':'test', 'U value': 1, 'comlexity':'very low', 'insulation capacity':'very low', 'possibility for condenstation':'very low'}
case = {'name':'test', 'U value': 1, 'comlexity':'very low', 'insulation capacity':'very low', 'possibility for condenstation':'very low', 'construction time': 'very low', 'fuzzy evalution': 'very low', 'pattern': 'ventilation'}
line = []
importance = {'comlexity': 1, 'insulation capacity': 0, 'possibility for condenstation': 3, 'construction time': 4,  'pattern': 3}
execute.execute_programme(case, importance)
serial = []
df_db = pd.read_excel('database_v1.xlsx', index_col=0)



