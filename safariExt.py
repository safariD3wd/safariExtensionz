#!/usr/bin/env python
#Description: Download a list of all of the Safari Extensions
# They can later be downloaded, extracted, and analyzed

import urllib2, os, bs4, time, datetime

#getting everything setup
allExts=open('allExts.txt', 'a')

#----------------------------------------------------------
#Get extension to download
#----------------------------------------------------------
url="https://safari-extensions.apple.com/extensions/extensions.json"


get = urllib2.urlopen(url).read()
dom = bs4.BeautifulSoup(get, "html.parser")

downloadURL="https://safari-extensions.apple.com/extensions/"

i = datetime.datetime.now()
dailyCheck=time.strftime("%j")
dailyCheck= str(i.year) + " Day " + dailyCheck + ".txt"

#write data to the file
allExts.write(dom.get_text())
allExts.close()
#open file called allExts.txt
file=open('allExts.txt', 'r')
file2=open(dailyCheck, 'w')

#variables
numL=0
full=""
make=""
url="https://safari-extensions.apple.com/extensions/"


for line in file:
  if "com." in line:
    if numL is 0:
	line = line.lstrip()
	line = line.rstrip()
	make= line[1:-4]
	numL=numL+1
  if "}," in line:
	data=next(file);
	if "date" not in data:
		data=data.lstrip()
		data=data.rstrip()
		make=data[1:-4]

  if "filename" in line:
	line=line.lstrip()
	line=line.rstrip()
	full= line[13:-2]
	file2.write("Download url: ")
	file2.write( url + make + "/" + full)
	file2.write("\n")
  file2.write(line.rstrip())
  file2.write("\n")

file.close()

#removing the file
try:
 os.remove('allExts.txt')
except:
 print
