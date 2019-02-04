import numpy as np
from pysoundcard import Stream
import os
import sys


"""
CLASS LABELS OF THE DATASET

Cmaj        ->  C Major
Cmin        ->  C Minor
Cmaj7       ->  C Major 7th
Csus4       ->  C sus 4
C#maj        ->  C# Major
C#min        ->  C# Minor
C#maj7       ->  C# Major 7th
C#sus4       ->  C# sus 4


etc.


For labelling purposes, every major or minor chord has a set of 10 chords each.
ie. We have 12 keys (C,C#,D,D#,E,F,F#,G,G#,A,A#,B).
Each scale can have 10 variations each. So we have 120 class labels.

"""

keys=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"];
variations=["maj","min","maj7","sus4"]

def getClassLabel(chord):
    #First detect the key.
    key=''
    variation=''
    if(str.find(chord,"#")==1):
        key=chord.split("#")[0]+"#";
        variation=chord.split("#")[1];
    elif(str.find(chord,"b")==1):
        key=chord.split("b")[0]+"b";
        variation=chord.split("b")[1];
    else:
        key=str(chord[0]);
        variation=chord[1:]
    #Cleaning the chord
    if(str.find(key,"b")==1):
        if(key[0]=="A"):
            key="G#"
        else:
            key=chr(ord(key[0])-1)+"#"
    if(variation==""):
        variation="maj"
    if(variation=="m"):
        variation="min"
    if(variation=="7"):
        variation="maj7"
    if(variation=="m7"):
        variation="min7"
    keys=["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"];
    variations=["maj","min","maj7","sus4"]
    if(key not in keys):
        return -1;
    if(variation not in variations):
        return -1;
    return keys.index(key)*10+variations.index(variation);






hop_s=128;

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
    data_point=data_point.reshape((frames_limit,hop_s))
    data.append(data_point)
data=np.asarray(data)
print("Loaded data "+str(data.shape))



s = Stream(samplerate = sample_rate, blocksize = hop_s)
beat_no=0

#Get input from user and save to file
outputfilename="_".join(data_name.split('_')[0:-1])+"_labelled.txt";
outputfile=open(outputfilename,"w")

#Checking if Auto Mode
default_chord="";
if( getClassLabel ( (data_name.split('_'))[0] ) == 0 ):
    default_chord=(data_name.split('_'))[0]
    print("Auto mode")

output_data=[]
previous_chord="null"
num_chords=0
for beat_data in data:
    print("For beat "+str(beat_no));
    sys.stdout.write("\033[F")
    s.start();
    for samples in beat_data:
        s.write(samples)
    if(default_chord==""):
        chord=raw_input("Enter chord:"+str(keys)+" "+str(variations)+" : ")
    else:
        previous_chord=default_chord;
        chord=""
        print("Using default chord  : "+default_chord)    
    if(chord==""):
        if(previous_chord=="null"):
            print("First time. Passing.")
            sys.stdout.write("\033[F")
        else:
            if(default_chord==""):
                print("Using previos chord:"+previous_chord)
            chord=previous_chord
            write_data=list(beat_data.reshape((frames_limit*hop_s)))
            write_data.append(getClassLabel(chord))
            output_data.append(write_data)
            num_chords += 1
    elif(chord=="p"):
        print("Pass")
    elif(chord=="Quit" or chord=="q" or chord=="quit"):
        s.stop();
        break;
    elif(getClassLabel(chord)==-1):
        print("Invalid chord. Skipping.")
    else:
        previous_chord=chord;
        print("Chord="+chord);
        write_data=list(beat_data.reshape((frames_limit*hop_s)))
        write_data.append(getClassLabel(chord))
        output_data.append(write_data)
        num_chords += 1
    s.stop();
    beat_no=beat_no+1

print("Done with taking labels")
print("Writing into file")
for line in output_data:
    count=0
    for el in line:
        outputfile.write(str(el)+"\t")
        count=count+1;
    outputfile.write("\n")

print("Written into file.")
