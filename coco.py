from pycocotools.coco import COCO
import cv2
import os
import matplotlib.pyplot as plt

# 1.加载
dataDir = '.'
dataType = 'val2017'
annFile = '{}/annotations/instances_{}.json'.format(dataDir, dataType)
coco = COCO(annFile)

# 2.显示类和超类名
cats = coco.loadCats(coco.getCatIds())
nms = [cat['name'] for cat in cats]
print("\ncoco categories: \n {} \n".format(' '.join(nms)))

nms = set([cat['supercategory'] for cat in cats])
print("coco supercategories: \n {} \n".format(' '.join(nms)))

# 3.加载并显示指定id的图片
catIds = coco.getCatIds(catNms=['person','truck','dog'])
imgIds = coco.getImgIds(catIds=catIds)
img = coco.loadImgs(imgIds[:])[0] # 第一张图

img_path = os.path.join("./val2017/",img['file_name'])
img_show = cv2.imread(img_path)


#4 将标注信息显示在图上
annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco.loadAnns(annIds)  # 一张图可能对应多个ann

I = plt.imread(img_path)
plt.imshow(I)
plt.axis('off')
coco.showAnns(anns)
plt.show()

