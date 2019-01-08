myturn=True
myturntype=0
default="123456"
numcops=5
turnlist=""
def nextCop(a):
	return chr((ord(a)-ord("A")+1)%numcops+ord("A"))
n=len(default)
copStrs=[default]*numcops
xStr=default

movesX=""
def checkwin()
	ans=xStr in copStrs
	index=["BAD COP",(copStrs+[xStr]).index(xStr)][xStr in copStrs]
	if index!="BAD COP":
        copWins(index);
    if turnsRem==0:
		xWin()
def map(x):
	return ord(x)-ord("A")
def msgRecieve(a):
	if a[0]!='X':
		currentCop=a[0]
		if a[0]=='P':
			if a[1]=='G':
				sendMessage("XPG"+xStr[(ord(a[2])-1)])
			else:
				sendMessage("XPM"+MTmind(a[2:],xStr) ) 

		else:
			copStrs[map(currentCop)]=a[2:]
			guiUpdate()
			checkwin()

def sendTurnInfo()
	sendStr="x"
	if reveal():
		sendStr=sendStr+xStr
	else:
		sendStr=sendStr+char(len(turnlist)/2)+turnlist
	sendMessage(sendstr)
	turnEnd()

def cyc1_clicked():
	if(!myturn):
		return
	temp =cyc1(xStr)
	xStr=temp
	checkwin()
	if myturntype!=1:
		turnlist=turnlist+"LC"
	else
		turnlist="BT"
	if myturntype==0:
		sendTurnInfo()
	if myturntype==1:
		sendturnInfo()
	if myturntype==2:
		myturntype=0
	guiUpdate()
def cyc2_clicked():
	if(!myturn):
		return
	temp =cyc2(xStr)
	xStr=temp
	checkwin()
	if myturntype!=1:
		turnlist=turnlist+"RC"
	else
		turnlist="BT"
	if myturntype==0:
		sendTurnInfo()
	if myturntype==1:
		sendturnInfo()
	if myturntype==2:
		myturntype=0
	guiUpdate()
def rev1_clicked():
	if(!myturn):
		return
	temp =rev1(xStr)
	xStr=temp
	checkwin()
	if myturntype!=1:
		turnlist=turnlist+"S1"
	else
		turnlist="BT"
	if myturntype==0:
		sendTurnInfo()
	if myturntype==1:
		sendturnInfo()
	if myturntype==2:
		myturntype=0
	guiUpdate()

def rev2_clicked():
	if(!myturn):
		return
	temp =rev2(xStr)
	xStr=temp
	checkwin()
	if myturntype!=1:
		turnlist=turnlist+"S2"
	else
		turnlist="BT"
	if myturntype==0: 
		sendTurnInfo()
	if myturntype==1:
		sendturnInfo()
	if myturntype==2:
		myturntype=0
	guiUpdate()

def pwpB_clicked():
	if pwpG_playable():
		myturntype=1
def pwp2_clicked():
	if pwp2_playable():
		myturntype=2






		
