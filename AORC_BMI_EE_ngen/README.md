# Testing BMI Python modules in ngen framework.
 - AORC_model.py: This file is the "model" it takes inputs and gives an output
 - AORC_bmi_model.py: This is the Basic Model Interface that talks with the model. This is what we are testing.
 - run_ngen_aorc_bmi.py: This is the driver that run the model in the ngen framework. It is assumed a file exists in the data/forcing/ directory with the name catchment-id.csv with a time column.
 - AORC_run_bmi_unit_test.py: This is a file that runs each BMI unit test to make sure that the BMI is complete and functioning as expected.
 - config.yml: This is a configuration file that the BMI reads to set inital_time (initial value of current_model_time) and time_step_seconds (time_step_size, catchment-id).
 - environment.yml: Environment file with the required Python libraries needed to run the model with BMI. Create the environment with this command: `conda env create -f environment.yml`, then activate it with `conda activate bmi_test`

# About
This is an implementation of a Python-based model that fulfills the Python language BMI interface and can be used in the Framework. The forcing data are provided in real time as ngen runs the time steps.

# Implementation Details

## Test the complete BMI functionality
`python AORC_run_bmi_unit_test.py`

## Run the model
`python run_ngen_aorc_bmi.py`

## Outputs
Outputs are in files the same as in ngen framework.
