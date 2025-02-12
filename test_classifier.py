from classifier import classifier 

test_image="pet_images/Collie_03797.jpg"
model = "shalnet"
image_classification = classifier(test_image, model)
print("\n Results of test_classifier.py \n Image:", test_image, " using model: ",
      model, " was classified as a: ", image_classification)