from os import listdir
def get_pet_labels(image_dir):
    in_files = listdir(image_dir)
    results_dic = dict()
    
    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            image_pet_name = in_files[idx].split("_")
            pet_label = ""
            for word in image_pet_name:
                if word.isalpha():
                    pet_label += word.lower() + " "
            # Strip off ending whitespace 
            pet_label = pet_label.strip()
            results_dic[in_files[idx]] = [pet_label]
        else:
            print("Warning- Duplicate files may exist in directory:", in_files[idx])

    print("\n All key-value dictionary results_dic are :\n")
    for key in results_dic:
        print(" Filename= ", key, " Pet Label = ", results_dic[key][0])

    return results_dic
