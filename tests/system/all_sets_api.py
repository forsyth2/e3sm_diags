# Running the software with the API:
#    python all_sets_api.py -d all_sets.py
from acme_diags.parameter.core_parameter import CoreParameter
from acme_diags.run import Run

thing = Run()
param = CoreParameter()
thing.run_diags([param])

