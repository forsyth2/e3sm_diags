import numpy
from .core_parameter import CoreParameter


class MeridionalMean2dParameter(CoreParameter):
    def __init__(self):
        super(MeridionalMean2dParameter, self).__init__()
        self.plevs = numpy.logspace(2.0, 3.0, num=17)
        # Granulating plevs causes duplicate plots in this case.
        # So keep all of the default values except plevs. 
        self.granulate.remove('plevs')
