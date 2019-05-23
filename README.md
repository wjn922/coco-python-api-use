# coco-python-api-use
A simple demo of coco python API.
-------
### 1. Files
```
-- val2017
   -- xxxxx.jpg
   -- xxxxx.jpg
   ...
-- annotaions
   -- instances_val2017.json
coco.py
```
### 2. Install coco python API
```
pip install Cython
pip install pycocotools
```

### 3. How to use
a. Display the image with mask and bbox. 
```
python3 coco.py
```
b. convert coco format to voc format.    
*coco format: all label stored in .json*    
*voc format: one image corresponds to one .txt*    
```
python3 coco2voc.py
```
