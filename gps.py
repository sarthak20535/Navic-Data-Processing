# -*- coding: utf-8 -*-
"""GPS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ipclXbyjuVxhNU1XzFkKj14uh9-fc7se
"""

from google.colab import drive
drive.mount('/content/drive/')


!pip install georinex
import georinex as gr
import numpy as np
print("hello")
file_name="/content/drive/My Drive/ACRD00IND_R_20192600425_02H_GN.rnx"
data=gr.load(file_name)
print(data)

ds=data.to_array
print(ds)

ds=data.to_dataframe()
ds['Crs'].replace('', np.nan, inplace=True)

ds.dropna(subset=['Crs'], inplace=True)
print(ds)
ds.to_csv(r"/content/drive/My Drive/GPS.csv",index=True)

