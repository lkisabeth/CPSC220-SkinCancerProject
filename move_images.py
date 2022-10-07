# Skin Cancer Data Set Cleaning
# Muskingum University - Applied Computer Programming (Intro to Machine Learning)
# Lucas Kisabeth
# lucask1@muskingum.edu
# 10/7/2022

# module load python/3.7-2019.10 cuda/10.1.168

import os
import csv

ROOT_PATH = "/users/PMUS0004/lucask1/Skin Cancer ML"
source_p1 = os.path.join(ROOT_PATH, "skin_cancer_archive/HAM10000_images_part_1")
source_p2 = os.path.join(ROOT_PATH, "skin_cancer_archive/HAM10000_images_part_2")
images_folder = os.path.join(ROOT_PATH, "images")
metadata_path = os.path.join(ROOT_PATH, "skin_cancer_archive/HAM10000_metadata.csv")

categories = {
    # "category": <destination folder number>
    "akiec": 1,
    "bcc": 2,
    "bkl": 3,
    "df": 4,
    "mel": 5,
    "nv": 6,
    "vasc": 7
}

def move_images(source):
    with open(metadata_path) as csvfile:
        metadata = csv.DictReader(csvfile)
        # header format: lesion_id,image_id,dx,dx_type,age,sex,localization
        for line in metadata:
            # get the image file name
            image_file = line["image_id"] + ".jpg"
            # get the category label number
            category_label = str(categories[line["dx"]])
            # get the source path
            source_path = os.path.join(source, image_file)
            # if there is an image at this path
            if os.path.exists(source_path):
                # move the image
                try:
                    # get the destination path
                    destination_path = os.path.join(
                        images_folder,
                        category_label,
                        image_file
                    )
                    os.rename(source_path, destination_path)
                    print("Moved " + image_file + " to Category Folder " + category_label)
                except Exception as e:
                    print(e)

move_images(source_p1)
move_images(source_p2)
