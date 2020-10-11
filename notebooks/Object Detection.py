
# coding: utf-8

# In[1]:


import cv2
import os
from PIL import Image


# In[2]:


os.chdir('/home/ubuntu/s3')


# In[3]:


#Use Opencv car classifier
car_cascade = cv2.CascadeClassifier('cars.xml')


# ### Stanford Cars Train

# In[14]:


drt = '/home/ubuntu/s3/stanford/cars_train'
output = '/home/ubuntu/sc/s_train/'


# In[15]:


#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    print(f'First loop. SD: {subdir}, DR: {dirs}, FN: {files}')
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# ### Stanford Cars Test

# In[4]:


drt = '/home/ubuntu/s3/stanford/cars_test'
output = '/home/ubuntu/sc/s_test/'


# In[5]:


#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    print(f'First loop. SD: {subdir}, DR: {dirs}, FN: {files}')
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# ### Honda Autotrader

# In[4]:


drt = '/home/ubuntu/sc/Honda/'
output = '/home/ubuntu/sc/Honda/od'


# In[ ]:


#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    print(f'First loop. SD: {subdir}, DR: {dirs}, FN: {files}')
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# ### Toyota Autotrader

# In[10]:


drt = '/home/ubuntu/sc/Toyota/86'
output = '/home/ubuntu/sc/Toyota/od'


# In[18]:


#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    print(f'First loop. SD: {subdir}, DR: {dirs}, FN: {files}')
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[19]:


drt = '/home/ubuntu/sc/Toyota/Avalon'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    print(f'First loop. SD: {subdir}, DR: {dirs}, FN: {files}')
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[20]:


drt = '/home/ubuntu/sc/Toyota/C-HR'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    print(f'First loop. SD: {subdir}, DR: {dirs}, FN: {files}')
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[21]:


drt = '/home/ubuntu/sc/Toyota/Camry'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[22]:


drt = '/home/ubuntu/sc/Toyota/Corolla'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[23]:


drt = '/home/ubuntu/sc/Toyota/FJCruiser'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[24]:


drt = '/home/ubuntu/sc/Toyota/Highlander'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[25]:


drt = '/home/ubuntu/sc/Toyota/Landcruiser'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[26]:


drt = '/home/ubuntu/sc/Toyota/Matrix'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[27]:


drt = '/home/ubuntu/sc/Toyota/Prius'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[28]:


drt = '/home/ubuntu/sc/Toyota/PriusC'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[ ]:


drt = '/home/ubuntu/sc/Toyota/PriusPrime'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[29]:


drt = '/home/ubuntu/sc/Toyota/PriusV'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[30]:


drt = '/home/ubuntu/sc/Toyota/RAV4'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[31]:


drt = '/home/ubuntu/sc/Toyota/Sequoia'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[32]:


drt = '/home/ubuntu/sc/Toyota/Supra'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[33]:


drt = '/home/ubuntu/sc/Toyota/Tacoma'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[ ]:


drt = '/home/ubuntu/sc/Toyota/Tundra'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[34]:


drt = '/home/ubuntu/sc/Toyota/Venza'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# In[35]:


drt = '/home/ubuntu/sc/Toyota/Yaris'
output = '/home/ubuntu/sc/Toyota/od'
#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, DR: {dirs}, FN: {filename}')
        img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            pass
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)

                cv2.imwrite(os.path.join(output,filename), jpg)


# ### VMMRdb

# In[4]:


drt = '/home/ubuntu/s3/VMMRdb/'
output = '/home/ubuntu/sc/VMMRdb'


# In[13]:


get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plt
plt.imshow(img)
plt.show()


# In[ ]:


##For VMMRdb, not working atm

#For loop going through each directory and sub-directory for cars
for subdir, dirs, files in os.walk(drt):
    for filename in files:
        #Open images
        print(f'SD: {subdir}, FN: {filename}')
        if filename == '.DS_Store':
            pass
        else:
            img = cv2.imread(os.path.join(subdir,filename)) #image location
        if img is None:
            img  = Image.open(os.path.join(subdir,filename))
            img.save(os.path.join(output,filename)) 
        else:
            # convert to gray scale of each frames 
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

            # Detects cars of different sizes in the input image 
            cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

            # To draw a rectangle on each car
            for (x,y,w,h) in cars: 
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
                #cropped the car
                cropped_car = img[y:y+h, x:x+w].copy()
                #encode the image
                rc,jpg = cv2.imencode('.jpg', cropped_car)
                if filename == '.DS_Store':
                    pass
                else:
                    cv2.imwrite(os.path.join(output,filename), jpg)
                #print(os.path.join(output,filename))


# In[11]:


len(img)


# In[12]:


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

# Detects cars of different sizes in the input image 
cars = car_cascade.detectMultiScale(gray, 1.1, 1) 

# To draw a rectangle on each car
for (x,y,w,h) in cars: 
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) 
    #cropped the car
    cropped_car = img[y:y+h, x:x+w].copy()
    #encode the image
    rc,jpg = cv2.imencode('.jpg', cropped_car)
    if filename == '.DS_Store':
        pass
    else:
        cv2.imwrite(os.path.join(output,filename), jpg)

