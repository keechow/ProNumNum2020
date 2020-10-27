import numpy as np
import pandas as pd
import xlrd

str_dict = {"ymd":str, "day":str,
            "p1":str, "p2":str, "p3":str,
            "s1":str, "s2":str, "s3":str, "s4":str, "s5":str, "s6":str, "s7":str, "s8":str, "s9":str, "s10":str,
            "c1":str, "c2":str, "c3":str, "c4":str, "c5":str, "c6":str, "c7":str, "c8":str, "c9":str, "c10":str}

df = pd.read_excel("DMC_test.xlsx", sheet_name="1", converters=str_dict)
print(df.head())