import os
import random
labels = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
labels = ['ix']

for label in labels:
    print('===============')
    print (label)
    image_files = os.listdir('vii_enhanced_14'+'/train/'+label+'/')
    for image_file in image_files:
        #if '.png' in image_file and 'aug' not in image_file and 'rot' not in image_file and 'trans' not in image_file:
        if "IMG" in image_file:
            print (image_file)
            #command = "convert -page -1-1 -background none -flatten "+'label_book/'+label+'/'+image_file+" "+'label_book_trans/'+label+'/trans_'+image_file
            v=0
            while v<5:
                if len(os.listdir('vii_enhanced_14'+'/train/'+label+'/'))>=1100:
                    break
                v+=1
                angle = random.randint(-10, 10)
                command = "convert -rotate "+str(angle)+" "+'vii_enhanced_14/train/'+label+'/'+image_file+" "+'vii_enhanced_14/train/'+label+'/rot_'+str(v)+'_'+image_file
                print (command)
                os.system(command)

                move1  = random.randint(-1, 4)
                move2  = random.randint(-1, 4)
                if move2>0:
                    str_move2='+'+str(move2)
                else:
                    str_move2=str(move2)

                if move1>0:
                    str_move1='+'+str(move1)
                else:
                    str_move1=str(move1)

                command = "convert -page "+str(str_move1)+str(str_move2)+" -background none -flatten "+'vii_enhanced_14/train/'+label+'/'+image_file+" "+'vii_enhanced_14/train/'+label+'/trans_'+str(v)+'_'+image_file
                print(command)
                os.system(command)

# Only transate
move1  = random.randint(-1, 4)
move2  = random.randint(-1, 4)


#Only rot
angle = random.randint(-10, 10)
