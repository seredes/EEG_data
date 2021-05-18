Test repository for EEG project.

Data originally from: https://archive.ics.uci.edu/ml/datasets/eeg+database

Experiment description:

There were two groups of subjects: alcoholic and control. 

Each subject was exposed to either a single stimulus (S1) or to two stimuli (S1 and S2) which were pictures of objects chosen from the 1980 Snodgrass and Vanderwart picture set. When two stimuli were shown, they were presented in either a matched condition where S1 was identical to S2 or in a non-matched condition where S1 differed from S2. 

There were 122 subjects and each subject completed 120 trials where different stimuli were shown. The electrode positions were located at standard sites


Data download: https://archive.ics.uci.edu/ml/machine-learning-databases/eeg-mld/

There are three versions of the EEG data set. 

1. The Small Data Set 
The small data set (**smni97_eeg_data.tar.gz**) contains data for the 2 subjects, alcoholic a_co2a0000364 and control c_co2c0000337. For each of the 3 matching paradigms, c_1 (one presentation only), c_m (match to previous presentation) and c_n (no-match to previous presentation), 10 runs are shown. 

2. The Large Data Set 
The large data set (**SMNI_CMI_TRAIN.tar.gz** and **SMNI_CMI_TEST.tar.gz**) contains data for 10 alcoholic and 10 control subjects, _with 10 runs (=trials) per subject per paradigm_. Since there are three paradigms (one stimulus, two matched stimuli, two non-matched stimuli) there are 30 runs for each subjects.

The test data used the same 10 alcoholic and 10 control subjects as with the training data, but with 10 out-of-sample runs per subject per paradigm. 

3. The Full Data Set 
This data set contains all 120 trials for **122 subjects**. The entire set of data is about 700 MBytes. 

NOTE: I was checking the full dataset from the UCI website, which I assume is eeg_full.tar. While there are 122 participants in the full dataset, as stated in the description, it looks like that the number of trials recorded per participant is not the same for each participant. For example participant 365 has 93 trials on record, while participant 364 has 88 trials on record. 

NOTE: There are 17 trials with empty files in co2c1000367. Some trials have "err" notices, e.g., search/grep for "err" and see "S2 match err" or "S2 nomatch err" etc. 


