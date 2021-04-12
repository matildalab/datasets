import pickle
import os
import shutil

gt_list = []
folder_list = []

file_name= sorted(os.listdir("./val"))

#https://github.com/ryujaehun/alexnet/blob/master/etc/data/ILSVRC2012_validation_ground_truth.txt
f = open('ground_truth.txt')
while True:
    idx = f.readline()
    if idx == "":
        break
    idx = idx.replace("\n", "")
    gt_list.append(int(idx))
f.close()

#https://gist.github.com/aaronpolhamus/964a4411c0906315deb9f4a3723aac57
f = open('imagenet_metadata.txt')
while True:
    name = f.readline()
    if name == "":
        break
    name = name.split()
    folder_list.append(name[0])
f.close()

#make directory
for i in folder_list:
    os.mkdir('./val/'+ str(i))

# classify image file
for i in range(0,50000):
    source ='./val/'+file_name[i]
    dest='./val/'+folder_list[gt_list[i]-1]+'/'
    shutil.move(source,dest)
