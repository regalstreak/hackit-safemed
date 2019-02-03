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
mean_stats=[54.36637,0.683168,0.966997,131.623762,246.264026,0.148515,0.528053,149.646865,0.326733,1.039604,1.3999340,0.729373,2.313531]
std_stats=[9.082101,0.466012,1.032052,17.53183,51.830751,0.356198,0.525860,22.905161,22.905161,0.469794,1.161075,0.616226,1.022606,0.61227]
'''
print(mean_stats)
print(std_stats)
'''
'''train_stats =  test_results.describe()
train_stats.pop("target")
train_stats = train_stats.transpose()

test_labels = test_results.pop('target')
print(train_stats)
'''
normalized_test = []
'''def norm(x):
    return ((x - mean_stats)/std_stats)
normalized_test = norm(test_results)'''
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
        test_file.write("{ has:'The person does not have Coronary heart Disease',\n")
        test_file.write("{ prob: "+str(predict[0]*100)+" }\n")
        test_file.close()
else:
    with open("result.txt","a") as test_file:
        test_file.write('{ has:"The person has Coronary heart Disease",\n')
        test_file.write("procedure:'The procedure required to recover from it is Coronary artery bypass surgery',\n")
        test_file.write("cost:'The average cost of procedure to operate on Coronary Heart disease is R50,000',\n")
        test_file.write("med:'The medicines required will be Statin, Blood Thinners, Beta blocker, Heart Medication, and Calcium channel blocker',\n")
        #test_file.write("Statin : Decreases the liver's production of harmful cholesterol.\nBlood Thinners : Helps prevent blood clots from forming or helps dissolve existing clots.\nBeta blocker : Slows heart rate and decreases blood pressure. When taken in eye-drop form, it reduces eye pressure.\nHeart Medication : Helps reduce chest pain or pressure caused by blockages in the arteries of the heart.\nCalcium channel blocker : Relaxes blood vessels.")
        test_file.write("prob: "+str(predict[0]*100)+" } \n")
        test_file.close()
