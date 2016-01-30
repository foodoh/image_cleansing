#!/usr/bin/env python

'''
Author = Tasdik Rahman

Scipt to clean the images from any background noise in the best way possible without training pytesser
'''


#### Status : 
'''
Ran successfully on the folder "light_background" 
Stored the cleaned images in "light_cleaned_images"
'''

#### Status

import os 
from PIL import Image

def main() : 
	## defining the directories which we have to work with 
	test_dir = r'/home/tasdik/Dropbox/projects/big_data_project/test'
	images_dir = r'/home/tasdik/Dropbox/projects/big_data_project/test/first_600_restaurants_light'

	## get the list of directories (the hotels) and store it in a list 
	hotels_list = os.listdir('/home/tasdik/Dropbox/projects/big_data_project/test/first_600_restaurants_light')

	## creating the cleaned menu dir if it not exists
	cleaned_images_dir = r'/home/tasdik/Dropbox/projects/big_data_project/test/light_cleaned_images'
	if not os.path.exists(cleaned_images_dir) : 
		os.makedirs(cleaned_images_dir)


	### keeping a list of images which could not be read 
	error_files = test_dir + '/error_files.txt'
	###

	## walking through the files in the directory 
	for hotel in hotels_list : 
		hotel_dir = cleaned_images_dir + '/' + hotel
		## making the directory 
		os.makedirs(hotel_dir)
		print '#'*100
		print '\nchanged the directory to : ' + hotel_dir
		os.chdir(hotel_dir)

		## traversing the particular directory inside the images link
		hotel_images_directory = images_dir + '/' + hotel
		images_list = os.listdir(hotel_images_directory)
		new_images_list = [hotel_images_directory + '/' + x for x in images_list]
		## the above print command will print all the images for the particular hotel name with the absolute paths 

		########################################################################

		'''
		Now to automate the task of cleaning the image
		'''
		### traversing the images list 
		i = 0 

		with open(error_files, 'w') as f : 
			try : 
				for img in new_images_list : 
					image_name = images_list[i]
					new_image_name = image_name[:-4]
					print 'cleaning image : '+image_name

					##############################################
					### Cleaning the image
					## greyscaling the image 

					col = Image.open(img)
					gray = col.convert('L')
					bw = gray.point(lambda x: 0 if x<150 else 250, '1')
					cleaned_image_name = new_image_name + '_cleaned.jpg'
					bw.save(cleaned_image_name)

					##############################################
					i += 1
			except Exception as e : 
				var = img
				f.write(var)
				## this will write a log file about the images which could not be opened and will 
				## append the absolute path to those images in the directory
				f.write('\n')
		########################################################################

if __name__ == '__main__' : 
	main()