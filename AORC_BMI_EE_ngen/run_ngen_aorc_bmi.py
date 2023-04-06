from pathlib import Path
import numpy as np
import os

# This is the BMI LSTM that we will be running
from AORC_bmi_model import AORC_bmi_model

def execute():
    # creating an instance of a model
    print('creating an instance of the  AORC_BMI_MODEL model object')
    model = AORC_bmi_model()

    # Initializing the BMI
    print('Initializing the AORC Forcings BMI')
    current_dir = Path(__file__).parent.resolve()
    model.initialize(bmi_cfg_file_name=str(current_dir.joinpath('config.yml')))

    # Now loop through the time steps, update the AORC Forcings model, and set output values
    print('Now loop through the time steps, run the AORC forcings model (update), and set output values')
    print('\n')
    print('model time', 'ids', 'RAINRATE', 'T2D', 'Q2D', 'U2D', 'V2D', 'PSFC', 'SWDOWN', 'LWDOWN')

    print("Input variables:")
    print(model.get_input_var_names())
    print("Output variables:")
    print(model.get_output_var_names())

    # Run a short test of the AORC_bmi_model module in standalone mode
    for x in range(5):

        #########################################
        # UPDATE THE MODEL WITH THE NEW INPUTS ##
        model.update()     ######################
        #########################################

        print(model.get_current_time(),model.get_value_ptr('ids'),model.get_value_ptr('APCP_surface'),model.get_value_ptr('TMP_2maboveground'),model.get_value_ptr('SPFH_2maboveground'),model.get_value_ptr('UGRD_10maboveground'),model.get_value_ptr('VGRD_10maboveground'),model.get_value_ptr('PRES_surface'),model.get_value_ptr('DSWRF_surface'),model.get_value_ptr('DLWRF_surface'))

    # Run `ngen` with the AORC_bmi_model providing forcing in the Model Engine Framework:
    print("begin to run ngen")
    cmd = '../cmake_serial_py/ngen ./catchment_data.geojson \"cat-304922\" ./nexus_data.geojson \"nex-299158\" bmi_multi_realization_config_w_py.json'
    os.system(cmd)

    # Finalizing the BMI
    print('Finalizing the AORC Forcings BMI')
    model.finalize()


if __name__ == '__main__':
    execute()
