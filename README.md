# Chord Detection using ML

This project is aimed at detecting chords from a music file using machine learning.
The unlabelled dataset for a song can be generated using [song to beat data](https://github.com/amaljose96/song_to_beat_data) module.
This is taken as an input to data_labeller.py which reads the dataset and lets us manually label the beat data.
This labelled data is then sent to the classifier which learns this data and can be used to predict chords of other songs.

## Classifier Learner

This file reads the dataset which is the output of the data_labeller and teaches to the classifier model. It uses the existing chord_classifier.dill or creates a new one. The classifier used is GaussianProcessClassifier from sklearn. The learnt classifier is then saved into a file using dill.

### Prerequisites

This file requires sklearn and dill.

> pip install sklearn dill

### How to run

> python chord_classifier_learner.py \<name of song\>\_labelled.txt

**Note :* To expand the dataset for the classifier with just one song, the song can be transposed externally, then run through the song_to_beat_data module and data_labeller and then train the classifier.

## Detector

 To be done.
