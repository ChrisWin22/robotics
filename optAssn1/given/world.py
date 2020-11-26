import numpy as np
import torch
from torchvision import models
from torchvision import transforms
from PIL import Image

def create_map():
    map = [['sec1.jpg', 'sec2.jpg', 'sec3.jpg', 'sec4.jpg'], ['sec5.jpg', 'sec6.jpg', 'sec7.jpg', 'sec8.jpg'], ['sec9.jpg', 'sec10.jpg', 'sec11.jpg', 'sec12.jpg'], ['sec13.jpg', 'sec14.jpg', 'sec15.jpg', 'sec16.jpg']]
    x = np.random.randint(0,4)
    y = np.random.randint(0,4)
    print("Actual location: [" + str(x) + ", " + str(y) + "]")
    map[x][y] = 'AlanStringer_Hiker.jpg'
    print('Map Loaded')
    return map

def checkForHiker(name, transform, alexnet):
    partialPath = "/home/christian/Documents/CSHW/Robotics/optAssn1/given/"
    image = Image.open(partialPath + str(name))
    transformedImage = transform(image)
    transformedBatch = torch.unsqueeze(transformedImage, 0)
    alexnet.eval()
    out = alexnet(transformedBatch)

    with open(partialPath + 'imagenet_classes.txt') as f:
	    classes = [line.strip() for line in f.readlines()]

    _, index = torch.max(out, 1)
    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
    if classes[index[0]] == '390, eel':
        return True
    return False

def run():
    alexnet = models.alexnet(pretrained=True)
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    map = create_map()
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if checkForHiker(map[i][j], transform, alexnet):
                print("found at: [" + str(i) + ", " + str(j) + "]")
                return

run()
