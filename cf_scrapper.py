import requests
import urllib.request
import os
from bs4 import BeautifulSoup
from shutil import copyfile

# to config 
configPath = "/home/user/" # Directory for save TC contest
pathToTemplate = None # Optional - path to template file Example: /home/io.cpp

if pathToTemplate != None and type(pathToTemplate) is not str:
	print('WARNING, pathToTemplate config must be a string')
elif type(pathToTemplate) is str:
	path_ = pathToTemplate.split('/')
	fileName = path_[len(path_) - 1]
	extension = fileName.split('.')[1]

id_contest = input("Enter contest id: ")
pathContestSolutions = configPath + id_contest


def createFileInDirectory(dir_, content_):
	file_ = open(dir_, 'w')
	file_.writelines(content_)
	file_.close()

def deleteInitialAndEndCRLF(string_):
	l = 0
	r = len(string_)
	if len(string_) > 2:
		if (ord (string_[0]) == 13 or ord (string_[0]) == 10):
			l+=1
		if (ord (string_[r- 1] ) == 13 or ord (string_[r -1]) == 10):
			r-=1
	return string_[l:r]
try:
	url = 'https://codeforces.com/contest/'+ str(id_contest)+ '/problems'
	print('REQUEST TO : ', url)
	response = requests.get(url)
	""" For test 
	outF = open("codeforces.txt", "w")
	outF.writelines(response.text)
	outF.close()
	"""
	if not os.path.exists(pathContestSolutions):
		os.mkdir(pathContestSolutions)
	else:
		print('WARNING :  Already exist contest path directory')
	htmlToScrap = BeautifulSoup(response.content, 'html.parser')
	divproblems = htmlToScrap.find_all('div', class_='problemindexholder')
	problemsLevel = []
	existDirec = False
	for i in divproblems:
		problemsLevel.append(i['problemindex'])
		pathProblem = pathContestSolutions + '/' + i['problemindex'] + '/'
		if not os.path.exists(pathProblem):
			os.mkdir(pathProblem)
		else:
			existDirec = True
		if type(pathToTemplate) is str:
			templateProblem = pathProblem + id_contest + i['problemindex'] + '.' + extension
			copyfile(pathToTemplate, templateProblem )
			print('Template copied:', pathProblem + id_contest + i['problemindex'] + '.' + extension) 
		inputTC = i.find_all('div', class_ ='input')
		problemIndex = 0
		for ii in inputTC:
			problemIndex +=1
			itemInput = ii.find('pre')
			problemInputRaw = itemInput.text
			lines = problemInputRaw.split("\n")
			problemTCFIleName = 'in' + str(problemIndex) + '.txt'
			filepath = os.path.join(pathProblem, problemTCFIleName)
			toWrite = deleteInitialAndEndCRLF(problemInputRaw)
			createFileInDirectory(filepath, toWrite)
		outputTC = i.find_all('div', class_ ='output')
		problemIndex = 0
		for ind, e in enumerate(outputTC):
			itemOutput = e.find('pre')
			problemOutputRaw = itemOutput.text
			lines = problemOutputRaw.split("\n")
			problemFileTCFileName = 'out' + str(ind + 1) + '.txt'
			filepath = os.path.join(pathProblem, problemFileTCFileName)
			toWrite = deleteInitialAndEndCRLF(problemOutputRaw)
			createFileInDirectory(filepath, toWrite)

	print('The problems test cases created in: ' , pathContestSolutions)
	print('id contest : ', id_contest)
	print('PROBLEM LEVELS : ', problemsLevel)

except Exception as e:
	raise e




