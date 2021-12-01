import random
import time
import sys
lives=17
clives=17
ships=0
ships=["🚢","🚤","⛵","⛵","🛶"]
choices=["up","down","left","right"]
ccol_num=[1,2,3,4,5,6,7,8,9,10]
ccol_num2=[1,2,3,4,5,6,7,8,9,10]
pcol_num=[1,2,3,4,5,6,7,8,9,10]
prow_num=["a","b","c","d","e","f","g","h","i","j"]
ship=["carrier","battleship","cruiser","submarine","destroyer"]
placement=[5,4,3,3,2]
cheese=[]
y=[]
z=[]
clist1=[]
clist2=[]
shotletlist=[]
cshotletlist=[]
cshotnumlist=[]
listnum=0
number=0
num2=5
num3=0
num4=2
num5=0
num6=0
compnum=0
shipnum=0

def eprint(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)

bcmap=[[0 for col in range(len(ccol_num))]for row in range(len(ccol_num2))]
for row in range(len(ccol_num2)):
 	for col in range(len(ccol_num)):
 	  bcmap[row][col]="🌊"

cmap=[[0 for col in range(len(ccol_num))]for row in range(len(ccol_num2))]
for row in range(len(ccol_num2)):
    for col in range(len(ccol_num)):
        cmap[row][col]="🌊"
print("\n")

for i in range(5):
	bplacement=random.randint(0,8)
	bplacement2=random.randint(0,8)
	clist1.append(bplacement)
	clist2.append(bplacement2)
		
	for i in range(placement[num6]):
		thing=random.randint(0,3)
		choice=choices[thing]
		for i in range(placement[num6]):
			if choice=="right":
				cmap[clist1[num6]][clist2[num6]+1]="🚢"
			if choice=="left":
				cmap[clist1[num6]][clist2[num6]-1]="🚢"
			if choice=="up":
				cmap[clist1[num6]+1][clist2[num6]]="🚢"
			if choice=="down":
				cmap[clist1[num6]-1][clist2[num6]]="🚢"
	num6=num6+1

#for row in range(len(ccol_num)):
	#print("".join(cmap[row]))
eprint("Welcome to battleships soldier!\nPlace your ships then attack the enemy!\nTry not to die first!\n\n")
eprint("by the way i think i got the coordinates the wrong way round so numbers are vertically and letters are horizontally, thanks!")



pmap=[[0 for col in range(len(pcol_num))]for row in range(len(prow_num))]
for row in range(len(prow_num)):
    for col in range(len(pcol_num)):
        pmap[row][col]="🌊"
print("\n")
for row in range(len(prow_num)):
	print("".join(pmap[row]))


for i in range(5):
	print("\nyou have",num2,"ships to place!\none carrier(5), one battleship(4), one cruiser(3), one submarine(3) and one destroyer(2)")
	print("where do you want to place your",ship[number]+"?\n")					
	xplace=int(input("choose a number between 1 and 10: "))
	if xplace not in pcol_num:
		print("im sorry that number was over/under 1 or 10!\nByeeeeeeee")
		quit()
	else:
		cheese.append(xplace-1)
		yplace=input("choose a letter between A and J: ").lower()
		y.append(yplace)
		for x in y:
			z.append(ord(x)-97)
		[int(i) for i in z]
		[int(i) for i in cheese]
		print("would you like to place the",ship[number],"horizontally(h) or vertically(v)?")
		horv=input("")
		if horv=="h":
			for i in range(placement[number]):
				if pmap[cheese[number]][z[num3]]=="🚢"or pmap[cheese[number]][z[num3]]=="🚤"or pmap[cheese[number]][z[num3]]=="⛵"or pmap[cheese[number]][z[num3]]=="⛵"or pmap[cheese[number]][z[num3]]=="🛶":
					print("that space already has a boat on it, sorry\ni havent coded the restart yet soooooooo")
					exit()
				else:
					pmap[cheese[number]][z[num3]]=ships[shipnum]
					z[num3]=z[num3]+1

		elif horv=="v":
			for i in range(placement[number]):
				if pmap[cheese[number]][z[num3]]=="🚢"or pmap[cheese[number]][z[num3]]=="🚤"or pmap[cheese[number]][z[num3]]=="⛵"or pmap[cheese[number]][z[num3]]=="⛵"or pmap[cheese[number]][z[num3]]=="🛶":
					print("that space already has a boat on it, sorry\ni havent coded the restart yet soooooooo")
					exit("good luck lol")
				else:
					pmap[cheese[number]][z[num3]]=ships[shipnum]
					cheese[number]=cheese[number]+1

		for row in range(len(prow_num)):
			print("".join(pmap[row]))
		number=number+1
		num2=num2-1
		num3=num3+num4
		num4=num4+1
		shipnum=shipnum+1

print("\ntime to play, you will go then the computer will go, try your best!")

while lives!=0 or clives!=0:
	shotnum=int(input("choose a number between 1 and 10 to hit: "))
	shotlet=input("choose a letter between A and J to hit: ")
	for j in shotlet:
		shotletlist.append(ord(j)-97)
	[int(i) for i in shotletlist]

	if cmap[shotnum-1][shotletlist[compnum]] =="🚢":
		print("you hit a ship\n")
		clives=clives-1
		bcmap[shotnum][shotletlist[compnum]] ="🔥"
		print("the computer map is now:")
		for row in range(len(prow_num)):
			print("".join(bcmap[row]))
		time.sleep(2)

		print("your map is now:")
		for row in range(len(prow_num)):
			print("".join(pmap[row]))
		time.sleep(2)

	elif cmap[shotnum-1][shotletlist[compnum]] =="🌊":
		print("you did not hit a ship\n")
		bcmap[shotnum][shotletlist[compnum]] ="❌"
		print("the computer map is now:")
		for row in range(len(prow_num)):
			print("".join(bcmap[row]))
		time.sleep(2)

		print("your map is now:")
		for row in range(len(prow_num)):
			print("".join(pmap[row]))
		time.sleep(2)
	
	
	cshotnum=random.randint(0,9)
	cshotlet=random.randint(0,9)
	#cshotnum=0
	#cshotlet="a"
	cshotletlist.append(cshotlet)
	cshotnumlist.append(cshotnum)

	if pmap[cshotnumlist[compnum]][cshotletlist[compnum]] =="🚢":
		print("\nthe computer is deciding...")
		time.sleep(2)
		print("the computer hit your ship!!")
		pmap[cshotnum][cshotletlist[compnum]] ="🔥"
		for row in range(len(prow_num)):
			print("".join(pmap[row]))
		compnum=compnum+1
			
	elif pmap[cshotnumlist[compnum]][cshotletlist[compnum]] =="🌊":
		print("\nthe computer is deciding...")
		time.sleep(2)
		print("the computer missed your ship!!\n")
		pmap[cshotnum][cshotletlist[compnum]] ="❌"
		for row in range(len(prow_num)):
			print("".join(pmap[row]))
		compnum=compnum+1

	else:
		cshotnum=random.randint(0,9)
		cshotlet=random.randint(0,9)
		if pmap[cshotnumlist[compnum]][cshotletlist[compnum]] =="🚢":
			print("the computer is deciding...")
			time.sleep(2)
			print("the computer hit your ship!!")
			pmap[cshotnum][cshotletlist[compnum]] ="🔥"
			for row in range(len(prow_num)):
				print("".join(pmap[row]))
			compnum=compnum+1
			
		elif pmap[cshotnumlist[compnum]][cshotletlist[compnum]] =="🌊":
			print("the computer is deciding...")
			time.sleep(2)
			print("the computer missed your ship!!\n")
			pmap[cshotnum][cshotletlist[compnum]] ="❌"
			for row in range(len(prow_num)):
				print("".join(pmap[row]))
			compnum=compnum+1
		
	
		
	
	


print ("")
