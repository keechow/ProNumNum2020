import numpy as np
import pandas as pd
import xlrd

"""
Converting result xlsx into dataframe 

#df = pd.read_excel('Book1.xlsx',sheetname='Sheet1',header=0,converters={'names':str,'ages':str})
#need to use coverters to specify data in xlsx is read as string
#this is to avoid data being converted to int or float (0123 -> 123)

str_dict = {"year":str, "month":str, "date":str, "day":str,
            "p1":str, "p2":str, "p3":str,
            "s1":str, "s2":str, "s3":str, "s4":str, "s5":str, "s6":str, "s7":str, "s8":str, "s9":str, "s10":str,
            "c1":str, "c2":str, "c3":str, "c4":str, "c5":str, "c6":str, "c7":str, "c8":str, "c9":str, "c10":str}

df_dmc = pd.read_excel("DMC30Aug.xlsx", sheet_name="1", converters=str_dict)
df_mag = pd.read_excel("MAG30Aug.xlsx", sheet_name="1", converters=str_dict)
df_toto = pd.read_excel("TOTO30Aug.xlsx", sheet_name="1", converters=str_dict)
"""

str_dict = {"ymd":str, "day":str,
            "p1":str, "p2":str, "p3":str,
            "s1":str, "s2":str, "s3":str, "s4":str, "s5":str, "s6":str, "s7":str, "s8":str, "s9":str, "s10":str,
            "c1":str, "c2":str, "c3":str, "c4":str, "c5":str, "c6":str, "c7":str, "c8":str, "c9":str, "c10":str}

df_dmc = pd.read_excel("DMC30Aug_ymd.xlsx", sheet_name="1", converters=str_dict)
df_mag = pd.read_excel("MAG30Aug_ymd.xlsx", sheet_name="1", converters=str_dict)
df_toto = pd.read_excel("TOTO30Aug_ymd.xlsx", sheet_name="1", converters=str_dict)

print(df_dmc.head())

print(df_dmc.describe())

#column = ["year", "month", "date", "day",
# "p1", "p2", "p3", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10",
# "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]

#44j