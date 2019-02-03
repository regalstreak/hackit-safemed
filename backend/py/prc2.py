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
with open('x3.csv',"rt", encoding='ascii') as f:
    reader = csv.reader(f)
    your_list = list(reader)
print(your_list[1])

int_list = []
for i in your_list[1]:
    int_list.append(int(i))

print(int_list)

mean_stats=[54.12,0.68590,0.966,144.623762,243.26456,0.348515,0.128053,153.646865,0.426733,1.79604,1.5999340,0.629373,2.713531]
std_stats=[9.82101,0.476012,1.072052,17.73183,49.830751,0.366198,0.95860,21.905161,22.905161,0.569794,1.191075,0.636226,1.322606,0.67227]

normalized_test = []

flag=0
for i in range(13):
    normalized_test.append((int_list[i] - mean_stats[i])/std_stats[i])
    print(i)
print(normalized_test)

new_model = tf.keras.models.load_model('heart.h5')
with open('x.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(column_names)
     wr.writerow(normalized_test)

df =  pd.read_csv('x.csv',na_values = '?',skipinitialspace=True)
print(df)
predict = new_model.predict(df).flatten()
print(predict)

if(predict<0.7):
    with open("result.txt","a") as test_file:
        test_file.write("The person does not have heart Disease\n")
        test_file.write("The probablity of disease is : {}".format(predict[0]*100))
        test_file.close()
else:
    with open("result.txt","a") as test_file:
        test_file.write("{ has:'The person has Heart Attack',\n")
        test_file.write("procedure:'The procedure required to recover from it is Coronary catheterization',\n")
        test_file.write("cost:'The average cost of procedure to operate on Coronary Heart disease is R1,00,000',\n")
        test_file.write("med:'The medicines required will be Blood pressure support, Involuntary nervous system blocker, and Antiarrhythmic',\n")
        #test_file.write("Statin : Decreases the liver's production of harmful cholesterol.\nBlood Thinners : Helps prevent blood clots from forming or helps dissolve existing clots.\nBeta blocker : Slows heart rate and decreases blood pressure. When taken in eye-drop form, it reduces eye pressure.\nHeart Medication : Helps reduce chest pain or pressure caused by blockages in the arteries of the heart.\nCalcium channel blocker : Relaxes blood vessels.")
        test_file.write("prob: "+str(predict[0]*100)+" } \n")
        test_file.close()
