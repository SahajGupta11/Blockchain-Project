import datetime
import hashlib
from datetime import datetime
from hashlib import sha256
 
class Block:
	def __init__(self, timestamp,amount,name,prev_hash):
		self.timestamp = timestamp
		self.prev_hash = prev_hash  
		self.amount=amount
		self.name=name
		self.blockdata=str(self.prev_hash) + str(self.timestamp) + self.name + str(self.amount)
		self.hash=hashlib.sha256(bytearray(self.blockdata, "utf-8")).hexdigest()
   
	def verify(previous_block_hash,block_hash):    
		return (previous_block_hash==block_hash)
 
 
#Initializing the Blockchain Variables
i=0
cnt=0
blockchain=[]
sz=0
 
msg="""Type 1 to add a transaction.   
       Type 2 to show the blockchain
       Type 4 to show a block
       Type 5 to exit"""
 
print(msg)
 
tempchain=[]
 
unverified=[]
verified=[]
 
prevhash=None
 
while(True):
	x=int(input())
	if cnt==3:
		blockchain.append(tempchain)
		prevhash=tempchain[cnt-1].hash
		tempchain=[]
		cnt=0
		sz+=3

	if(x==1 and i==0):
		print("Enter The Amount")
		am=int(input())
		print("Enter your Name") 
		name=input()
		tempchain.append(Block(datetime.now(),am,name,None)) 
		print(tempchain[cnt].timestamp)
		print(tempchain[cnt].prev_hash)
		print(tempchain[cnt].hash)
		print(tempchain[cnt].amount)
		print(tempchain[cnt].name)
		i+=1
		cnt+=1

	elif(x==1 and i>0 and cnt>0):
		print("Enter The Amount ")
		am=int(input())
		print("Enter your Name ") 
		name=input()
		tempchain.append(Block(datetime.now(),am,name,tempchain[cnt-1].hash)) 
		if(Block.verify(tempchain[cnt].prev_hash,tempchain[cnt-1].hash)):
			verified.append(tempchain[cnt])
		else:
			unverified.append(tempchain[cnt])
			tempchain.pop()
			cnt-=1
			i-=1
		print(tempchain[cnt].timestamp)
		print(tempchain[cnt].prev_hash)
		print(tempchain[cnt].hash)
		print(tempchain[cnt].amount)
		print(tempchain[cnt].name)
		i+=1
		cnt+=1

	elif(x==1 and i>0 and cnt==0):
		print("Enter The Amount ")
		am=int(input())
		print("Enter your Name ") 
		name=input()
		tempchain.append(Block(datetime.now(),am,name,prevhash)) 
		z=int(sz/3)
		if(Block.verify(tempchain[cnt].prev_hash,prevhash)):
			verified.append(tempchain[cnt])
		else:
			unverified.append(tempchain[cnt])
			tempchain.pop()
			cnt-=1
			i-=1


		print(tempchain[cnt].timestamp)
		print(tempchain[cnt].prev_hash)
		print(tempchain[cnt].hash)
		print(tempchain[cnt].amount)
		print(tempchain[cnt].name)
		i+=1
		cnt+=1

	if(x==5):
		break

	if(x==4):
		print("Type the block you want to see ")
		y=int(input())
		if(y<=sz):
			y-=1
			z=int(y/3)
			a=y%3
			print(blockchain[z][a].timestamp)
			print(blockchain[z][a].prev_hash)
			print(blockchain[z][a].hash)	
			print(blockchain[z][a].amount)	
			print(blockchain[z][a].name)

		elif(y>sz and y<=sz+cnt):
			y-=1
			z=int(y/3)
			a=y%3    	
			print(tempchain[a].timestamp)
			print(tempchain[a].prev_hash)
			print(tempchain[a].hash)	
			print(tempchain[a].amount)	
			print(tempchain[a].name)
	if(x==2):
		count=1
		for ele in blockchain:
			print("Details of Block:",count)
			print(ele[0].timestamp)
			print(ele[0].prev_hash)
			print(ele[0].hash)	
			print(ele[0].amount)	
			print(ele[0].name)

			print(ele[1].timestamp)
			print(ele[1].prev_hash)
			print(ele[1].hash)	
			print(ele[1].amount)	
			print(ele[1].name)

			print(ele[2].timestamp)
			print(ele[2].prev_hash)
			print(ele[2].hash)	
			print(ele[2].amount)	
			print(ele[2].name)
			count+=1
