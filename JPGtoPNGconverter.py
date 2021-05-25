import sys
import os
from PIL import Image, ImageFilter

# grab first and the second document
image_folder = sys.argv[1]
output_folder = sys.argv[2]
#check if new folder exists and create it if not
if not os.path.exists(output_folder):
	print(f'{output_folder} does not exist, creating new file')
	new_dir = output_folder
	os.makedirs(new_dir)
else:
	print(f'{output_folder} folder already exists')
#loop through pokedex
#convert images to png
#save the new folder
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}\\{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{output_folder}\\{clean_name}.png','png')
	print('all done!')