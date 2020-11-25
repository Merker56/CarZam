#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
from PIL import Image


# In[2]:


car_cascade = cv2.CascadeClassifier('cars.xml')
os.chdir('/home/ubuntu/s3')
drt = '/home/ubuntu/s3/'
output = '/home/ubuntu/VMMRdb'


# In[3]:


# classes = {'Chevrolet Avalanche': 0, 'Chevrolet Blazer': 1, 'Chevrolet Bolt': 2, 'Chevrolet Camaro': 3, 
#          'Chevrolet Captiva_Sport': 4, 'Chevrolet Colorado': 5, 'Chevrolet Corvette': 6, 'Chevrolet Cruze': 7, 
#          'Chevrolet Equinox': 8, 'Chevrolet Express_1500': 9, 'Chevrolet Impala': 10, 'Chevrolet Malibu': 11, 
#          'Chevrolet Silverado_1500': 12, 'Chevrolet Sonic': 13, 'Chevrolet Spark': 14, 'Chevrolet Suburban': 15, 
#          'Chevrolet Tahoe': 16, 'Chevrolet Traverse': 17, 'Chevrolet Trax': 18, 'Chevrolet Volt': 19, 'Ford Edge': 20, 
#          'Ford Escape': 21, 'Ford Expedition': 22, 'Ford Expedition_Max': 23, 'Ford Explorer': 24, 'Ford F150': 25, 
#          'Ford F250': 26, 'Ford F450': 27, 'Ford F550': 28, 'Ford Fiesta': 29, 'Ford Flex': 30, 'Ford Focus': 31, 
#          'Ford Fusion': 32, 'Ford Mustang': 33, 'Ford Ranger': 34, 'Ford Taurus': 35, 'Ford Transit_150': 36, 
#          'Ford Transit_Connect': 37, 'Honda Accord': 38, 'Honda CR_V': 39, 'Honda Civic': 40, 'Honda Crosstour': 41, 
#          'Honda Fit': 42,  'Honda HR_V': 43, 'Honda Insight': 44, 'Honda Odyssey': 45, 'Honda Passport': 46, 
#          'Honda Pilot': 47, 'Honda Ridgeline': 48, 'MercedesBenz AMG_GT': 49, 'MercedesBenz A_220': 50, 
#          'MercedesBenz CLA_250': 51, 'MercedesBenz CLS_450': 52, 'MercedesBenz CLS_550': 53, 'MercedesBenz C_250': 54, 
#          'MercedesBenz C_300': 55, 'MercedesBenz C_43_AMG': 56, 'MercedesBenz C_63_AMG': 57, 'MercedesBenz E_300': 58, 
#          'MercedesBenz E_350': 59, 'Toyota 4Runner': 60, 'Toyota 86': 61, 'Toyota Avalon': 62, 'Toyota C_HR': 63, 
#          'Toyota Camry': 64, 'Toyota Corolla': 65, 'Toyota FJ_Cruiser': 66, 'Toyota Highlander': 67, 
#          'Toyota Land_Cruiser': 68, 'Toyota Prius': 69, 'Toyota Prius_C': 70, 'Toyota Prius_Prime': 71, 
#          'Toyota Prius_V': 72, 'Toyota RAV4': 73, 'Toyota Sequoia': 74, 'Toyota Sienna': 75, 'Toyota Supra': 76, 
#          'Toyota Tacoma': 77, 'Toyota Tundra': 78, 'Toyota Venza': 79, 'Toyota Yaris': 80}
classes = {}


# In[4]:


for d, subdirs, f in os.walk(drt):
    for s in subdirs:
        for di, sub, files in os.walk(os.path.join(drt,s)):
            for filename in files:
                #Open images
                print(f'SD: {s}, FN: {filename}, DIR: {d}')
                if filename == '.DS_Store':
                    pass
                else:
                    img = cv2.imread(os.path.join(d,s,filename)) #image location
                if img is None:
                    img  = Image.open(os.path.join(d,s,filename))
                    img.save(os.path.join(output,filename)) 
                else:
                    filename = filename.replace(" ", "_")                    
                    # convert to gray scale
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

                    # Detects cars of different sizes in the input image 
                    cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
                    # if car exists create bounding box, annotation, and create greyscale image
                    if len(cars) > 0:
                        # Take filenames and separate out last 5 characters (remove the years and that last underscore)
                        n = s[:-5].title()
                        # split first _ as make then take the remainder as classes
                        make, model = n.split("_", 1)
                        make = make.replace(" ", "")
                        model = model.replace(" ", "_") #change space to _ to fix file issue
                        # add to classes if it's not in there
                        mm = str(make + ' ' + model)
                        if mm not in classes.keys():
                            classes[mm] = len(classes)
                        # annotations are of "class x y width height" all numbers must be between 0 and 1
                        hieght, width = img.shape[:2]
                        name = filename.replace("jpg", "txt", 1)
                        f = open(os.path.join(output,name), "w+")
                        # To draw a rectangle on each car
                        max_area, area, i, c = 0, 0, 0, 0
                        for (x,y,w,h) in cars: 
                            i += 1
                            cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2) 
                            #cropped the car
                            #cropped_car = img[y:y+h, x:x+w].copy()
                            #encode the image
                            rc,jpg = cv2.imencode('.jpg', gray)
                            area = w * h 
                            max_area = max(max_area, area)
                            if max_area == area:
                                c = i-1
                            if filename == '.DS_Store':
                                pass
                            else:
                                cv2.imwrite(os.path.join(output,filename), jpg)
                        #creation of annotation row
                        (x,y,w,h) = cars[c] 
                        yx = x/width
                        yy = y/hieght
                        yw = w/width 
                        yh = h/hieght
                        if classes.get(str(make + ' ' + model)) is None: 
                            val = 82 
                        else: 
                            val = classes.get(str(make + ' ' + model))
                        f.write(" ".join([str(val), str(yx), str(yy), str(yw), str(yh)]))
                        f.close()
                    else:
                        pass


# In[5]:


print(classes.keys())


# In[6]:


pwd


# In[11]:


f = open("VMMR_Classes.txt", "w+")
f.write(str(classes.keys()))
f.close


# In[12]:


f = open("VMMR_dict.txt", "w+")
f.write(str(classes))
f.close

