import os, tarfile, csv, string, re

## sourcePwd is where your rawdata stored
## destinationPwd is where the Processed-data sotred
sourcePwd = '/root/Downloads/rawdata.tar.gz'
destinationPwd = '/var/tmp'
dirVar = '/root/Downloads/'
print '****no sub dir****'
files = os.listdir(dirVar)

def tarProcessor(tarTempFile):
	tarFileHandler = tarfile.open(tarTempFile, 'r|gz')
	tarFileHandler.extractall(destinationPwd, members = None)
	filenamelist = tarFileHandler.getnames()
	filenamelistTmp = []


	for name_ in filenamelist:		
		tempSonTar = tarfile.open(destinationPwd + os.sep + name_, 'r|gz')
		tempSonTar.extractall(destinationPwd + os.sep + name_[:-7] + os.sep, members = None)  
		filenamelistTmp.append(name_[:-7])
		tempSonTar.close()
	tarFileHandler.close()	
	return filenamelistTmp 

csvSourceList = tarProcessor(sourcePwd)
print len(csvSourceList)
rePattern = re.compile(r'(\d{1,2}vm)')
tempList = []
for itemTmp in csvSourceList:
	tempListNode = rePattern.split(itemTmp)[2]	
	print itemTmp
	print tempListNode
	tempList.append(tempListNode)
patternSet = set(tempList)
print patternSet
patternList = list(patternSet)
print patternList
for patternItem in patternList:
	tempRunList = []
	tempDataList2csv = []
	csvFileName = '/var/tmp/' + patternItem + '.csv'
	csvFile = file(csvFileName, 'wb')
	writer = csv.writer(csvFile)
	csvTitleList = ['numberOfVM(s)','avaBootTime(second)','avaUpTime(second)','dd-ndw(MB/s)','dd-dw(MB/s)','dd-ndr(MB/s)','dd-dr(MB/s)','MYSQL-R-ipos','MYSQL-W-ipos','Video-Reclen','Viedo-Stride-R']
        writer.writerow(csvTitleList)
	csvSourceList.sort(key=lambda x:int(filter(str.isdigit, x[:2])))
	print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$this is the csvSourceList", csvSourceList
	for diff in csvSourceList:
		pathWay = destinationPwd + os.sep + diff +'/result/'
		if( diff.find(patternItem) > 0 ):
			print diff, "-----------------------------------"
			#pathWay = destinationPwd + os.sep + diff +'/result/'
			print pathWay
			os.chdir(pathWay)
			firstDirList =  os.listdir(pathWay)
			#bootTimeFile = ''
##			print firstDirList
			for firstDirItem in firstDirList:
				subStr = 'boot'
				if ( firstDirItem.find(subStr) > -1 ):
					bootTimeFile = firstDirItem
					file_path = pathWay + bootTimeFile
##					print file_path
					bootTimeFile = open(file_path)
					lines = bootTimeFile.readlines()
					lineNumber = len(lines)
					print lineNumber-1
					bootTimeTotal_ = 0.0
					upTimeTotal_ = 0.0
					for line in lines[1:lineNumber]:
##						print line
						bootTimeTotal_ += float(line.split()[1])
						upTimeTotal_ +=  float(line.split()[2])
					tempRunList.append(lineNumber-1)
					print "avage boot time", bootTimeTotal_/(lineNumber-1)
					tempRunList.append(bootTimeTotal_/(lineNumber-1))
					tempRunList.append(upTimeTotal_/(lineNumber-1))
					print "avage up time", upTimeTotal_/(lineNumber-1)	
					bootTimeFile.close()
			vmNumbers = int(filter(str.isdigit, diff[:2]))
			print vmNumbers
			vmDirList = []
			for ii in range(1,vmNumbers+1):
				if ii<10:
					vmDirList.append('0'+str(ii))
				else:
					vmDirList.append(str(ii))
##			print vmDirList
			totalDdNdw = 0
			totalDdDw = 0
			totalDdNdr = 0
			totalDdDr =0
			totalMysqlRead = 0
			totalMysqlWrite = 0
			totalVideoReclen = 0
			totalVideoLast = 0
			print "####################################this is vmDirList", vmDirList
			for vm in vmDirList:
				vmPathWay = pathWay + 'vm' + vm + os.sep
##				print vmPathWay
				eachVMDataList = os.listdir(vmPathWay)
##				print eachVMDataList
				for eachVMData in eachVMDataList:
					eachVMDataItem = vmPathWay + eachVMData
					tarEachVMDataItem = tarfile.open(eachVMDataItem,'r|gz')
					tarEachVMDataItem.extractall(vmPathWay, members = None)
					#filenamelistOfEachVMDataItem = tarEachVMDataItem.getnames()
					#print filenamelistOfEachVMDataItem
					tarEachVMDataItem.close()
				itemListUnderVMDir = os.listdir(vmPathWay)
##				print itemListUnderVMDir
				for itemUnderVMDir_ in itemListUnderVMDir:
					if ( itemUnderVMDir_.find('test-mysqlfio.res') > -1):
						mysqlBenFilePath = vmPathWay + itemUnderVMDir_
						mysqlFile = open(mysqlBenFilePath)
						mysqllines = mysqlFile.readlines()
						mysqlFlag = 0
						for mysqlline in mysqllines:
							for mysqlword in mysqlline.split():
								if ( mysqlword.find('iops')>-1):
								#	print "read / write %d", int(filter(str.isdigit, mysqlword))							
									if ( mysqlFlag == 0):
										totalMysqlRead += int(filter(str.isdigit, mysqlword))
										mysqlFlag += 1
										break
									if (mysqlFlag == 1):
										totalMysqlWrite += int(filter(str.isdigit, mysqlword))
#for the dd process from here
				#for itemUnderVMDir_ in itemListUnderVMDir:
					if ( itemUnderVMDir_.find('test-dd.res') > -1):
						ddBenFilePath = vmPathWay + itemUnderVMDir_
						ddFile = open(ddBenFilePath)
						ddlines = ddFile.readlines()
						ddFlag = 0
						totalDdNdw += float(ddlines[0].split()[-2])
						totalDdDw += float(ddlines[1].split()[-2])
						totalDdNdr += float(ddlines[2].split()[-2])
						totalDdDr += float(ddlines[3].split()[-2])
# process the dd , until here

# process the video from here
					if ( itemUnderVMDir_.find('test-videoio.res') > -1):
						videoFilePath = vmPathWay + itemUnderVMDir_
						videoFile = open(videoFilePath)
						videolines = videoFile.readlines()
						videoFlag = 0
						for videoline in videolines:
							for videoword in videoline.split():
								if (videoword.find('4096000')>-1):
									if (videoFlag == 0):
										videoFlag += 1
									else:
##										print videoline
										totalVideoReclen += float(videoline.split()[1])
										totalVideoLast += float(videoline.split()[-1])
                                               				#totalVideoReclen += float(videoDataLine[0])
                                                			#totalVideoLast += float(videoDataLine[-1])
							
# process the video stop here
			print "avage Mysql Read iops" ,totalMysqlRead/vmNumbers
			print "avage Mysql Write iops", totalMysqlWrite/vmNumbers
			#print "avage Dd "totalDdNdw, totalDdDw, totalDdNdr, totalDdDr
			print "no direct write: %f MB/s", (totalDdNdw/vmNumbers)
			print "direct write: %f MB/s", (totalDdDw/vmNumbers)
			print "no direct read: %f MB/s", (totalDdNdr/vmNumbers)
			print "direct read: %f MB/s", (totalDdDr/vmNumbers)
			print "video reclen", float(totalVideoReclen/vmNumbers)
			print "video xx read", float(totalVideoLast/vmNumbers)
			tempRunList.append(totalDdNdw/vmNumbers)
			tempRunList.append(totalDdDw/vmNumbers)
			tempRunList.append(totalDdNdr/vmNumbers)
			tempRunList.append(totalDdDr/vmNumbers)
			tempRunList.append(totalMysqlRead/vmNumbers)
			tempRunList.append(totalMysqlWrite/vmNumbers)
			tempRunList.append(totalVideoReclen/vmNumbers)
			tempRunList.append(totalVideoLast/vmNumbers)
			tempDataList2csv.append((lineNumber-1,float('%.2f'%(bootTimeTotal_/(lineNumber-1))),float('%.2f'%(upTimeTotal_/(lineNumber-1))),float('%.2f'%(totalDdNdw/vmNumbers)),float('%.2f'%(totalDdDw/vmNumbers)),float('%.2f'%(totalDdNdr/vmNumbers)),float('%.2f'%(totalDdDr/vmNumbers)),(totalMysqlRead/vmNumbers),(totalMysqlWrite/vmNumbers),(totalVideoReclen/vmNumbers),float('%.2f'%(totalVideoLast/vmNumbers))))
			#writer.writerows(tempDataList2csv)
	print "****different pattern******************************************"
	writer.writerows(tempDataList2csv)
	csvFile.close()

	
