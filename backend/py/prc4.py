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
'''
test_results.tail()
test_results.isna().sum()
test_results = test_results.dropna()
test_set = test_results.drop(test_results.index)
test_set.pop("target")'''
int_list = []
for i in your_list[1]:
    int_list.append(int(i))

print(int_list)



mean_stats=[42.36637,0.783168,1.966997,141.623762,236.264026,0.548515,0.128053,149.846865,1.326733,1.079604,1.6999340,1.729373,3.313531]

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


if(predict<0.5):
    with open("result.txt","a") as test_file:
        test_file.write("The person does not have Arrhythmia\n")
        test_file.write("The probablity of disease is : {}".format(predict[0]*100))
        test_file.close()
else:
    with open("result.txt","a") as test_file:
        test_file.write("{ has:'The person has Arrhythmia',\n")
        test_file.write("procedure:'The procedure required to recover from it is Cardioversion and Radiofrequency ablation',\n")
        test_file.write("cost:'The average cost of procedure to operate on Coronary Heart disease is R75,000',\n")
        test_file.write("med:'The medicines required will be Antiarrhythmic, Calcium channel blocker, Beta blocker, and Dietary supplement',\n")
        #test_file.write("Statin : Decreases the liver's production of harmful cholesterol.\nBlood Thinners : Helps prevent blood clots from forming or helps dissolve existing clots.\nBeta blocker : Slows heart rate and decreases blood pressure. When taken in eye-drop form, it reduces eye pressure.\nHeart Medication : Helps reduce chest pain or pressure caused by blockages in the arteries of the heart.\nCalcium channel blocker : Relaxes blood vessels.")
        test_file.write("prob: "+str(predict[0]*100)+" } \n")
        test_file.close()

