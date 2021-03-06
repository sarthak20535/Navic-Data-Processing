# -*- coding: utf-8 -*-
"""IRNSS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19mniLXZ1C8qTiaX1X9ebEC_LRbmsZ6bS
"""

from google.colab import drive
drive.mount('/content/drive/')


import csv
cont=0

def save_data(data):
  print(data)
  data = [data]
  file_name = "/content/drive/My Drive/IRNSS.csv"
  with open(file_name, 'a') as csvfile:
      csvwriter = csv.writer(csvfile) 
      for i in range(len(data)):
        csvwriter.writerow(data[i])


with open("/content/drive/My Drive/ACRD00IND_R_20192600425_02H_IN.rnx", "r") as file: 
    data = file.readlines() 
    for line in data: 
      
        data = []

        word = line.split()

        if cont ==1:
          if word[0][0]=='I':
            save_data([word[0]])
            print(word[0])
            if (len(word[6]))>2:
              times=(len(word[6])-2)//19
              remove=word[6][2:len(word[6])]
              
              word[6]=word[6][:2]

              for j in range(times):
                  data.append(remove[(19*j):(19*(j+1))])
              for j in range(3-times):
                  data.append(word[7+j])

            else:
              for i in range(7,len(word)):
                if len(word[i]) == 18:
                  data.append(word[i])
                
                else:
                  times=(len(word[i])-18)//19
                  data.append(word[i][:18])
                  for j in range(times):
                    data.append(word[i][(18+(19*j)):(18+(19*(j+1)))])  
          else:
            for i in range(len(word)):
              if len(word[i]) == 18:
                data.append(word[i])
              else:
                times=(len(word[i])-18)//19
                data.append(word[i][:18])
                
                for j in range(times):
                  data.append(word[i][(18+(19*j)):(18+(19*(j+1)))])
          save_data(data)
        if 'HEADER' in word:
          cont =1

j