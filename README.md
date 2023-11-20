# Training_notebooks
A repository to store code for training purposes

Jupyter notebooks that can be run on JASMN in the JasPy environment.

***Instructions to set up for use on JASMIN***


***Instructions to set up for use elsewhere***

Step 1 navigate to the directory that you wish to store the notebook into and clone the github repository:
`git clone https://github.com/MetOffice/Python_training_notebooks.git`

Step 2 is to ensure that you have downloaded the miniconda installer:
`$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`

Step 3 is to create a base environment:
`$ bash Miniconda3-latest-Linux-x86_64.sh`

Step 4 is to activate the base environment:
`$ source ~/miniconda3/bin/activate`

Step 5 is to create a conda enviroment using the command:
`$ conda create -n testenv iris iris-sample-data jupyter nc-time-axis pandas scipy seaborn scikit-learn statsmodels`

Step 6 is to activate the conda environment using the command:
`$ conda activate testenv`

Step 7 is to add three further libraries to the environment:
`conda install -c conda-forge iris-sample-data iris nc-time-axis`

Step 8 to is to run the course notebooks by navigating to the CLARE-PALM-TREEs/Training_notebooks directory you made and using the command:
`$ jupyter notebook`

***Instructions to reopen the notebooks for use elsewhere***
Once you have created the testenv conda environment, to return to using the notebooks just follow these steps.

Step 1 is to activate the conda environment using the command:
`$ conda activate testenv`

Step 2 is to run the course notebooks by navigating to the CLARE-PALM-TREEs/Training_notebooks directory you made and using the command:
`$ jupyter notebook`
