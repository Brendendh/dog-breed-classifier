#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#                                                                             
# PROGRAMMER: Brenden Lee
# DATE CREATED: 10/18/2023                          
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
#

# Imports python modules
from time import time, sleep

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Record start time
    start_time = time()
    
    # Get the input arguments and puts it into in_arg
    in_arg = get_input_args()

    # Gets pet labels from filename and returns a results dictionary
    results = get_pet_labels(in_arg.dir)

    # Classifies images
    classify_images(in_arg.dir, results, in_arg.arch)

    # Extend the results dictionary with checks if the classifier is correct
    adjust_results4_isadog(results, in_arg.dogfile)


    # Calculate results stats
    results_stats = calculates_results_stats(results)

    # Print summary results
    print_results(results, results_stats, in_arg.arch, True, True)
    
    # Collect end time
    end_time = time()
    
    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time#calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
