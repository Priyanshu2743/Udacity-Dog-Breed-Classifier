from classifier import classifier 
test_image="pet_images/German_shorthaired_pointer_04986.jpg"
model = "shalnet"
image_classification = classifier(test_image, model)
print("\n Results of test_classifier.py \n Image:", test_image, " using model: ",
      model, " was classified as a: ", image_classification)