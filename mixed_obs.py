# -*- coding: utf-8 -*-
"""Mixed_Obs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15GnKOEThHHZ0EMLrsCEqwLmvGyTY5-uq
"""

from google.colab import drive
drive.mount('/content/drive/')

# Python code to illustrate split() function 

import csv

def save_data(data,q):
  print(data)
  if q=='i':
    file_name = "/content/drive/My Drive/i.csv"
  else:
    file_name = "/content/drive/My Drive/g.csv"
  with open(file_name, 'a') as csvfile:
      # creating a csv writer object 
      csvwriter = csv.writer(csvfile) 
        
      # writing the fields 
      for i in range(len(data)):
        csvwriter.writerow(data[i])
cont=0
g =0
i =0   
g_data = []
i_data =[]
with open("/content/drive/My Drive/ACRD00IND_R_20192600425_02H_01S_MO.rnx", "r") as file: 
    data = file.readlines() 
    for line in data: 
        word = line.split()
        if cont ==1 and '>' not in word:
          if word[0][0] == 'G': # G 7
            rem = 0
            for k in range(len(word)):
              if len(word[k])==1:
                rem +=1
            for k in range(len(word)-rem):
              if len(word[k])==1:  
                word.remove(word[k])
            g += 1 
            g_data.append(word)
                       
          elif word[0][0] == 'I': # I 8
            rem =0
            for k in range(len(word)):
              if len(word[k])==1:
                rem +=1
            for k in range(len(word)-rem):
              if len(word[k])==1:  
                word.remove(word[k])
            i += 1
            i_data.append(word)
            
        if cont ==1 and '>' in word: # for saving time
          print (word[6])
          save_data([[float(word[6])]],'i')
          save_data([[float(word[6])]],'g')
        if 'HEADER' in word:
          cont =1
        if i==8:
          save_data(i_data,'i')
          print(i_data)
          i_data =[]
          i=0
        elif g==7: 
          save_data(g_data,'g')
          g_data = []
          g =0

