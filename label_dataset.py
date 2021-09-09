import pandas as pd
import os
from shutil import copyfile
import sys

# The folder where you would like to store you data folder
dataset_id = sys.argv[1]
data_folder = dataset_id+'/data/'

# Labels is the CSV file you download from Tordnado
df = pd.read_csv(dataset_id+'/labels.csv')
count = 0
labels = []
for index, row in df.iterrows():
    label = row['1d907373cbcf2513a4d4c8c760a06cc6_human_label']#row['auto_label']
    image_file = './raw_data/'+row['image_file']
    if not pd.isna(label): #row['auto_proba']>=.8:
        if label not in labels:
            labels.append(label)
        print (label)
        print("======")
        count += 1
        number_of_current_val_files = len(os.listdir(data_folder+'val/'+label+'/'))
        print(number_of_current_val_files)
        if number_of_current_val_files<50:
            # Add to val
            print(image_file+' copied to val')
            copyfile(image_file,data_folder+'val/'+label+'/'+row['image_file'])
        else:
            # Add to train
            copyfile(image_file,data_folder+'train/'+label+'/'+row['image_file'])
            print(image_file+' copied to train')
