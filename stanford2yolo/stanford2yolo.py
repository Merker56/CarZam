from scipy.io import loadmat
from PIL import Image

trainAnnot = loadmat('cars_train_annos.mat')
meta = loadmat('cars_meta.mat')
x = trainAnnot['annotations']
imagedir = '/Users/adminwk/w210/detector/stanford/cars_train/'
outdir = '/Users/adminwk/w210/detector/stanford/yoloannot/'

for example in trainAnnot['annotations'][0]:
    x1 = example[0][0]
    y1 = example[1][0]
    x2 = example[2][0]
    y2 = example[3][0]
    width = float(x2 - x1)
    height = float(y2 - y1)
    centerX = float(x1 + x2) / 2.0
    centerY = float(y1 + y2) / 2.0
    image = example[-1][0]

    im = Image.open(imagedir + image)
    imageWidth = float(im.size[0])
    imageHeight = float(im.size[1])

    yoloX = centerX / imageWidth
    yoloY = centerY / imageHeight
    yoloWidth = width / imageWidth
    yoloHeight = height / imageHeight

    outputFilename = outdir + image.replace('jpg', 'txt')
    f = open(outputFilename, "w")
    f.write('0 %f %f %f %f' % (yoloX, yoloY, yoloWidth, yoloHeight))
    f.close()

