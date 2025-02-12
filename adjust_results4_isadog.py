def adjust_results4_isadog(results_dic, dogfile):
    dognames_dict = dict()

    # Reads in dognames from file,
    with open(dogfile, "r") as infile:
        # Reads in dognames 
        line = infile.readline()

 
        # processing line and adding dognames to dognames_dic with while loop
        while line != "":
            if line not in dognames_dict:
                dognames_dict[line.rstrip()] = 1
            
            line = infile.readline()

    for key in results_dic:

        # Pet Image Label IS of Dog (e.g. found in dognames_dic)
        if results_dic[key][0] in dognames_dict:

            if results_dic[key][1] in dognames_dict:
                results_dic[key].extend((1, 1))

            else:
                results_dic[key].extend((1, 0))


        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
        else:
            if results_dic[key][1] in dognames_dict:
                results_dic[key].extend((0, 1))
            else:
                results_dic[key].extend((0, 0))





    