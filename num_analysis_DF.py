"""
Name: num_analysis_DF.py
Objective: Create a pandas DF that contains num_range, num_cat and num_sum for each 4D num
example:

---------------------------------------
Num  |  num_range | num_cat | num_sum |
-----|------------|---------|---------|
0000 | 0          | 4       | 0       |
1234 | 1          | 24      | 10      |
2233 | 2          | 22      | 10      |



"""

import pandas as pd
import num_analysis as na

# na.check_num_sum()
# na.check_num_cat()
# na.check_num_range()



all_num = na.gen_num()
all_num_pd_list = [] #list containing data for constructind pd df
#[['1212', 22, 1, 6], ['1213', 12, 1, 7],...]
df_columns = ["4D_num", "num_cat", "num_range", "num_sum"]
for each_num in all_num:
    num_str = each_num
    num_cat = na.check_num_cat(each_num)
    num_range = na.check_num_range(each_num)
    num_sum = na.check_num_sum(each_num)

    each_num_list = [num_str, num_cat, num_range, num_sum]
    all_num_pd_list.append(each_num_list)

# creating df
# data = [['Alex',10],['Bob',12],['Clarke',13]]
# df = pd.DataFrame(data,columns=['Name','Age'])

df = pd.DataFrame(all_num_pd_list, columns=df_columns)

print(df.head())
print(len(df))
i24 = na.get_i24()    #num_cat = 24
i12 = na.get_i12()
i8 = na.get_i8()      #num_cat = 8
i4 = na.get_i4()      #num_cat = 4
i_double = na.get_double()  #num_cat = 22
i12_no_double = na.get_i12_no_double()  #num_cat = 12

num_sum_list = []    # list to store all num in accordance to their num_sum
for each in range(37):  #num_sum is indicated using element's index in num_sum_list
    num_sum_list.append([])

for each in all_num:
    idx = na.check_num_sum(each)
    num_sum_list[idx].append(each)


"""
TESTING GROUND

for each in all_num_pd_list[1212:1299]:
    print(each)


counter = 0
for each in num_sum_list:
    len_str = str(len(each))
    counter_str = str(counter)
    print(counter_str +" : " + len_str)
    counter += 1
"""