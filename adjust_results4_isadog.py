def adjust_results4_isadog(results_dic, dogfile):
    dognames_dict = dict()
    with open(dogfile, "r") as infile:
        line = infile.readline()
        while line != "":
            if line not in dognames_dict:
                dognames_dict[line.rstrip()] = 1
            line = infile.readline()

    for key in results_dic:
        if results_dic[key][0] in dognames_dict:

            if results_dic[key][1] in dognames_dict:
                results_dic[key].extend((1, 1))
            else:
                results_dic[key].extend((1, 0))
        
        else:
            if results_dic[key][1] in dognames_dict:
                results_dic[key].extend((0, 1))
            else:
                results_dic[key].extend((0, 0))   