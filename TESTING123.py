import pandas as pd

c_name = ["c1","c2"]
c1_data = ["apple", "ball", "cat"]
c2_data = ["epal", "bola", "kucing"]

c3 = {c_name[0]:c1_data, c_name[1]:c2_data}

df_c = pd.DataFrame(c3)

c00 = ["fruit", "thing", "animal"]

df_c["c3"] = c00

new_ls = []
for index, data in df_c.iterrows():
    new_ls.append(data)

for each in new_ls:
    print(type(each))
    print()
    print(each)

"""
for i, j in df.iterrows(): 
    print(i, j) 
    print() 
"""