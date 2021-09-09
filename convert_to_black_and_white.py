import pandas as pd
import os
from shutil import copyfile
import sys


dataset_id = sys.argv[1]
data_folder = dataset_id+'/train'


labels = ['i','ii','iii','iv','v','vi','vii','viii','ix','x']
for label in labels:
    image_files = os.listdir(data_folder+'/'+label+'/')
    for image_file in image_files:
        #command = "convert -channel RGB -negate "+data_folder+'/'+label+'/'+image_file+" "+data_folder+'/'+label+'/'+image_file
        #command = "convert -fuzz 1% -trim +repage "+data_folder+'/'+label+'/'+image_file+" "+data_folder+'/'+label+'/'+image_file
        #command = "convert -threshold 99% "+data_folder+'/'+label+'/'+image_file+" "+data_folder+'/'+label+'/'+image_file
        #Crop
        #command = "convert -fuzz 1% -trim +repage "+data_folder+'/'+label+'/'+image_file+" "+data_folder+'/'+label+'/'+image_file
        # Smooth
        #command = "convert -median 1 "+data_folder+'/'+label+'/'+image_file+" "+data_folder+'/'+label+'/'+image_file
        # Black and White
        command = "convert -alpha off -threshold 50% "+data_folder+'/'+label+'/'+image_file+" "+data_folder+'/'+label+'/'+image_file
        print(command)
        ret_code = os.system(command)
        if ret_code == 0:
            print(image_file+' Reverted')
