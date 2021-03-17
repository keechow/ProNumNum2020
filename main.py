import numpy as np
import pandas as pd
import xlrd
import num_analysis as na
"""
Converting result xlsx into dataframe 

#df = pd.read_excel('Book1.xlsx',sheetname='Sheet1',header=0,converters={'names':str,'ages':str})
#need to use coverters to specify data in xlsx is read as string
#this is to avoid data being converted to int or float (0123 -> 123)

#column = ["ymd", "day", "p1", "p2", "p3", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]
"""

str_dict = {"ymd":str, "day":str,
            "p1":str, "p2":str, "p3":str,
            "s1":str, "s2":str, "s3":str, "s4":str, "s5":str, "s6":str, "s7":str, "s8":str, "s9":str, "s10":str,
            "c1":str, "c2":str, "c3":str, "c4":str, "c5":str, "c6":str, "c7":str, "c8":str, "c9":str, "c10":str}

df_dmc = pd.read_excel("DMC30Aug_ymd.xlsx", sheet_name="1", converters=str_dict)
df_mag = pd.read_excel("MAG30Aug_ymd.xlsx", sheet_name="1", converters=str_dict)
df_toto = pd.read_excel("TOTO30Aug_ymd.xlsx", sheet_name="1", converters=str_dict)

#separate df according to prize category, pcat


df_pcats_dmc = df_dmc[["ymd", "day", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10"]]
df_pcats_mag = df_mag[["ymd", "day", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10"]]
df_pcats_toto = df_toto[["ymd", "day", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10"]]
#       print(df_pcats_dmc.columns)
#       >>>     Index(['ymd', 'day', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10'], dtype='object')

df_pcatc_dmc = df_dmc[["ymd", "day", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]]
df_pcatc_mag = df_mag[["ymd", "day", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]]
df_pcatc_toto = df_toto[["ymd", "day", "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]]
#       print(df_pcatc_dmc.columns)
#       >>> Index(['ymd', 'day', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10'],dtype='object')

df_pcat123_dmc = df_dmc[["ymd", "day", "p1", "p2", "p3"]]
df_pcat1_dmc = df_dmc[["ymd", "day", "p1"]]
df_pcat2_dmc = df_dmc[["ymd", "day", "p2"]]
df_pcat3_dmc = df_dmc[["ymd", "day", "p3"]]

df_pcat123_mag = df_mag[["ymd", "day", "p1", "p2", "p3"]]
df_pcat1_mag = df_mag[["ymd", "day", "p1"]]
df_pcat2_mag = df_mag[["ymd", "day", "p2"]]
df_pcat3_mag = df_mag[["ymd", "day", "p3"]]

df_pcat123_toto = df_toto[["ymd", "day", "p1", "p2", "p3"]]
df_pcat1_toto = df_toto[["ymd", "day", "p1"]]
df_pcat2_toto = df_toto[["ymd", "day", "p2"]]
df_pcat3_toto = df_toto[["ymd", "day", "p3"]]

#       print(df_pcat123_dmc.columns)
#       >>>    Index(['ymd', 'day', 'p1', 'p2', 'p3'], dtype='object')

#2020.11.03] After separating result df into different df according to respective pcat, we want to put each 4D into na module to get numcat,numrange,numsum,norm score

#convert df to list, then put list into na.get_df_4d
#use output from na.get_df_4d to build a new DF

pcat1_dmc_ls = list(df_pcat1_dmc["p1"])
#pcat2_dmc_ls = list(df_pcat2_dmc["p1"])
#pcat3_dmc_ls = list(df_pcat3_dmc["p1"])

dict_pcat1_dmc_ls = na.get_df_4d(pcat1_dmc_ls)
#df_pcat2_dmc_ls = na.get_df_4d(pcat2_dmc_ls)
#df_pcat3_dmc_ls = na.get_df_4d(pcat3_dmc_ls)

df_pcat1_dmc_na = pd.DataFrame(dict_pcat1_dmc_ls)

print(df_pcat1_dmc_na.to_string())
#2222
