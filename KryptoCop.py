myturn=True
currentCop="A"
default="123456"
numcops=5
def nextCop(a):
	return chr((ord(a)-ord("A")+1)%numcops+ord("A"))
n=len(default)
copStrs=[default]*numcops
xStr=n*"*"
movesX=""
def xLoses():
	showStringSomehow("You Win")
	gameEnd()

def xWins():
	showStringSomehow("You Lose") 
	gameEnd()
	
def map(x):
	return ord(x)-ord("A")
def msgRecieve(a):
	if a[0]=='X':
		if a[1]=='E':
			if a[2]=='X':
				xWins()
			else:
				xStr=copStrs[map(a[2])]
				guiUpdate()
				xLoses()

		elif a[1]=='P':
				if a[2]=='G':
					 showStringSomehow(a[3] )
				else :
					showStringSomehow("Number of perfectly Matching characters:"+ord(a[3]))
		else:
			if a[2]=='R':
				myturn=True
				movesX=""
				xStr=a[3:]
				guiUpdate()
			else:
				myturn=True
				movesX=movesX+a[4:]
				guiUpdate()
def sendTurnInfo():
	sendMessage(currentCop+char(len(default))+copStrs[map(currentCop)]);
def cyc1_clicked():
	if(!myturn):
		return
	temp =cyc1(copStrs[map[currentCop]])
	sendTurnInfo()
	copStrs[map[currentCop]]=temp
	currentCop=nextCop(currentCop)
	if currentCop=="A":
		myturn=False
	guiUpdate()
def cyc2_clicked():
	if(!myturn):
		return
	temp =cyc2(copStrs[map[currentCop]])
	sendTurnInfo()
	copStrs[map[currentCop]]=temp
	currentCop=nextCop(currentCop)
	if currentCop=="A":
		myturn=False
	guiUpdate()
def rev1_clicked():
	if(!myturn):
		return
	temp =rev1(copStrs[map[currentCop]])
	sendTurnInfo()
	copStrs[map[currentCop]]=temp
	currentCop=nextCop(currentCop)
	if currentCop=="A":
		myturn=False
	guiUpdate()
def rev2_clicked():
	if(!myturn):
		return
	temp =rev2(copStrs[map[currentCop]])
	sendTurnInfo()
	copStrs[map[currentCop]]=temp
	currentCop=nextCop(currentCop)
	if currentCop=="A":
		myturn=False
	guiUpdate()

def pwpG_clicked():
	pwpGrem-=1
	if pwpG_playable():
		a= getNumfromGui()
		sendMessage("PG"+char(a))
def pwpM_clicked():
	pwpMrem-=1
	if pwpM_playable():
		a=getStringfromGui()
		sendMessage("PM"+a)






		