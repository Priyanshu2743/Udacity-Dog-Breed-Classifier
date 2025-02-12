import argparse
def get_input_args():

    parser= argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='Path to pet images')
    parser.add_argument('--arch', default='shalnet',
                  help=' CNN model architecture')
    parser.add_argument('--dogfile', default='dognames.txt',
                  help='Path to text file w dog names')
    return parser.parse_args()
