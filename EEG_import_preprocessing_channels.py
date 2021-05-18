# Predict Who is Alcoholic

import gzip
import seaborn as sn
import matplotlib.pyplot as plt
from pyprojroot import here
from EEG_load_function import import_eeg_file

# Import data from one trial from participant 338 in control group
fc = gzip.open(here('./SMNI_CMI_TRAIN/co2c0000338/co2c0000338.rd.000.gz'), 'rb')
# Import data from one trial from one participant 364 in alcoholic group
fa = gzip.open(here('./SMNI_CMI_TRAIN/co2a0000364/co2a0000364.rd.000.gz'), 'rb')
dfc = import_eeg_file(fc)
dfa = import_eeg_file(fa)

# correlation matrix for partcipant
corrMatrix_c = dfc.corr()
ax = plt.axes()
sn.heatmap(corrMatrix_c,
           cbar=False,
           square=True,
           xticklabels=False,
           yticklabels=False,
           ax = ax
           )
ax.set_title('Correlation Matrix - Participant in Control Group')
ax.set_xlabel('Electrodes') # x-axis label with fontsize 15
ax.set_ylabel('Electrodes') # y-axis label with fontsize 15

plt.show()

corrMatrix_a = dfa.corr()
ax = plt.axes()
sn.heatmap(corrMatrix_a,
           cbar=False,
           square=True,
           xticklabels=False,
           yticklabels=False,
           ax = ax
           )
ax.set_title('Correlation Matrix - Participant in Alcoholic Group')
ax.set_xlabel('Electrodes') # x-axis label with fontsize 15
ax.set_ylabel('Electrodes') # y-axis label with fontsize 15
plt.show()