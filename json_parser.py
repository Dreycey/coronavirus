#usr/bin/python
## library
import sys
import json
import os
## non-standard

"""
This script modifies the input JSON files that output by nextstrain and
retrieves information such as 

(1) CSV output for the location and mutation of the strains. 

(2) 
"""


class nextstrain_output():
    """
    This class defines the nextstrain output object, and the methods within this
    class are used to parse the output files. 

    INPUT: Nextflow directory containing JSON files. 

    OUTPUT: Each function outputs a dictoinary format as follows: 
          { seq_name_1: {},  seq_name_2: {}, ..., seq_name_n: {}}

    """
    #constructor
    def __init__(self, output_dir):
        self.directory = output_dir

    def sanity_check(self):
        print(self.directory)
        print("it's working. nice.")

    # parsing the JSON containing information on the location.
    def parsing_area_json(self):
        """
        This function will parse the JSON containing information on the location
        for the different sequences in the nextflow output. 

        INPUT: self

        OUTPUT: 
            { seq_name_1: ["2020.1734972677596", "2020-03-04"],
              seq_name_2: ["2019.995890410959", "2019-12-30"],
              , ..., 
              seq_name_n: ["2020.0478142076502", "2020-01-18"]
            }
        """
        nodelength_location = os.path.join(self.directory, 'branch_lengths.json')
        json_data = json.loads(open(nodelength_location).read())
        parsing_loc_dict = {}
        sequences_nodes = json_data["nodes"]
        for seq_id in sequences_nodes.keys():
            if "NODE" not in seq_id:
                node_info = sequences_nodes[seq_id]
                try:
                    parsing_loc_dict[seq_id] = [node_info["numdate"],
                                                node_info["raw_date"]]
                except:
                    None
        return parsing_loc_dict

    # parsing information on the mutations present in the nucelotides.
    def parsing_nt_mutations(self):
        """
        This function will parse the JSON containing information on the
        nucleotide mutation for the different sequences in the nextflow output. 

        INPUT: self

        OUTPUT:
            { 'reference': 'ATGTC..TACGTC',  seq_name_2: ['A153G', ...,'A13C'], ...}
        """
        ntMut_location = os.path.join(self.directory, 'nt_muts.json')
        json_data = json.loads(open(ntMut_location).read())
        parsing_nt_dict = {"reference" : json_data["reference"]["nuc"]}
        sequences_nodes = json_data["nodes"]
        for seq_id in sequences_nodes.keys():
            seq_name = seq_id
            seq_mutations = sequences_nodes[seq_id]["muts"]
            parsing_nt_dict[seq_name] = seq_mutations
        return json_data

    # parsing information on the mutations present in the proteins.
    def parsing_aa_mutations(self):
        """
        This function will parse the JSON containing information on the
        amino acids mutations for the different sequences in the nextflow output. 

        INPUT: self

        OUTPUT: 
            { "annotations" : {gene1 : {info}, gene2 : {info}}, 
              "reference" : {gene1 : 'SWYTYCTYTS', gene2 : 'SWYTYCTYTS'}
              "seq1" : {gene1 : ['S153T'], gene2 :['S13T']},
              "seq2" : {gene1 : ['S153T'], gene2 :['S13T']},
              ...
            }
        """
        aaMut_location = os.path.join(self.directory, 'aa_muts.json')
        json_data = json.loads(open(aaMut_location).read())
        parsing_aa_dict = {"reference" : json_data["reference"],
                          "annotations" : json_data["annotations"]}
        sequences_nodes = json_data["nodes"]
        for seq_id in sequences_nodes.keys():
            mutation_dict = {k : v for k, v in
                             sequences_nodes[seq_id]["aa_muts"].items()}
            parsing_aa_dict[seq_id] = mutation_dict
        return parsing_aa_dict

class nextstrain_analysis(nextstrain_output):
    """
    nextstrain_analysis is the child class of nextstrain_output, inheriting all
    of the parsing functions. The analysis methods can take full advantage of
    the parsing methods in the base class to perform objectives.
    """

    # function that returns the counts of each mutation type
    def mutation_counter(self):
        """
        The goal of this function is to find the mutations that occur the most
        often by couting occurances.
        """
        None

    # function that returns location, time, type of mutation
        ## plot each mutation type that occurs more than twice
            # as count over time. 
        ## based on location, what mutations are seen the most often (top 5)
    def join_mutLocTime(self):
        """
        This function joins all of the data for aa mutations together.

        INPUT:

        OUTPUT:
        """
        None

    ## timecourse plotter - plot mutation over time
    def timecourse_array(self, mutation, location, join_mutLocTime_OUT): 
        """
        This function returns an array for an input mutation in the number of 
        mutations over time, for a particular location
        """
        None

    ## create protein sequence using mutations
    def strain_aa_creater(self, prot_sequence, mut_array):
        """
        This function takes in the reference protein sequence (string), and the
        identified amino acid changes (array). It uses this information to
        create a protein with the substitutions inside the array. 

        NOTE: may need to look for deletions too

        INPUT: strain_creater("YWSAGCTYTAYCTTCG", ['Y1A', 'S3G'])

        OUTPUT: "AWGAGCTYTAYCTTCG"
        """
        None 

    ## create genome sequence using mutations
    def strain_nt_creater(self, prot_sequence, mut_array):
        """
        This function takes in the reference genome sequence (string), and the
        identified nucleotide changes (array). It uses this information to
        create a genome with the substitutions inside the array. 

        NOTE: may need to look for deletions too

        INPUT: strain_creater("ATACTAGCTATCG", ['A1T', 'A3G'])

        OUTPUT: "TTGCTAGCTATCG"
        """
        None 

    ## think about cooccurance here.
        # how many snps happen at the same time?
    def find_cooccurance(self):
        """
        empty now -- but plot cooccurances. Mabye use some graph theory to try
        and find mutations that may be commonly cooccuring in order to identify
        what has been made, AND what has the potential to be made (on the
        protein level)

        INPUT: 

        OUTPUT: 
        """
        None

    # function that returns a table of mutations that happened independently
       # for both protein and nucleotides
        # different cities, near the same time? 
    def indiMut(self):
        """
        The goal of this function is to find mutations that are suspected to
        have happened independently. The idea here is that these meet a set of
        rules (defined in this function), and if they meet these rules they were
        thought to be independently occuring mutations. 

        INPUT: self
        OUTPUT: {"G26A" : {"init_country" : [],
                           "init_time:" : [],
                           "counts" : []
                          }
        """
        None

    # based on counts, returns ordered protein sequences
    # mabye use a baysian model here?
    def most_common_muts():
        """
        The purpose for this method is to find the mutations that occur the most
        often for each protein. Therefore returning a nested dictionary with a
        key for each protein, and two sub dictionaries: "counts" and "muts".
        The "counts" dictionary contains (mutID : count) and muts contains 
        (mutID : [mut1, mut2, ...,  mutN]).

        NOTE: mutID is randomly assigned int

        INPUT: self

        OUPUT: {prot1 : {"counts" : {mutID : count, ...},
                         "mut" : {mutID : [mut1, mut2, ...,  mutN], ...}
                        },
                prot2 : {},
                ...,
                protN : {}
               }
        """
        None

# main function that controls analysis. 
def main():
    # create nextstrain output
    nextstrain_input = sys.argv[1]
    print("in main()")
    output_obj = nextstrain_analysis(nextstrain_input)
    output_obj.sanity_check()
    print(output_obj.parsing_area_json())
    print("end main()")

if __name__ == '__main__':
    main()


