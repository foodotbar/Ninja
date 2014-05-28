#!/root/Desktop/workdir/python27/bin/python


import os, tarfile, csv, string, re
import configtest
## sourcePwd is where your rawdata stored
## destinationPwd is where the Processed-data sotred
sourcePwd = configtest.workdir + 'result/'
print sourcePwd
print '****files and dirs need to be processed****'
items = os.listdir(sourcePwd)
print items
filesList = []
#Files under the Dir of result
vmDirList = configtest.VM
# Get the VM list from configure FILE
#vm's dir under the Dir of result

workFlowPattern = configtest.workflow
print "this test Round's work Pattern"
print workFlowPattern

for item in items:
	if item[:2]=='vm':
		#vmDirList.append(item)
		continue
	else:
		filesList.append(item)
print filesList
print vmDirList
vmDirList.sort(key = lambda x:int(filter(str.isdigit, x[2:])))
for filename in filesList:
	if filename[:4]=='boot':
		bootTimeFile = filename
print bootTimeFile
vmSetSize = len(vmDirList)
#vmSetSize is the VM's total number in this test round
print vmSetSize
testHostname =  bootTimeFile.split('.')[1]
#testHostname is the hw's name run the test
#############################         customizedTag = bootTimeFile.split('.')[2]
customizedTag = configtest.PROFILE
#customizedTag is the features about HDD such as SDD or eth's difference
summaryTimeTag = bootTimeFile.split('.')[3]
#summaryTimeTag is the time in the summary CSV File(and the summary File's name segament)
print testHostname
print customizedTag
print summaryTimeTag

reportLocationDir = configtest.workdir + 'report/'
#report's location
print reportLocationDir

#vm 's data will be recored in those list, like vm1_bootTime vm2_bootTime
vmBootTimeList  = []
vmUpTimeList    = []
vmDdNdwList     = []
vmDdDwList      = []
vmDdNdrList     = []
vmDdDrList      = []
vmDdTimeList    = []
vmMysqlRipos    = []
vmMysqlWipos    = []
vmMysqlTimeList = []
vmVideoWrite    = []
vmVideoRanR     = []
vmVideoStriR    = []
vmVideoTimeList = []

###########
# fio raw data will be recored in those lists
vmFioRWList = []
vmFioRWListSon = []
vmFioWList  = []
vmFioWListSon = []
vmFioRList  = []
vmFioRListSon = []
###########
#   Get the boot related time source data
##########
os.chdir(sourcePwd)
print "the boot time related file is here"
print os.getcwd()
#process the 'bootTimeFile' to get the boot time and the up time.
bootTimeFileHandler = open(sourcePwd + bootTimeFile)
lines = bootTimeFileHandler.readlines()
print lines
#lineNumber = len(lines)
lineNumber = len(vmDirList) + 1
print "boot time file should count VM's line"
print lineNumber-1
for line in lines[1:lineNumber]:
	print line
	vmBootTimeList.append(float(line.split()[1]))
	vmUpTimeList.append(float(line.split()[2]))
bootTimeFileHandler.close()
print vmBootTimeList
print vmUpTimeList


####################
#              process the vm's dir to get the DD, MySQL, Video raw data
####################
print os.getcwd()
for vm in vmDirList:
	print vm
	vmProcessPwd = sourcePwd + vm + os.sep
	print vmProcessPwd
	os.chdir(vmProcessPwd)
	print os.getcwd()
	eachVmFileList = os.listdir(os.getcwd())
	print eachVmFileList
	tarFileList = []
	for eachVmFile in eachVmFileList:
		if eachVmFile[-6:] == 'tar.gz':
			tarFileList.append(eachVmFile)
	print tarFileList
	#########
########    tar all the tar.gz file under the vmXX's dir
	#########		
	for tarFile in tarFileList:
		#######
################  add the time into vmMysqlTimeList  vmDdTimeList  vmVideoTimeList
		#######
		if tarFile.split('.')[2] == 'test-videoio':
			vmVideoTimeList.append(tarFile.split('.')[1])
		if tarFile.split('.')[2] == 'test-mysqlfio':
                        vmMysqlTimeList.append(tarFile.split('.')[1])
		if tarFile.split('.')[2] == 'test-dd':
                        vmDdTimeList.append(tarFile.split('.')[1])
		tempSonTar = tarfile.open(os.getcwd() + os.sep + tarFile, 'r|gz')
                tempSonTar.extractall(os.getcwd() + os.sep, members = None)
                tempSonTar.close()
	#############
########	get all the DOT res file's LIST
	#############
	print os.getcwd()
	print "here will print the DOT res FILE"
	vmExtraFileList = os.listdir(os.getcwd())
	vmExtraResFileList = []
	for vmExtraFile in vmExtraFileList:
		if vmExtraFile[-3:] == 'res':
			vmExtraResFileList.append(vmExtraFile)
	print vmExtraResFileList
	for vmExtraResFile in vmExtraResFileList:
		print vmExtraResFile[:-4]	
		if vmExtraResFile[:-4] == 'test-mysqlfio':
			mysqlFile = open(vmExtraResFile)
			mysqllines = mysqlFile.readlines()
			mysqlFlag = 0
			for mysqlline in mysqllines:
				for mysqlword in mysqlline.split():
					if ( mysqlword.find('iops')>-1):
#	print "read / write %d", int(filter(str.isdigit, mysqlword))							
						if ( mysqlFlag == 0):
							vmMysqlRipos.append(int(filter(str.isdigit, mysqlword)))
							mysqlFlag += 1
							break
						if (mysqlFlag == 1):
							vmMysqlWipos.append(int(filter(str.isdigit, mysqlword)))
			mysqlFile.close()
###################################################################
		if vmExtraResFile[:-4] == 'test-dd':
			ddFile = open(vmExtraResFile)
			ddlines = ddFile.readlines()
			ddFlag = 0
			vmDdNdwList.append(float(ddlines[2].split()[-2]))
			vmDdDwList.append(float(ddlines[5].split()[-2]))
			vmDdNdrList.append(float(ddlines[8].split()[-2]))
			vmDdDrList.append(float(ddlines[11].split()[-2]))
			ddFile.close()
#############################################         #####################3
		if vmExtraResFile[:-4] == 'test-videoio':
			videoFile = open(vmExtraResFile)
			videolines = videoFile.readlines()
			videoFlag = 0
			print videolines[-3].split()
			#for videoline in videolines:
			#	for videoword in videoline.split():
			#		if (videoword.find('4096000')>-1):
			#			if (videoFlag == 0):
			#				videoFlag += 1
			#			else:
##							print videoline
			#				vmVideoRanR.append(float(videoline.split()[-3]))
			#				vmVideoStriR.append(float(videoline.split()[-1]))
			vmVideoWrite.append(int(videolines[-3].split()[2]))
			vmVideoRanR.append(int(videolines[-3].split()[-3]))
                        vmVideoStriR.append(int(videolines[-3].split()[-1]))
			videoFile.close()
			
######################################   fio  testResultPrase #####################
		if vmExtraResFile[:-4] == 'test-fiorw':
			vmFioRWListSon.append(vm)
			fioRWFile = open(vmExtraResFile)
			fioRWlines = fioRWFile.readlines()
			for fioRWline in fioRWlines:
				for fioRWword in fioRWline.split():
					if (fioRWword.find('iops=') > -1 ):
						tmptmptmp = (int(filter(str.isdigit, fioRWword)))
						tmptmp = filter(str.isalpha, fioRWline.split()[0]) + ' '+ filter(str.isalpha, fioRWword) + '='
						print tmptmp 	
						print (int(filter(str.isdigit, fioRWword)))
						vmFioRWListSon.append(tmptmp)
						vmFioRWListSon.append(tmptmptmp)
					if (fioRWword.find('lat') > -1 and fioRWline.split()[-1].find('%') > -1 ):
						print fioRWline.split()
						for latWord in fioRWline.split():
							if (latWord.find('=') > -1):
								print latWord.partition('=')
								raioWord = latWord.partition('=')
								vmFioRWListSon.append(raioWord[0] + fioRWline.split()[1])
								vmFioRWListSon.append(raioWord[2])	
		#print vmFioRWListSon
		if len(vmFioRWListSon):
			vmFioRWList.append(vmFioRWListSon)
		vmFioRWListSon = []
		print vmFioRWList

#print vmFioRWList
####################################   fio-w
		if vmExtraResFile[:-4] == 'test-fiow':
			vmFioWListSon.append(vm)
			fioWFile = open(vmExtraResFile)
			fioWlines = fioWFile.readlines()
			for fioWline in fioWlines:
				for fioWword in fioWline.split():
					if (fioWword.find('iops=') > -1 ):
						tmptmptmpW = (int(filter(str.isdigit, fioWword)))
						tmptmpW = filter(str.isalpha, fioWline.split()[0]) + ' '+ filter(str.isalpha, fioWword) + '='
						print tmptmpW 	
						print (int(filter(str.isdigit, fioWword)))
						vmFioWListSon.append(tmptmpW)
						vmFioWListSon.append(tmptmptmpW)
					if (fioWword.find('lat') > -1 and fioWline.split()[-1].find('%') > -1 ):
						print fioWline.split()
						for latWord in fioWline.split():
							if (latWord.find('=') > -1):
								print latWord.partition('=')
								raioWord = latWord.partition('=')
								vmFioWListSon.append(raioWord[0] + fioWline.split()[1])
								vmFioWListSon.append(raioWord[2])	
		#print vmFioWListSon
		if len(vmFioWListSon):
			vmFioWList.append(vmFioWListSon)
		vmFioWListSon = []
		print vmFioWList

###################################################  fio-r
		if vmExtraResFile[:-4] == 'test-fior':
			vmFioRListSon.append(vm)
			fioRFile = open(vmExtraResFile)
			fioRlines = fioRFile.readlines()
			for fioRline in fioRlines:
				for fioRRord in fioRline.split():
					if (fioRRord.find('iops=') > -1 ):
						tmptmptmp = (int(filter(str.isdigit, fioRRord)))
						tmptmp = filter(str.isalpha, fioRline.split()[0]) + ' '+ filter(str.isalpha, fioRRord) + '='
						print tmptmp 	
						print (int(filter(str.isdigit, fioRRord)))
						vmFioRListSon.append(tmptmp)
						vmFioRListSon.append(tmptmptmp)
					if (fioRRord.find('lat') > -1 and fioRline.split()[-1].find('%') > -1 ):
						print fioRline.split()
						for latRord in fioRline.split():
							if (latRord.find('=') > -1):
								print latRord.partition('=')
								raioRord = latRord.partition('=')
								vmFioRListSon.append(raioRord[0] + fioRline.split()[1])
								vmFioRListSon.append(raioRord[2])	
		#print vmFioRListSon
		if len(vmFioRListSon):
			vmFioRList.append(vmFioRListSon)
		vmFioRListSon = []
		print vmFioRList









print "***************this is the result**************of fio *********"
print vmFioRWList
print "**************************"
print vmFioWList
print "*****************************************"
print vmFioRList

fristRow = []
secondRow = []
triRow = []
############### generate a csv file about the detials of fio tests ###########
csvFioFileName = reportLocationDir + 'fiotests.' + str(vmSetSize) + 'vms.'+ summaryTimeTag + '.csv'
csvFioFile = file(csvFioFileName, 'wb')
writerFio = csv.writer(csvFioFile)

for j in range(0, vmSetSize):
	firstRow = vmFioRWList[j][0:5]
	print fristRow 
	writerFio.writerow(firstRow)
	tmpRow = vmFioRWList[j][5::2]
	secondRow = tmpRow
	writerFio.writerow(secondRow)
	triRow = vmFioRWList[j][6::2]
	writerFio.writerow(triRow)
	
	firstRow = vmFioWList[j][0:3]
	print fristRow 
	writerFio.writerow(firstRow)
	tmpRow = vmFioWList[j][3::2]
	secondRow = tmpRow
	writerFio.writerow(secondRow)
	triRow = vmFioWList[j][4::2]
	writerFio.writerow(triRow)
	
	
	firstRow = vmFioRList[j][0:3]
	print fristRow 
	writerFio.writerow(firstRow)
	tmpRow = vmFioRList[j][3::2]
	secondRow = tmpRow
	writerFio.writerow(secondRow)
	triRow = vmFioRList[j][4::2]
	writerFio.writerow(triRow)
csvFioFile.close()

Size = vmSetSize
print testHostname
print customizedTag
print summaryTimeTag
print Size
print vmBootTimeList
print vmUpTimeList
print vmDdTimeList
print vmMysqlTimeList
print vmVideoTimeList
print vmMysqlRipos
print vmMysqlWipos
print vmDdNdwList
print vmDdDwList
print vmDdNdrList
print vmDdDrList
print vmVideoWrite
print vmVideoRanR
print vmVideoStriR
###
###generate the summary file describe this round's test
csvFileName = reportLocationDir + 'summary.' + str(Size) + 'vms.' + summaryTimeTag + '.csv'
csvFile = file(csvFileName, 'wb')
writer = csv.writer(csvFile)
#csvTitleList = ['numberOfVM(s)','avaBootTime(second)','avaUpTime(second)','dd-ndw(MB/s)','dd-dw(MB/s)','dd-ndr(MB/s)','dd-dr(MB/s)','MYSQL-R-ipos','MYSQL-W-ipos','Video-Write','Video-Random-R','Viedo-Stride-R','testHostname','profile']
csvTitleList = ['testHostname','profile','numberOfVM(s)','avaBootTime(second)','avaUpTime(second)']
csvTitleWorkFlowList = []
for workPattern in workFlowPattern:
	if workPattern == 'test-dd':
		csvTitleWorkFlowList.extend(['dd-ndw(MB/s)','dd-dw(MB/s)','dd-ndr(MB/s)','dd-dr(MB/s)'])
	if workPattern == 'test-mysqlfio':
		csvTitleWorkFlowList.extend(['MYSQL-R-ipos','MYSQL-W-ipos'])
	if workPattern == 'test-videoio':
		csvTitleWorkFlowList.extend(['Video-Write','Video-Random-R','Viedo-Stride-R'])
csvTitleList.extend(csvTitleWorkFlowList)
#csvTitleList.extend(['testHostname','profile'])
writer.writerow(csvTitleList)
###
#   ****** Insert the summary_data after the cal~
###
csvDataList = []
csvDataList.append(testHostname)
csvDataList.append(customizedTag)
csvDataList.append(Size)
csvDataList.append(sum(vmBootTimeList)/Size)
csvDataList.append(sum(vmUpTimeList)/Size)

csvDataWorkFlowList = []

for workPattern_1 in workFlowPattern:
        if workPattern_1 == 'test-dd':
                csvDataWorkFlowList.extend([sum(vmDdNdwList)/Size, sum(vmDdDwList)/Size,sum(vmDdNdrList)/Size,sum(vmDdDrList)/Size])
        if workPattern_1 == 'test-mysqlfio':
                csvDataWorkFlowList.extend([sum(vmMysqlRipos)/Size,sum(vmMysqlWipos)/Size])
        if workPattern_1 == 'test-videoio':
                csvDataWorkFlowList.extend([sum(vmVideoWrite)/Size,sum(vmVideoRanR)/Size,sum(vmVideoStriR)/Size])
#csvDataList.append(sum(vmDdNdwList)/Size)
#csvDataList.append(sum(vmDdDwList)/Size)
#csvDataList.append(sum(vmDdNdrList)/Size)
#csvDataList.append(sum(vmDdDrList)/Size)

#csvDataList.append(sum(vmMysqlRipos)/Size)
#csvDataList.append(sum(vmMysqlWipos)/Size)

#csvDataList.append(sum(vmVideoWrite)/Size)
#csvDataList.append(sum(vmVideoRanR)/Size)
#csvDataList.append(sum(vmVideoStriR)/Size)
csvDataList.extend(csvDataWorkFlowList)
#csvDataList.append(testHostname)
#csvDataList.append(customizedTag)
writer.writerow(csvDataList)
##################
csvFile.close()
###
###
csvDetailsFileName = reportLocationDir + 'details.' + str(Size) + 'vms.'+ summaryTimeTag + '.csv'
csvDetailsFile = file(csvDetailsFileName, 'wb')
writerDetails = csv.writer(csvDetailsFile)
#csvDetailsTitleList = ['vmOrder','BootTime(second)','UpTime(second)','dd-ndw(MB/s)','dd-dw(MB/s)','dd-ndr(MB/s)','dd-dr(MB/s)','MYSQL-R-ipos','MYSQL-W-ipos','Video-Write','Video-Random-R','Viedo-Stride-R','testHostname','Profile']
csvDetailsTitleList = ['testHostname','profile','vmName','BootTime(second)','UpTime(second)']
csvDetailsTitleList.extend(csvTitleWorkFlowList)
#csvDetailsTitleList.extend(['testHostname','profile'])
writerDetails.writerow(csvDetailsTitleList)
###
#   ****** Insert the summary_data after the cal~
###
for i in range(0, Size):
	csvDetailsDataList = []
	csvDetailsDataList.append(testHostname)
	csvDetailsDataList.append(customizedTag)
	csvDetailsDataList.append(vmDirList[i])
	csvDetailsDataList.append(vmBootTimeList[i])
	csvDetailsDataList.append(vmUpTimeList[i])

	csvDetailsDataWorkFlowList = []

	for workPattern_2 in workFlowPattern:
        	if workPattern_2 == 'test-dd':
                	csvDetailsDataWorkFlowList.extend([vmDdNdwList[i], vmDdDwList[i],vmDdNdrList[i],vmDdDrList[i]])
        	if workPattern_2 == 'test-mysqlfio':
                	csvDetailsDataWorkFlowList.extend([vmMysqlRipos[i],vmMysqlWipos[i]])
        	if workPattern_2 == 'test-videoio':
                	csvDetailsDataWorkFlowList.extend([vmVideoWrite[i],vmVideoRanR[i],vmVideoStriR[i]])
#	csvDetailsDataList.append(vmDdNdwList[i])
#	csvDetailsDataList.append(vmDdDwList[i])
#	csvDetailsDataList.append(vmDdNdrList[i])
#	csvDetailsDataList.append(vmDdDrList[i])
#	csvDetailsDataList.append(vmMysqlRipos[i])
#	csvDetailsDataList.append(vmMysqlWipos[i])
#	csvDetailsDataList.append(vmVideoWrite[i])
#	csvDetailsDataList.append(vmVideoRanR[i])
#	csvDetailsDataList.append(vmVideoStriR[i])

	csvDetailsDataList.extend(csvDetailsDataWorkFlowList)
#	csvDetailsDataList.append(testHostname)
#	csvDetailsDataList.append(customizedTag)
	writerDetails.writerow(csvDetailsDataList)
csvDetailsFile.close()
