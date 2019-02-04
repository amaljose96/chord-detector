from sklearn.gaussian_process import GaussianProcessClassifier
import numpy as np
import sys
import dill
import os
if(len(sys.argv)<2):
    print("Filename not given.")
    exit();
data_name=sys.argv[1]
inputfile=open(data_name,"r")
inputdata=[]
data=[]
print("Loading data..")

for line in inputfile:
    inputdata.append(line)

for line in inputdata:
    data_point=np.asarray(line.rstrip("\n").split("\t")[:-1]).astype(np.float32)
    data.append(data_point)
data=np.asarray(data)
print("Loaded data "+str(data.shape))
data=np.transpose(data);
labels=data[-1]
data=data[0:-1]
data=np.transpose(data)
print(labels)
x_data=data
y_data=labels

print("Data Ready")

classifier=GaussianProcessClassifier()
print("Fitting")
classifier.fit(x_data,y_data)
print("Fit")
y_predict=classifier.predict(x_data)
print(classifier.predict(x_data))
