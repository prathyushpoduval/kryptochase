N=3
noCops=5
k=5
def allreverse(x):
	return x[::-1]
def halfreverse(x):
	return x[:N][::-1]+x[N:][::-1]
def shiftright(x):
	return x[-1]+x[:-1]
def shiftleft(x):
	return x[1:]+x[0]
def swaps(x):
	return "".join([x[i^1] for i in range(2*N)])
def halfswap(x):
	return x[N:]+x[:N]
def transmitstring(x):
	print(x)
def initialise():
	stringy=raw_input("Initialise")
	return stringy
def receivestring():
	stringy=raw_input("Receive String")
	return stringy
def takeinput():
	stringy=raw_input("Input please senpai")
	return stringy
moveDict={"R":"allreverse","H":"halfreverse","<":"shiftleft",">":"shiftright","S":"swaps","W":"halfswap"}
moveinfoDict={"R":"R","H":"R","<":"H",">":"H","S":"S","W":"S"}
stringprobably=initialise()
currentstring=""
if stringprobably[0]=="T":
	N=int(ord(stringprobably[1])/2)
			indPlayer=int(x[0])
			responses[indPlayer]+=[x]
			if x[1]=="B":
				flag[indPlayer]=1
	win=""
	for i in range(noCops):
		x=responses[i]
		for j in x:
			if j[1]=="A":
				if j[4:]==currentstring:
			indPlayer=int(x[0])
			responses[indPlayer]+=[x]
			if x[1]=="B":
				flag[indPlayer]=1
	win=""
	for i in range(noCops):
		x=responses[i]
		for j in x:
			if j[1]=="A":
				if j[4:]==currentstring:
			indPlayer=int(x[0])
			responses[indPlayer]+=[x]
			if x[1]=="B":
				flag[indPlayer]=1
	win=""
	for i in range(noCops):
		x=responses[i]
		for j in x:
			if j[1]=="A":
				if j[4:]==currentstring:
	currentstring=stringprobably[2:]
else:
	print("WTF")
	exit()
numberOfMoves=1
while True:
	flag=[0 for i in range(noCops)]
	responses=[[] for i in range(noCops)]
	while(0 in flag):
		x=receivestring()
		if x[0]!="T":
			indPlayer=int(x[0])
			responses[indPlayer]+=[x]
			if x[1]=="B":
				flag[indPlayer]=1
	win=""
	for i in range(noCops):
		x=responses[i]
		for j in x:
			if j[1]=="A":
				if j[4:]==currentstring:
			indPlayer=int(x[0])
			responses[indPlayer]+=[x]
			if x[1]=="B":
				flag[indPlayer]=1
	win=""
	for i in range(noCops):
		x=responses[i]
		for j in x:
			if j[1]=="A":
				if j[4:]==currentstring:
					win=str(i)
	if numberOfMoves>=30:
		win="T"
	thiefmove=raw_input()
	message="T"
	if numberOfMoves%k==3:
		message+="B"
	else:
		message+="A"
	if thiefmove[0]=="A":
		print("Not yet!")
		break
	if thiefmove[0]=="B":
		currentstring=eval(moveDict[thiefmove[1]]+"(currentstring)")
		message+=moveinfoDict[thiefmove[1]]
		if numberOfMoves%k==3:
			message+=chr(2*N)
			message+=currentstring
	transmitstring(message)
	message2="TC"
	if win=="":
		message2+="N"
	else:
		message2+="W"
		message2+=win
	transmitstring(message2)
	numberOfMoves+=1
	if win!="":
		break

















