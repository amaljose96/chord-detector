from sklearn.gaussian_process import GaussianProcessClassifier
import numpy as np
import sys
import dill
import os



def label_to_chord(label):
    label=int(label)
    keys=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    variations=["maj","min","maj7","sus4"]
    keyIndex=label/10;
    variationIndex=label%10;
    chord=keys[keyIndex]+variations[variationIndex];
    return chord







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
header=inputdata[0]
hop_s=int(header.rstrip("\n").split("\t")[0])
frames_limit=int(header.rstrip("\n").split("\t")[1])
sample_rate=int(header.rstrip("\n").split("\t")[2])
inputdata=inputdata[1:]

for line in inputdata:
    data_point=np.asarray(line.rstrip("\n").split("\t")[:-1]).astype(np.float32)
    data.append(data_point)
data=np.asarray(data)
print("Loaded data "+str(data.shape))




x_data=data

try:
    classifier=dill.load(open("chord_classifier.dill",'r'))
except:
    print("Error : Classifier missing");
    exit();
print("Fit")
predicted_chords=classifier.predict(x_data)

for label in predicted_chords:
    chord = label_to_chord(label)
    print(chord)





