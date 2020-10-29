import numpy as np
import pandas as pd
import xlrd

import num_analysis as na

"""
          day    p1    p2    p3    s1    s2  ...    c5    c6    c7    c8    c9   c10
ymd                                          ...                                    
20200801  sat  6211  3339  3678  3695  9642  ...  2796  8210  6529  1070  2918  9750
20200802  sun  7667  7847  3133  7524  5845  ..

#return a.  0738  1684  2304  0118  7063  4324
20200805  wed  2956  0924  2741  8325  0601  ...  6395  1673  2739  2485  3980  9809
"""

str_dict = {"ymd":str, "day":str,
            "p1":str, "p2":str, "p3":str,
            "s1":str, "s2":str, "s3":str, "s4":str, "s5":str, "s6":str, "s7":str, "s8":str, "s9":str, "s10":str,
            "c1":str, "c2":str, "c3":str, "c4":str, "c5":str, "c6":str, "c7":str, "c8":str, "c9":str, "c10":str}

df = pd.read_excel("DMC_test.xlsx", sheet_name="1", converters=str_dict, index_col="ymd")
# index_col = "ymd" changes the indexing number from 0,1,2,... to ymd number

# use loc[index] to get a particular row
# eg. draw_result_20200801 = df.loc[20200801]

#use df_new = df[["col_1", "col_3", "col_9"]] to create a new df with columns that we want only
# eg: df_p123 = df[["day", "p1", "p2", "p3"]]

"""
use iterrows to loop rows
for key, data in df.iterrows():
    print(key, data)
    print()
"""
# print(df.describe()) can give some stats on the df that may be useful

#1. convert df column to list
#2. loop through each element in list and put the element into num analysis
#3. append result into a news list
#4. add the list as a new column into the df

p1_list = list(df["p1"])
p1_num_sum_ls = []
p1_num_range_ls = []
p1_num_cat_ls = []
p1_norm_num_sum = []
p1_norm_num_cat = []
p1_norm_total = []
for each in p1_list:
    n_sum = na.check_num_sum(each)
    n_range = na.check_num_range(each)
    n_cat = na.check_num_cat(each)
    norm_num_sum = round(na.calc_norm_num_sum(n_sum),6)
    norm_num_cat = round(na.calc_norm_num_cat(n_cat),6)

    p1_num_sum_ls.append(n_sum)
    p1_num_range_ls.append(n_range)
    p1_num_cat_ls.append(n_cat)
    p1_norm_num_sum.append(norm_num_sum)
    p1_norm_num_cat.append(norm_num_cat)
    p1_norm_total.append(round(norm_num_sum+norm_num_cat,6))
df_key = ["4D_Num","num-cat","num-range","num-sum","norm-score-cat", "norm-score-sum","norm-score-total"]
p1_dict_data = {df_key[0]: p1_list, df_key[1]:p1_num_cat_ls, df_key[2]:p1_num_range_ls, df_key[3]:p1_num_sum_ls, df_key[4]:p1_norm_num_cat, df_key[5]:p1_norm_num_sum, df_key[6]:p1_norm_total}

p1_df = pd.DataFrame(p1_dict_data)
"""
print(p1_df)

print(p1_df.to_string())

"""

for each in range(37):
    print(str(each) + " : " + str(na.calc_norm_num_sum(each)))