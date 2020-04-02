#usr/bin/python
## library
import sys
import json
import os
## non-standard
import matplotlib.pyplot as plt
import numpy as np
## from this analysis
from json_parser import nextstrain_analysis as ns_parser

"""
This script evaluates the mutations found using nextstrain.
"""


# a function that makes mutations ready for plotting
def mutationfreq_to_plot(mut_dict):
    """
    This function takes in the mutation count dictionary and returns an array
    that has all of the information ordered for plotting. 

    INPUT: json_parser.nextstrain_analysis.mutation_counter() output

    OUTPUT: [
             [protein, mutation, count],
             [ATPsynthase, M1G, 15],
             ...,
             [GFP, M1A, 23]
            ]
    """
    mut_count_array = []
    for protein in mut_dict:
        #print(protein)
        for mutation, count in mut_dict[protein].items():
            #print('\t', mutation, count)
            mut_count_array.append([protein, mutation, count])
    return mut_count_array

# plotter (make as general as possible)
def dynamic_bar_plot(input_array):
    """
    This function makes a plot for the frequency of mutations. 

    INPUT:
        [
         [protein, mutation, count], 
         [ATPsynthase, M1G, 15],
         ...
         [GFP, M1A, 23]
        ]

    OUTPUT: a PNG file with bar plots
    """
    # parameters
    cutoff = 10
    cols = 5
    output_fig_name = "figout.png"
    array = np.asarray(input_array)
    sub_plot_names = set(array[:,0])
    rows = int(round(len(sub_plot_names) / cols))
    fig, axs = plt.subplots(rows,cols, figsize=(15,10))
    print(round(len(sub_plot_names) / cols)*cols, len(sub_plot_names))
    counter = 0
    row_temp = -1
    for sp_name in sub_plot_names:
        col_temp = counter % cols
        row_temp += 1 if col_temp == 0 else 0
        #print(row_temp, col_temp)
        sp_array = array[array[:,0] == sp_name][:cutoff]
        mut_name = sp_array[:,1]
        count_vec = list(map(int, sp_array[:,2]))
        print(mut_name, count_vec)
        print("before")
        axs[row_temp, col_temp].bar(mut_name, count_vec, color = 'orange',
                                    edgecolor='b')
        axs[row_temp, col_temp].set_title(sp_name)
        axs[row_temp, col_temp].tick_params(axis='x', labelrotation=90)
        counter += 1
    fig.suptitle('Mutational frequencies for each COVID-19 gene', size=20)
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    fig.savefig(output_fig_name, dpi=300, facecolor='w', edgecolor='b',
        orientation='portrait', papertype=None, format=None,
        transparent=True, pad_inches=1,
        metadata=None)




# main function that controls analysis.
def main():
    # create nextstrain output
    nextstrain_input = sys.argv[1]
    print("in main()")

    output_obj = ns_parser(nextstrain_input)
    mut_freq_dict = output_obj.mutation_counter()

    # plotting
    NeededForPlotting = mutationfreq_to_plot(mut_freq_dict)
    dynamic_bar_plot(NeededForPlotting)

    print("end main()")

if __name__ == '__main__':
    main()

