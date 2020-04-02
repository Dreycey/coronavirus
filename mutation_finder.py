#usr/bin/python
## library
import sys
import json
import os
## non-standard
import matplotlib.pyplot as plt
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
    print("it is working hehe.")
    mut_count_array = []
    for protein in mut_dict:
        print(protein)
        for mutation, count in mut_dict[protein].items():
            print('\t', mutation, count)
            mut_count_array.append([protein, mutation, count])
    return mut_count_array



# plotter (make as general as possible)
def dynamic_bar_plot():
    None

# main function that controls analysis.
def main():
    # create nextstrain output
    nextstrain_input = sys.argv[1]
    print("in main()")

    output_obj = ns_parser(nextstrain_input)
    mut_freq_dict = output_obj.mutation_counter()

    # plotting
    NeededForPlotting = mutationfreq_to_plot(mut_freq_dict)
    #dynamic_bar_plot(NeededForPlotting)

    print("end main()")

if __name__ == '__main__':
    main()

