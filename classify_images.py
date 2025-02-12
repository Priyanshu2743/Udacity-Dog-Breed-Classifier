# Description: This file contains the function classify_images(images_dir, results_dic, model) that uses the classifier function to classify images and compare pet labels to classifier labels. The function adds classifier labels and comparison of labels to the results dictionary.
# Imports classifier function for using CNN to classify images 
from classifier import classifier 
 
def classify_images(images_dir, results_dic, model):
    # classifier fnction
    for key in results_dic:
        #image_pat = images_dir + ke
        model_label = classifier(images_dir+key, model).lower().strip()
        truth = results_dic[key][0]
        results_dic[key].extend([model_label, 1 if truth in model_label else 0])