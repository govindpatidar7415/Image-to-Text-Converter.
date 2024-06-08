from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
import json
import os
import numpy as np
import tensorflow as tf

# Load label information
with open('./models/imagenet_classes.json', 'r') as f:
    labelInfo = json.load(f)

# Load the pre-trained model
model = load_model('./models/MobileNetModelImagenet.h5')

# Set image dimensions
img_height, img_width = 224, 224

# Create your views here.
def index(request):
    context = {'a': 1}
    return render(request, 'index.html', context)

def predictImage(request):
    if request.method == 'POST' and 'filePath' in request.FILES:
        fileobj = request.FILES['filePath']
        fs = FileSystemStorage()
        filePathName = fs.save(fileobj.name, fileobj)  
        filePathName = fs.url(filePathName)
        testimage = '.' + filePathName
        img = image.load_img(testimage, target_size=(img_height, img_width))
        x = image.img_to_array(img)
        x = x / 255
        x = np.expand_dims(x, axis=0)
        predi = model.predict(x)
        predictedLabel = labelInfo[str(np.argmax(predi[0]))]  
        context = {'filePathName': filePathName, 'predictedLabel': predictedLabel[1]}
        return render(request, 'index.html', context)
    return render(request, 'index.html')

def viewsDataBase(request):
    listofImages = os.listdir('./media/')
    listofImagesPath = ['./media/' + i for i in listofImages]
    context = {'listofImagesPath': listofImagesPath}
    return render(request, 'views.html', context)
