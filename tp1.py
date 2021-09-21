import hashlib

from datetime import datetime

from hashlib import sha256
import json

class Block:
    def __init__(self,previous_block_hash,timestamp,amount,name):
        self.previous_block_hash = previous_block_hash
        self.timestamp=timestamp
        self.amount=amount
        self.name=name
        self.block_data=str(self.amount)+ "-" +(self.name)+"-"+str(self.timestamp)+ "-" + previous_block_hash
        self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()

    def verify(previous_block_hash,block_hash):    
        return (previous_block_hash==block_hash)


i=0;
blockchain=[]


# if(Block.verify(1,1)): 
#     print("Verified")

blockchain.append(Block("Initial String",datetime.now(),342,"Sahaj"))
i+=1
print(blockchain[0].timestamp)
print(blockchain[0].block_hash)
print(blockchain[0].name) 
print("\n")

print("\n")
# print(i)

while(True):
    x=int(input())

    if(x==1):
        # print(i)
        amount=int(input())
        name=input()
        blockchain.append(Block(blockchain[i-1].block_hash,datetime.now(),amount,name)) 
        
        if(Block.verify(blockchain[i-1].block_hash,blockchain[i].previous_block_hash)):
            print("Verified")

        print(blockchain[i].timestamp)
        print(blockchain[i].block_hash)
        print(blockchain[i].name) 
        print("\n")
        i+=1

    else:
        break    

