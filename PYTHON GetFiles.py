import urllib.request
import shutil
import os
import sys


'''
Usage: python GetFiles.py <relase number>

For example: python GetFiles.py 100.5
'''

#Alternate method
#urllib.request.urlretrieve("http://build10:8080/view/BitBucket/job/BB-csoonDB/ws/SourceCode/Content/Procedures", "Asset_GetById.sql")

release_directory="J:\\DB_Releases\\Release "+str(sys.argv[1])

if not (os.path.isdir(release_directory)):
	os.mkdir(release_directory)

scripts=[]
f = open('Database.doc', 'r')
for line in f:
	scripts.append(line)
	
print (str(scripts.__len__())+" files to deploy...\n")

for s in scripts:
	s="http://build10:8080/view/BitBucket/job/BB-csoonDB/ws/SourceCode/"+s
	url=s.replace(" ","%20")
	x= s.rfind('/')
	filename = (s[x+1:-1])
	print(filename)
	with urllib.request.urlopen(url) as response, open (release_directory+"/"+filename,'wb') as out_file:  shutil.copyfileobj(response, out_file)
	
f.close()	
