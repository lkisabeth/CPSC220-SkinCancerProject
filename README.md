# CPSC220-SkinCancerProject
Tensorflow Models for Skin Cancer Recognition

# Part 1: Organizing and Cleaning the Data

*The data required for this project is stored on Owens Ohio Supercomputer Center. The files in this repo are being uploaded to and run on the supercomputer.*

`move_images.py` organizes the provided skin cancer images into seperate folders by category (1-7).

Categories:
1) akiec  Actinic Keratoses    20% metastasize
2) bcc    Basal Cell Carcinoma Less than 1% metastasize
3) bkl    Benign Keratosis     Benign
4) df     Dermatofibroma       Rarely metastasize
5) mel    Malignant Melanoma   Malignant
6) nv     Melanocytic Nevi     Can be malignant
7) vasc   Vascular Lesions     Can be malignant


`count_images.sh` is a bash script that simply counts the number of images in each of the category folders

Initial Image Counts by Category:
1) 327
2) 514
3) 1099
4) 115
5) 1113
6) 6705
7) 142

For each category with fewer than 1000 images, `augment_image_set.py` will augment the image set by creating flipped, flopped, and flip-flopped versions of the images.

Image Counts After Augmentation:
1) 1308
2) 2056
3) 1099
4) 460
5) 1113
6) 6705
7) 568
