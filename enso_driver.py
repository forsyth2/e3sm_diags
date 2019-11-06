import os

from acme_diags.parameter.core_parameter import CoreParameter

from acme_diags.parameter.enso_diags_parameter import EnsoDiagsParameter

 

from acme_diags.run import runner

 

param = CoreParameter()

 

#For compy

#machine_path_prefix = '/compyfs/e3sm_diags_data/'

#For cori

machine_path_prefix = '/global/project/projectdirs/acme/acme_diags'

 

param.reference_data_path = os.path.join(machine_path_prefix, 'obs_for_e3sm_diags/time-series/')

#param.test_data_path = os.path.join(machine_path_prefix, '/Users/zhang40/Documents/ACME_simulations/E3SM_v1/')
param.test_data_path = os.path.join(machine_path_prefix, '/global/project/projectdirs/acme/acme_diags/test_model_data_for_acme_diags/time-series/E3SM_v1')

param.test_name = 'e3sm_v1'

#param.output_format = ['png', 'pdf', 'svg']

 

#prefix = '/compyfs/www/zhan429/examples/'

#prefix = '/Users/zhang40/Downloads/e3sm_diags_tests'
prefix = '/global/homes/f/forsyth/e3sm_diags'
 

param.results_dir = os.path.join(prefix, 'enso_diags')

#param.multiprocessing = True

#param.num_workers =  40

 

# We're passing in this new object as well, in

# addtion to the CoreParameter object.

 

ts_param = EnsoDiagsParameter()

#ts_param.ref_names = ['none']   #This setting plot model data only

#ts_param.output_format = ['png', 'pdf', 'svg']

ts_param.test_name = 'e3sm_v1'

ts_param.start_yr = '2000'

ts_param.end_yr = '2004'

 

runner.sets_to_run = ['enso_diags']

runner.run_diags([param, ts_param])
