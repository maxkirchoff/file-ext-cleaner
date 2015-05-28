#!/usr/bin/env python
import os, sys, time


def extMatcher(ext):
	# we're not including the . (period) in the ext name list
	matchExtensions = ['jpg','jpeg','png','gif','css','js']
	# slice them without the . (period)
	if (ext[1:3] in matchExtensions): 
		# return with the period
		return ext[:3]
	if (ext[1:4] in matchExtensions): 
		return ext[:4]
	if (ext[1:5] in matchExtensions): 
		return ext[:5]
	return

def runType():
	if (len(sys.argv) > 1):
	 	if (sys.argv[1] == "--please"):
			print "This is a LIVE run. Files will be changed. Hit INTERRUPT to abort."
			return "rename"
	print "This is a test run. No files will be changed. Run this script with the '--please' flag to actually rename all the files."
	return


paths = (os.path.join(root, filename) for root, _, filenames in os.walk('.') for filename in filenames)
run = runType()
#give them a chance to read the message
time.sleep(10)
for path in paths:
    fileName, fileExtension = os.path.splitext(path)
    extMatched = extMatcher(fileExtension)
    if (extMatched and (extMatched != fileExtension)):
    	print "\n"
    	print "Original file path: " + path
    	print "New file path: " + fileName + extMatched
    	print "Removed from extension name: " + fileExtension[len(extMatched):]
    	if (run == "rename"):
    		os.rename(path, fileName + extMatched)
