# importing PIL.Image library and os library
from PIL import Image 
import os

# Deletes old created images if they exist
if os.path.exists("newImage.png"):
	os.remove("newImage.png")

# Prints two blank lines to start our program output
print("\n\n")

# Opens image - Local File in repl.it
img = Image.open('image.jpg')

# Rescale image size down, if needed
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )

#Sorts the image in image.jpg with priority based on user input. The sorted version is saved as a png in newImage.png
def sortColor(color1, color2):
	#Set color3 based on color1 and color2
	if color1==0:
		if color2==1:
			color3= 2
		else:
			color3= 1
	elif col2==0:
		if col1==1:
			color3= 2
		else:
			color3=1
	else:
		color3= 0
	# Creates an ImageCore Object from original image
	pixels = img.getdata()
	# Creates empty array to hold new pixel values
	new_pixels = []
	# For every pixel from our original image, it saves
	# a copy of that pixel to our new_pixels array
	for p in pixels:
		new_pixels.append(p)
	# Starts at the first pixel in the image
	location = 0

	#create lists to hold seperated pixel colors
	newRed=[]
	newGreen=[]
	newBlue=[]
	# Loop through all of new_pixels and seperate the pixel colors into lists newRed newGreen newBlue, where newRed would be an list of the primary color to sort by, 
	# newGreen being the secondary color, and newBlue being the final color
	while location < len(new_pixels):
		# Gets the current color of the pixel at location
		p = new_pixels[location]
		# Splits pixel into red, green and blue component lists
		newRed.append(p[color1])
		newGreen.append(p[color2])
		newBlue.append(p[color3])

		# Changes the location to the next pixel in array
		location = location + 1
	

	#Creates list which will stored sorted components of the newRed, newGreen, and newBlue
	newRed2=[]
	newGreen2=[]
	newBlue2=[]

	#Stores the newRed list sorted increasing in newRed2, the values of newGreen stored increasing with each equal newRed2 value 
	# into newGreen2, and the values of newBlue sorted increasing with each equal newGreen2 into newBlue2. (for [0,8,0,6,6,0,6,7,5,8] as
	# newRed, [5,3,6,2,5,1,2,0,6,2] as newGreen, and [3,4,4,3,1,8,9,3,2,1] as newBlue, the values will be [0,0,0,5,6,6,6,7,8,8]
	# for newRed2, [1,5,6,6,2,2,5,0,2,3] for newGreen2 and [3,4,8,2,3,4,9,3,4,1] for newBlue2)

	#use repetition to check all possible 'red' values (0-255) and add them to newRed2 in order.
	for x in range(0, 256):
		#checks to make sure there is a pixel with value x in newRed 
		if newRed.count(x)>0:
			#creates lists that will store all values 'green' and 'blue' where 'red' has value x
			newTempGreen=[]
			newTempBlue=[]
			#Get the number of values in newRed with value x
			num1=newRed.count(x)
			#store all values 'green' and 'blue' where 'red' has value x through uses of repitition
			for y in range(num1):
				num2=newRed.index(x)
				newRed.pop(num2)
				newTempGreen.append(newGreen.pop(num2))
				newTempBlue.append(newBlue.pop(num2))
			#use repetition to check all possible 'blue' values (0-255) with the same 'red' value and add them to newBlue in order.
			for z in range(0, 256):
				#checks to make sure there is a pixel with value z in newTempBlue 
				if newTempGreen.count(z)>0:
					#create a list that will store values 'blue' where 'red' has value x and 'green' has value z
					newTempBlue2=[]
					#Get the number of values in newRed with value z		
					num3=newTempGreen.count(z)
					#store all values 'blue' where 'red' has value x and 'green' has value z through uses of repitition
					for w in range(num3):
						num4=newTempGreen.index(z)
						newTempGreen.pop(num4)
						newTempBlue2.append(newTempBlue.pop(num4))
					#Sort newTempBlue2
					newTempBlue2.sort()

					#Adds all values where 'red' has value x and 'green' has value z by appending them to the newRed2 and newGreen2 lists
					for r in range(len(newTempBlue2)):
						newRed2.append(x)
						newGreen2.append(z)
					#Add the sorted values of newTempBlue2 to newBlue2.
					newBlue2.extend(newTempBlue2)
			#Print what x value the program is on to show the user relative progress.
			print((str)(x) + "/255")

	#Combine the values of each newRed2, newGreen2, and newBlue2 as pixelsTemp and reassign the values of each respective index
	# of sorted values with the original RGB format into new_pixels
	num5 =0
	while(num5<len(new_pixels)):
		pixelsTemp=[0,0,0]
		for d in range(0,3):
			if d==color1:
				pixelsTemp[d]=(newRed2[num5])
			elif d==color2:
				pixelsTemp[d]=(newGreen2[num5])
			else:
				pixelsTemp[d]=(newBlue2[num5])
		new_pixels[num5]=(pixelsTemp[0], pixelsTemp[1], pixelsTemp[2])
		num5= num5+1
  	# Creates a new image, the same size as the original 
  	# using RGB value format
	newImage = Image.new("RGB", img.size)
  	# Assigns the pixel values to newImage
	newImage.putdata(new_pixels)
 	# Saves the new image file
	newImage.save("newImage.png")
	#Displays the newImage to the user so they don't have to access the file.
	newImage.show()





#Introduce program
print("Hello and welcome to Image Pixel Sorter. You will be able to sort an image based on the color of each pixel or use a predefined image.") 
print("API's and other works cited are commented at the end of the program")
print("\n\n")
test1=(str)("no")
#Check if the image the user wants to sort is in the image.jpg file. 
while not test1=="yes":
	print("Enter yes if you would like to use the predefined image " + " or have changed the image in the image.jpg file to a different jpg image and restarted the program")
	test1= input()

#Get the primarily sort color and set it to integer variable col1. Ask again if not 0-2
col1= (int)(input("What color do you want to primarily sort by? enter  (0 for red, 1 for green, or 2 for blue) "))
while not (col1==0 or col1==1 or col1==2):
	col1= (int)(input("enter (0 for red, 1 for green, or 2 for blue) "))

#Get the primarily sort color and set it to integer variable col1. Ask again if not 0-2 or the same as col1
col2= (int)(input("What color do you want to secondarily sort by? enter (0 for red, 1 for green, or 2 for blue) "))
while col2==col1 or not(col2==0 or col2==1 or col2==2):
	col2= (int)(input("enter either the character 0 for red, 1 for green, or 2 for blue which is not the same as the primary color "))



#Performs the sort with the specified priority colors.
sortColor(col1, col2)


#general information for user.
print("***If the sorted image was not automatically displayed please access the newImage.png. ")
print("I found that this program works best when the image input is .jpg and the output is .png as starting as .jpg is faster ") 
print("and ending in .png has minimal/no loss. Ending with .jpg has noticeable lossy compression and 'static' where ")
print("colors have had their values moved closer to their average and there are 8*8 grids of pixels throughout the image which have ")
print("'random' values. To verify pixel colors I don't recommend paint3D ***")

# Works Cited
# This program uses both the Python os and PIL.Image libraries several times throughout the program
# Code segments from Brian Ford's raster starter code are also used
# The original photo was posted by Bessi on pixabay
