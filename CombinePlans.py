#Combine RTML files with different targets into one plan
#
#Example usage: 
#>>python CombinePlans.py StandardStar.rtml Target.rtml
#
#There is no maximum to the number of files that can be combined.

import sys

outputName = "Combined.rtml"

numFiles = len(sys.argv)-1

print (numFiles, 'files to combine')

if numFiles <2:
	raise Exception("At least two filenames must be provided")

#start with fresh file
with open('outputName', 'w'): pass
  
with open('outputName', 'w') as f:
   
	#first file
	filename = sys.argv[1]
	print("Adding", filename)
	file = open(filename, 'r') 
	Lines = file.readlines() 

	for line in Lines: 	
		if '</Request>' in line:
			#exit once we reach the end of the plan
			break
		else:
			#otherwise write it to the output
			f.write(line)
			
	#middle file
	
	for i in range(2, 1+numFiles):
		
		print(i)
		filename = sys.argv[i]
		print("Adding", filename)
		file = open(filename, 'r') 
		Lines = file.readlines() 

		foundPlan = False

		for line in Lines: 
		
			if '<Target ' in line:
				#Found the target tag
				f.write(line)
				foundPlan = True
			elif '</Target>' in line:
				#end of target, write and stop
				f.write(line)
				if i!=numFiles:
					break
			elif foundPlan:
				#otherwise write it to the output
				f.write(line)
				
		
	
