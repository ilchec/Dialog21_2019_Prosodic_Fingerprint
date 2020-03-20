# Prosodic Fingerprints
The project consists of the following files:

- pitch_to_unigrams.py — a Python 3 script that converts raw pitch data to unigrams.
- Dialog_code.Rmd — an R Notebook with data wrangling, plots and models.
- Pitch — the folder with the raw pitch data.
- Unigrams.csv — the output of *pitch_to_unigrams.py*, contains all data points with unigram annotation.
- Unigrams_counted.csv — the output of *pitch_to_unigrams.py*, contains counts of unigrams per speaker, the file is not used anymore.

### The Python 3 Script
To run the *pitch_to_unigrams.py*, simply place it in the same folder with the Pitch folder (NB! not *inside* the pitch filder). The script uses **Python 3**. It also uses the following default Python packages: **math**, **future**, **sys**, **os**, **operator**, **statistics**, **re**. Make sure the packages are installed before you run the script. Since running the script takes approximately 10 minutes on a relatively powerful machine, I also provide the output of the script in *Unigrams.csv* and *Unigrams_counted.csv*.

### The R Notebook
To run the R Notebook, the **R Software** and **RStudio** are required. The following R packages are required: **tidyverse**, **plyr**, **ggplot2**, **effects**, **lmerTest**, **Hmisc**. If the packages are not installed on your machine yet, please use the *install.packages("<package_name>")* function.

### The Data
The Pitch folder contains the raw pitch data extracted from the audio recordings. The following metadata are encoded in the filenames: *pseudonym*, *place of residence*, *age*, *type of text*, *number of sentence*. When converting the data to the unigram format, these data are automatically extracted from the filenames by the Python script.

### Differences from the Published Paper
The names of the groups in the barplots have been corrected.
