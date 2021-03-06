import os
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from acme_diags.driver.utils.general import get_output_dir


def plot(var, regions_to_data, parameter):
    # Data is a list based on the len of the regions parameter.
    # Each element is a tuple with ref data,
    # test data, and metrics for that region.

    # plot time series
    plotTitle = {'fontsize': 8.5}
    plotSideTitle = {'fontsize': 6.5}

    # Position and sizes of subplot axes in page coordinates (0 to 1)
    # The dimensions [left, bottom, width, height] of the new axes. All quantities are in fractions of figure width and height.
    line_color = ['r', 'b', 'g', 'm']

    panel = [(0.1500, 0.5500, 0.7500, 0.3000),
             (0.1500, 0.1300, 0.7500, 0.3000),
             ]

    panel = [(0.1, 0.68, 0.25, 0.25),
             (0.4, 0.68, 0.25, 0.25),
             (0.7, 0.68, 0.25, 0.25),
             (0.1, 0.38, 0.25, 0.25),
             (0.4, 0.38, 0.25, 0.25),
             (0.7, 0.38, 0.25, 0.25),
             (0.1, 0.08, 0.25, 0.25),
             (0.4, 0.08, 0.25, 0.25),
             (0.7, 0.08, 0.25, 0.25),
             ]

    # Create the figure.
    figsize = [11.0, 8.5]
    dpi = 150
    fig = plt.figure(figsize=figsize, dpi=dpi)
    num_year = int(parameter.test_end_yr) - int(parameter.test_start_yr) +1

    for i_region, data_set_for_region in enumerate(regions_to_data.values()):
        refs = data_set_for_region.refs
        test = data_set_for_region.test
        ax1 = fig.add_axes(panel[i_region])
        ax1.plot(test.asma(), 'k', linewidth=2,label = 'model' +' ({0:.1f})'.format(np.mean(test.asma())))
        for i_ref, ref in enumerate(refs):
            ax1.plot(ref.asma(), line_color[i_ref], linewidth=2,label = ref.ref_name +' ({0:.1f})'.format(np.mean(ref.asma())))

        x = np.arange(num_year)
        ax1.set_xticks(x)
        x_ticks_labels = [str(x) for x in range(int(parameter.test_start_yr),int(parameter.test_end_yr)+1)]
        ax1.set_xticklabels(x_ticks_labels, rotation='45', fontsize=6)

        if i_region % 3 == 0 :
            ax1.set_ylabel('variable name (units)')
            #ax1.set_ylabel(test.long_name + ' (' + test.units + ')')
        ax1.legend(loc=1, prop={'size': 6})
        fig.text(panel[i_region][0]+0.12, panel[i_region][1]+panel[i_region][3]-0.015, parameter.regions[i_region],ha='center', color='black')
    # Figure title.
    fig.suptitle('Annual mean ' + var + ' over regions ' + parameter.test_name_yrs, x=0.5, y=0.97, fontsize=15)

    # Save the figure.
    output_file_name = var
    for f in parameter.output_format:
        f = f.lower().split('.')[-1]
        fnm = os.path.join(get_output_dir(parameter.current_set,
            parameter), output_file_name + '.' + f)
        plt.savefig(fnm)
        # Get the filename that the user has passed in and display that.
        # When running in a container, the paths are modified.
        fnm = os.path.join(get_output_dir(parameter.current_set, parameter,
            ignore_container=True), output_file_name + '.' + f)
        print('Plot saved in: ' + fnm)

    plt.close()

