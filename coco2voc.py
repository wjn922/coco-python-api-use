import os
import matplotlib.pyplot as plt
from pycocotools.coco import COCO
import pandas as pd
import numpy as np
import time

img_dir = "./val2017/"
ann_path = "./annotations/instances_val2017.json"

label_dir = "./labels/"
if not os.path.exists(label_dir):
	os.mkdir(label_dir)


time_open = time.time()
coco = COCO(ann_path)

################### Create label folder ###############
# 获取所有的图片 字典信息
img_dict = coco.loadImgs(coco.getImgIds()) 
#print(img_dict[0:5])

# pd保存图片信息
img_num = len(img_dict)
img_df = pd.DataFrame([img_dict[0]])
for i in range(1, img_num):
	df_temp = pd.DataFrame([img_dict[i]])
	img_df = pd.concat([img_df, df_temp])
img_df.to_csv("image.csv", index=False)

# 写label文件
for i in range(img_num):
	img = img_df.iloc[i]
	width = img['width']
	height = img['height']
	annIds = coco.getAnnIds(imgIds=img['id'])
	anns = coco.loadAnns(annIds)  # 一张图可能对应多个ann

	with open(os.path.join(label_dir, img['file_name'].split('.')[0]+'txt'), 'w') as f:
		for i in range(len(anns)):
			line = []
			line.append(str(anns[i]['category_id'])+'\t')
			x, y, w, h = anns[i]['bbox']
			#x = float(x) / width
			#y = float(y) / height
			#w = float(w) / width
			#h = float(h) / height
			line.append(str(x)+'\t')
			line.append(str(y)+'\t')
			line.append(str(w)+'\t')
			line.append(str(h)+'\n')
			f.writelines(line)



################### Create train and test names files #############
with open('train.txt','w') as f:
	for i in range(img_num):
		img = img_df.iloc[i]
		img_name = img['file_name']
		line = img_dir + img_name + '\n'
		f.writelines(line)


################ Create names(classes) file ####################
# Get the names of all classes
cats = coco.loadCats(coco.getCatIds())
nms = [cat['name'] for cat in cats]
with open('coco.names','w') as f:
	for i in range(len(nms)):
		line = nms[i] + '\n'
		f.writelines(line)



time_end = time.time()-time_open
print("Finished in %fs" %time_end)


