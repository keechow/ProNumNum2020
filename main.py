import numpy as np
import pandas as pd
import xlrd

"""
Converting result xlsx into dataframe 
"""
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

print(len(df_dmc))
print(len(df_mag))
print(len(df_toto))
