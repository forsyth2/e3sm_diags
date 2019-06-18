import cdutil

regions_specs = {
    'NHEX': {'domain': cdutil.region.domain(latitude=(30., 90, 'ccb'))},
    'SHEX': {'domain': cdutil.region.domain(latitude=(-90., -30, 'ccb'))},
    'TROPICS': {'domain': cdutil.region.domain(latitude=(-30., 30, 'ccb'))},
    "global": {},
    'TRMM_region': {'domain': cdutil.region.domain(latitude=(-38., 38, 'ccb'))},
    '90S50S': {'domain': cdutil.region.domain(latitude=(-90., -50, 'ccb'))},
    '50S20S': {'domain': cdutil.region.domain(latitude=(-50., -20, 'ccb'))},
    '20S20N': {'domain': cdutil.region.domain(latitude=(-20., 20, 'ccb'))},
    '20N50N': {'domain': cdutil.region.domain(latitude=(20., 50, 'ccb'))},
    '50N90N': {'domain': cdutil.region.domain(latitude=(50., 90, 'ccb'))},
    '60S90N': {'domain': cdutil.region.domain(latitude=(-60., 90, 'ccb'))},
    'ocean': {'value': 0.65, },
    'ocean_seaice': {'value': 0.65, },
    'land': {'value': 0.65, },
    'land_60S90N': {'value': 0.65, 'domain': cdutil.region.domain(latitude=(-60., 90, 'ccb'))},
    'ocean_TROPICS': {'value': 0.65, 'domain': cdutil.region.domain(latitude=(-30., 30, 'ccb'))},
    'land_NHEX': {'value': 0.65, 'domain': cdutil.region.domain(latitude=(30., 90, 'ccb'))},
    'land_SHEX': {'value': 0.65, 'domain': cdutil.region.domain(latitude=(-90., -30, 'ccb'))},
    'land_TROPICS': {'value': 0.65, 'domain': cdutil.region.domain(latitude=(-30., 30, 'ccb'))},
    'ocean_NHEX': {'value': 0.65, 'domain': cdutil.region.domain(latitude=(30., 90, 'ccb'))},
    'ocean_SHEX': {'value': 0.65, 'domain': cdutil.region.domain(latitude=(-90., -30, 'ccb'))},
    # follow AMWG polar range,more precise selector
    'polar_N': {'domain': cdutil.region.domain(latitude=(50., 90., 'ccb'))},
    'polar_S': {'domain': cdutil.region.domain(latitude=(-90., -55., 'ccb'))},
    # To match AMWG results, the bounds is not as precise in this case
    # 'polar_N_AMWG':{'domain': Selector(latitude=(50., 90.))},
    # 'polar_S_AMWG':{'domain': Selector(latitude=(-90., -55.))},

    # Below is for modes of variability
    "NAM": {'domain': cdutil.region.domain(latitude=(20., 90, 'ccb'), longitude=(-180, 180, 'ccb'))},
    "NAO": {'domain': cdutil.region.domain(latitude=(20., 80, 'ccb'), longitude=(-90, 40, 'ccb'))},
    "SAM": {'domain': cdutil.region.domain(latitude=(-20., -90, 'ccb'), longitude=(0, 360, 'ccb'))},
    "PNA": {'domain': cdutil.region.domain(latitude=(20., 85, 'ccb'), longitude=(120, 240, 'ccb'))},
    "PDO": {'domain': cdutil.region.domain(latitude=(20., 70, 'ccb'), longitude=(110, 260, 'ccb'))},
    # Below is for monsoon domains
    # All monsoon domains
    'AllM': {'domain': cdutil.region.domain(latitude=(-45., 45., 'ccb'), longitude=(0., 360., 'ccb'))},
    # North American Monsoon
    'NAMM': {'domain': cdutil.region.domain(latitude=(0., 45., 'ccb'), longitude=(210., 310., 'ccb'))},
    # South American Monsoon
    'SAMM': {'domain': cdutil.region.domain(latitude=(-45., 0., 'ccb'), longitude=(240., 330., 'ccb'))},
    # North African Monsoon
    'NAFM': {'domain': cdutil.region.domain(latitude=(0., 45., 'ccb'), longitude=(310., 60., 'ccb'))},
    # South African Monsoon
    'SAFM': {'domain': cdutil.region.domain(latitude=(-45., 0., 'ccb'), longitude=(0., 90., 'ccb'))},
    # Asian Summer Monsoon
    'ASM': {'domain': cdutil.region.domain(latitude=(0., 45., 'ccb'), longitude=(60., 180., 'ccb'))},
    # Australian Monsoon
    'AUSM': {'domain': cdutil.region.domain(latitude=(-45., 0., 'ccb'), longitude=(90., 160., 'ccb'))},
}

    #
points_specs = {
    # ARM sites coordinates, select nearest grid poit to ARM site coordinates
    # Each point is supplied with [latitude, longitude,select method, description of the point]
    'sgp': [36.4, -97.5,'cob','97.5W 36.4N Oklahoma ARM'],
    'nsa': [71.3, -156.6,'cob','156.6W 71.3N Barrow ARM'],
    'twpc1': [-2.1, 147.4,'cob','147.4E 2.1S Manus ARM'],
    'twpc2': [-0.5, 166.9,'cob', '166.9E 0.5S Nauru ARM'],
    'twpc3': [-12.4, 130.9,'cob','130.9E 12.4S Darwin ARM'],

}
