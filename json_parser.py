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

    INPUT: 

    OUTPUT: 
    """
    
    pass

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
