# Chord Detection using ML

This project is aimed at detecting chords from a music file using machine learning.
The unlabelled dataset for a song can be generated using [song to beat data](https://github.com/amaljose96/song_to_beat_data) module.
This is taken as an input to data_labeller.py which reads the dataset and lets us manually label the beat data.
This labelled data is then sent to the classifier which learns this data and can be used to predict chords of other songs.

## Data labeller

This file reads the data file, plays each beat data to the user one by one and ask for the corresponding chord. The chord is then converted into classlabel and saved as \<song_name\>_labelled.txt
Chord to Class label conversion are as follows:
- The key is detected from every chord.
- Every key can have 10 chord variations (like maj, min, maj7 etc.)
- Class label is calculated as 'key_number \* 10 + variation_number' where key_number and variation_number are the indices.
- Key can be obtained by dividing the class label by 10. Variation can be obtained by mod 10.

### How to run
> python data_labellor.py \<name of song\>_data.txt
### How to label
- For every input, give key followed by variation. eg. Cmaj, D#min etc.
- If the data is not to be taken(ie. does not clearly define a chord or has a transition), press 'p' to pass.
- If the same chord is repeated (as in the current beat has the same chord as the previous), press 'Enter'.
- If you want to quit, press 'q'.

## Classifier
 
 To be done.
 
## Detector

 To be done.
