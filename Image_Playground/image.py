import sys
import os
from PIL import Image

#grab first and second item
FirstFolder = sys.argv[1]
SecondFolder = sys.argv[2]

#Check if the Secondfolder is there or not

if not os.path.exists(SecondFolder):
	os.mkdir(SecondFolder)
	print(f'{SecondFolder} Folder Created')
else:
	print(f'{SecondFolder} Already Exists')
	


#LOOP THROUGH Pokedox

for item in os.listdir(FirstFolder):
	convertimg = os.path.splitext(item)[0]
	img = Image.open(f"{FirstFolder}{item}")
	img.save(os.path.join(f"{SecondFolder} {convertimg}.png"))

