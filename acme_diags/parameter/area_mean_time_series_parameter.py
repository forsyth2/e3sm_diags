from .core_parameter import CoreParameter


class AreaMeanTimeSeriesParameter(CoreParameter):
    def __init__(self):
        super(AreaMeanTimeSeriesParameter, self).__init__()
        # A list of the reference names to run the diags on.
        self.ref_names = []
        # Granulating with regions doesn't make sense,
        # because we have multiple regions for each plot.
        # So keep all of the default values except regions. 
        self.granulate.remove('regions')

    def check_values(self):
        if not self.ref_names:
            msg = 'You must have a value for ref_names.'
            raise RuntimeError(msg)
