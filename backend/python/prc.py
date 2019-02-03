#!/usr/bin/python3

import tensorflow as tf
from tensorflow import keras
import pandas as pd
import os
import csv
from tabula import convert_into
convert_into("./file1.pdf","z3.csv",output_format='csv')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
column_names = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
#test_results =  pd.read_csv('test3.csv',na_values = '?',skipinitialspace=True)
x3 = pd.read_csv('./z3.csv').T.to_csv('./x3.csv',header = False)
with open('./x3.csv',"rt", encoding='ascii') as f:
    reader = csv.reader(f)
    your_list = list(reader)
print(your_list[1])
int_list = []
for i in your_list[1]:
    int_list.append(int(i))
print(int_list)
mean_stats=[54.36637,0.683168,0.966997,131.623762,246.264026,0.148515,0.528053,149.646865,0.326733,1.039604,1.3999340,0.729373,2.313531]
std_stats=[9.082101,0.466012,1.032052,17.53183,51.830751,0.356198,0.525860,22.905161,22.905161,0.469794,1.161075,0.616226,1.022606,0.61227]
normalized_test = []
flag=0
for i in range(13):
    normalized_test.append((int_list[i] - mean_stats[i])/std_stats[i])
    print(i)
print(normalized_test)

new_model = tf.keras.models.load_model('./heart.h5')
with open('./x.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(column_names)
     wr.writerow(normalized_test)

df =  pd.read_csv('./x.csv',na_values = '?',skipinitialspace=True)
print(df)
predict = new_model.predict(df).flatten()
print(predict)

if(predict<0.5):
    print("Not Sick")
    with open("result.txt","w") as test_file:
        test_file.write("The person does not have heart Disease\n")
        test_file.write("The probablity of disease is : {}".format(predict*100,2))
        test_file.close()
else:
    print("Sick")
    with open("result.txt","w") as test_file:
        test_file.write("The person has coronary artery heart Disease\n")
        test_file.write("The probablity of disease is : {}".format(predict*100))
        test_file.close()
