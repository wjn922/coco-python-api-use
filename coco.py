from pycocotools.coco import COCO
import cv2
import os
import matplotlib.pyplot as plt

colorname = [
'aliceblue',
'antiquewhite',
'aqua',
'aquamarine',
'azure',
'beige',
'bisque',
'black',
'blanchedalmond',
'blue',
'blueviolet',
'brown',
'burlywood',
'cadetblue',
'chartreuse',
'chocolate',
'coral',
'cornflowerblue',
'cornsilk',
'crimson',
'cyan',
'darkblue',
'darkcyan',
'darkgoldenrod',
'darkgray',
'darkgreen',
'darkkhaki',
'darkmagenta',
'darkolivegreen',
'darkorange',
'darkorchid',
'darkred',
'darksalmon',
'darkseagreen',
'darkslateblue',
'darkslategray',
'darkturquoise',
'darkviolet',
'deeppink',
'deepskyblue',
'dimgray',
'dodgerblue',
'firebrick',
'floralwhite',
'forestgreen',
'fuchsia',
'gainsboro',
'ghostwhite',
'gold',
'goldenrod',
'gray',
'green',
'greenyellow',
'honeydew',
'hotpink',
'indianred',
'indigo',
'ivory',
'khaki',
'lavender',
'lavenderblush',
'lawngreen',
'lemonchiffon',
'lightblue',
'lightcoral',
'lightcyan',
'lightgoldenrodyellow',
'lightgreen',
'lightgray',
'lightpink',
'lightsalmon',
'lightseagreen',
'lightskyblue',
'lightslategray',
'lightsteelblue',
'lightyellow',
'lime',
'limegreen',
'linen',
'magenta',
'maroon',
'mediumaquamarine',
'mediumblue',
'mediumorchid',
'mediumpurple',
'mediumseagreen',
'mediumslateblue',
'mediumspringgreen',
'mediumturquoise',
'mediumvioletred',
'midnightblue',
'mintcream',
'mistyrose',
'moccasin',
'navajowhite',
'navy',
'oldlace',
'olive',
'olivedrab',
'orange',
'orangered',
'orchid',
'palegoldenrod',
'palegreen',
'paleturquoise',
'palevioletred',
'papayawhip',
'peachpuff',
'peru',
'pink',
'plum',
'powderblue',
'purple',
'red',
'rosybrown',
'royalblue',
'saddlebrown',
'salmon',
'sandybrown',
'seagreen',
'seashell',
'sienna',
'silver',
'skyblue',
'slateblue',
'slategray',
'snow',
'springgreen',
'steelblue',
'tan',
'teal',
'thistle',
'tomato',
'turquoise',
'violet',
'wheat',
'white',
'whitesmoke',
'yellow',
'yellowgreen']


def draw_box(anns):
	for i in range(len(anns)):
		x, y, w, h = anns[i]['bbox']
		x, y, w, h = float(x), float(y), float(w), float(h)
		#print(x,y,w,h,'\t')
		plt.gca().add_patch(plt.Rectangle(xy=(x,y), width=w, height=h, \
			color=colorname[(3*i)%140], fill=False, linewidth=2))


# 1.加载
dataDir = '.'
dataType = 'val2017'
annFile = '{}/annotations/instances_{}.json'.format(dataDir, dataType)
coco = COCO(annFile)

# 2.显示类和超类名
cats = coco.loadCats(coco.getCatIds())
nms = [cat['name'] for cat in cats]
ids = [cat['id'] for cat in cats]
dic_cats = [str(cat['id'])+"_"+cat['name'] for cat in cats]
print("\ncoco categories: \n {} \n".format(' '.join(dic_cats)))
#print("\ncoco categories: \n {} \n".format(' '.join(nms)))

nms = set([cat['supercategory'] for cat in cats])
print("coco supercategories: \n {} \n".format(' '.join(nms)))

# 3.加载并显示指定id的图片
catIds = coco.getCatIds(catNms=['person','truck','dog'])
imgIds = coco.getImgIds(catIds=catIds)
img = coco.loadImgs(imgIds[:])[0] # 第一张图，返回的该图的字典信息

img_path = os.path.join("./val2017/",img['file_name'])
#img_show = cv2.imread(img_path)


#4 将标注信息显示在图上
annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None) #这里只找所需类的annotation					
anns = coco.loadAnns(annIds)  # 一张图可能对应多个ann
print(anns)

# fig = plt.figure()
I = plt.imread(img_path)
plt.imshow(I)
draw_box(anns)
plt.axis('off')
coco.showAnns(anns)
plt.savefig("test.jpg")
plt.show()
