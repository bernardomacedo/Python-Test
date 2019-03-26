import sys

sys.setrecursionlimit(50000)

imageDefined = False
processingVector = []

def resetImage():
	global imageVector
	global M
	global N
	global imageDefined
	imageVector = [["O" for x in range(M)] for y in range(N)]

	imageDefined = True

def processPixel(X, Y, C, oldC):
	global M
	global N
	global processingVector
	# lets check if the current pixel was processed
	if ([X, Y] not in processingVector):
		processingVector.append([X,Y])
		if (imageVector[X][Y] == oldC):
			# lets change this pixel color
			imageVector[X][Y] = C
			# these 4 functions will prevent infinite recursion
			# if there is only one function to process all, it will create an infinite loop of pixels evaluation
			if (X-1 >= 0):
				processPixel(X-1, Y, C, oldC)
			if (X+1 < N):
				processPixel(X+1, Y, C, oldC)
			if (Y-1 >= 0):
				processPixel(X, Y-1, C, oldC)
			if (Y+1 < M):
				processPixel(X, Y+1, C, oldC)

def main():
	global imageDefined
	global imageVector
	global M
	global N
	# this will be the instance of the array being ccreated to store the colours
	
	# the program will ask for the 

	com = raw_input('>')
	com = com.split(" ") # split the command so we can process the rest

	if (com[0] == "C"):
		# clears the content of the image
		resetImage()

	elif com[0] == "I":
		if ((com[1].isdigit()) and (com[2].isdigit()) and (int(com[2]) >= 1) and (int(com[2]) <= 250) and (int(com[1]) >= 1) and (int(com[1]) <= 250)):
			M = int(com[1])
			N = int(com[2])
			resetImage()
		else:
			print("Input parameters are incorrect")
		

	elif com[0] == "L":
		# add validators so the program does not explode
		if (not imageDefined):
			print("There is no image defined")
		else:
			if ((com[1].isdigit()) and (com[2].isdigit()) and (com[3].isupper())):
				X = int(com[1])-1 # column
				Y = int(com[2])-1 # initial line
				C = com[3] # color
				imageVector[Y][X] = C
			else:
				print("Input parameters are incorrect")

	elif com[0] == "V":
		if (not imageDefined):
			print("There is no image defined")
		else:
			if ((com[1].isdigit()) and (com[2].isdigit()) and (com[3].isdigit()) and (com[4].isupper())):
			    # here we will expect a column X
			    X = int(com[1])-1 # column
			    Y1 = int(com[2])-1 # initial line
			    Y2 = int(com[3])-1 # finish line
			    C = com[4] # color

			    #@TODO double check if these indexes exist

			    for i in range(len(imageVector)):
			    	for j in range(len(imageVector[i])):
			    		if (j == X): # column
			    			if ((i >= Y1) and (i <= Y2)): # Line
			    				imageVector[i][j] = C
			else:
				print("Input parameters are incorrect")

	elif com[0] == "H":
		if (not imageDefined):
			print("There is no image defined")
		else:
			if ((com[1].isdigit()) and (com[2].isdigit()) and (com[3].isdigit()) and (com[4].isupper())):
			    # here we will expect a column X
			    X1 = int(com[1])-1 # column start
			    X2 = int(com[2])-1 # column end
			    Y = int(com[3])-1 # line
			    C = com[4] # color

			    for i in range(len(imageVector)):
			    	for j in range(len(imageVector[i])):
			    		if (i == Y):
			    			if ((j >= X1) and (j <= X2)):
			    				imageVector[i][j] = C
			else:
				print("Input parameters are incorrect")

	elif com[0] == "F":
		if (not imageDefined):
			print("There is no image defined")
		else:
			if ((com[1].isdigit()) and (com[2].isdigit()) and (com[3].isupper())):
				global processingVector
				X = int(com[1])-1
				Y = int(com[2])-1
				C = com[3]
				processingVector = []

				oldC = imageVector[Y][X] # get old color to compare
				processPixel(Y,X,C,oldC)

				# empty the global processing vector
				processingVector = []
			else:
				print("Input parameters are incorrect")

	elif com[0] == "S":
		if (not imageDefined):
			print("There is no image defined")
		else:
			imageLine = []
			print ""
			print "=>"
			# display the contents of the image
			for i in range(len(imageVector)):
				for j in range(len(imageVector[i])):
					imageLine.append(imageVector[i][j])
				print ''.join(imageLine)
				imageLine = []
			print ""
	elif com[0] == "X":
		# let's stop the program execution
		print("Bye bye")
		exit()
	else:
		print("Command not found")

if __name__=="__main__":
	while True:
		main()