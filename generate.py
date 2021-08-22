# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
from datetime import datetime
import time
import sys
import os
import random

list = "list.txt"
sourceImageName = "source.jpg"

allPersons = sum(1 for line in open(list))

person = 0

startTime = datetime.now()
print("")

certificateDirectory = "Certificate " + str(datetime.now().strftime("%Y%m%d%H%M%S")) + "-" + str(random.randint(100, 999))

if not os.path.exists(certificateDirectory):
    os.makedirs(certificateDirectory)

while person < allPersons:
	with open(list) as lines:
	    content = lines.readlines()
	
	content = [stripContent.strip() for stripContent in content] 
	result = content[person].split(',')
	
	sourceImage = Image.open(sourceImageName)

	employeeNamefontSize = 67
	employeeIdfontSize = 148

	employeeNamefont = ImageFont.truetype('calibrib.ttf', employeeNamefontSize)
	employeeIdfont = ImageFont.truetype('calibrib.ttf', employeeIdfontSize)

	resultedImage = ImageDraw.Draw(sourceImage)
	
	w, h = resultedImage.textsize(result[1], font=employeeNamefont)

	resultedImage.text((1578,735), result[0], (237, 230, 211), font=employeeIdfont)
	resultedImage.text(((2474-w)/2,1650), result[1], (237, 230, 211), font=employeeNamefont)

	sourceImage.save(certificateDirectory + "/" + result[1] + ".jpg")
		
	person = person + 1
	
	sys.stdout.write("\rСоздано: "+str(person) + " из " + str(allPersons))
	sys.stdout.flush()

print("")
print("Выполнено.")
print("Время выполнения: " + str(datetime.now() - startTime))
print("")