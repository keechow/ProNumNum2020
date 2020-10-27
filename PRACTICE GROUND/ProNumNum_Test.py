import numpy as np
import pandas as pd
import xlrd
"""
          day    p1    p2    p3    s1    s2  ...    c5    c6    c7    c8    c9   c10
ymd                                          ...                                    
20200801  sat  6211  3339  3678  3695  9642  ...  2796  8210  6529  1070  2918  9750
20200802  sun  7667  7847  3133  7524  5845  ...  0738  1684  2304  0118  7063  4324
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

for key, data in df.iterrows():
    print(key, data)
    print()