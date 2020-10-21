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

df_columns = ["4D_num", "num_cat", "num_range", "num_sum", "num_score"]

for each_num in all_num:
    num_str = each_num
    num_cat = na.check_num_cat(each_num)
    num_range = na.check_num_range(each_num)
    num_sum = na.check_num_sum(each_num)

    norm_sum = na.calc_norm_num_sum(num_sum)
    norm_cat = na.calc_norm_num_cat(num_cat)
    num_score = round((norm_sum + norm_cat), 6)


    each_num_list = [num_str, num_cat, num_range, num_sum, num_score]
    all_num_pd_list.append(each_num_list)

df = pd.DataFrame(all_num_pd_list, columns=df_columns)
    #df containing all num
    # 4D_num : num_cat : num_range : num_sum

df_num_score = df[["4D_num", "num_score"]]
#duplicateRowsDF = dfObj[dfObj.duplicated()]


print(df_num_score)


i24 = na.get_i24()    #num_cat = 24
i12 = na.get_i12()
i8 = na.get_i8()      #num_cat = 8
i4 = na.get_i4()      #num_cat = 4
i_double = na.get_double()  #num_cat = 22
i12_no_double = na.get_i12_no_double()  #num_cat = 12
"""

#TESTING GROUND

for each in all_num_pd_list:
    print(each)

total_num_sum = 0

counter = 0

for each in num_sum_list:
    total_num_sum += len(each)
    len_str = str(len(each))
    len_percentage_str = str(len(each)/100)
    counter_str = str(counter)

    print(counter_str +" : " + len_str + "(" + len_percentage_str + ")")
    counter += 1
print(total_num_sum)
"""