import hashlib
from datetime import datetime
 
 
class Transaction:
    def __init__(self, timestamp, amount, name, prev_hash):
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.amount = amount
        self.name = name
        self.blockdata = str(self.prev_hash) + str(self.timestamp) + self.name + str(self.amount)
        self.hash = hashlib.sha256(bytearray(self.blockdata, "utf-8")).hexdigest()
 
    def verify(previous_block_hash, block_hash):
        return (previous_block_hash == block_hash)
 
 
class Block:
    def __init__(self, transaction, prev_block_hash):
        self.blockdata = transaction
        self.prev_block_hash=prev_block_hash
        self.blockhash = hashlib.sha256(bytearray(self.blockdata, "utf-8")).hexdigest()
 
    def verify(previous_block_hash, block_hash):
        return (previous_block_hash == block_hash)
 
 
# Initializing the Blockchain Variables
i = 0
cnt = 0
blockchain = []
sz = 0
 
msg = """Type 1 to add a transaction.   
       Type 2 to show the blockchain
       Type 3 to show a block
       Type 4 to show a transaction
       Type 5 to check the integrity of the blockchain
       Type 6 to exit"""
 
print(msg)
 
tempchain = []
 
transaction = []
 
unverified = []
verified = []
temphash = ""
integrity = True
 
prevhash = None
 
while (True):
    x = int(input())
    if cnt == 3 and sz > 0:
        z = (int)(sz / 3)-1
        # t = (int)((sz + 1) / 3)
        blockchain.append(Block(temphash, blockchain[z].blockhash))
        t=z+1
        if (Block.verify(blockchain[t].prev_block_hash, blockchain[z].blockhash)):
            integrity = True
        else:
            integrity = False
            break
        prevhash = tempchain[cnt - 1].hash
        tempchain = []
        temphash = ""
        cnt = 0
        sz+=3
        
 
    elif cnt == 3 and sz == 0:
        blockchain.append(Block(temphash, None))
        prevhash = tempchain[cnt - 1].hash
        tempchain = []
        temphash = ""
        cnt = 0
        sz += 3
 
    if (x == 1 and i == 0):
        print("Enter The Amount")
        am = int(input())
        print("Enter your Name")
        name = input()
        transaction.append(Transaction(datetime.now(), am, name, None))
        tempchain.append(Transaction(datetime.now(), am, name, None))
        print(tempchain[cnt].timestamp)
        print(tempchain[cnt].prev_hash)
        print(tempchain[cnt].hash)
        print(tempchain[cnt].amount)
        print(tempchain[cnt].name)
        temphash += str(tempchain[cnt].hash)
        i += 1
        cnt += 1
 
    elif (x == 1 and i > 0 and cnt > 0):
        print("Enter The Amount ")
        am = int(input())
        print("Enter your Name ")
        name = input()
        transaction.append(Transaction(datetime.now(), am, name, tempchain[cnt - 1].hash))
        tempchain.append(Transaction(datetime.now(), am, name, tempchain[cnt - 1].hash))
        if (Transaction.verify(tempchain[cnt].prev_hash, tempchain[cnt - 1].hash)):
            print("Verified")
            verified.append(tempchain[cnt])
        else:
            print("Unverified")
            unverified.append(tempchain[cnt])
            tempchain.pop()
            transaction.pop()
            cnt -= 1
            i -= 1
        print(tempchain[cnt].timestamp)
        print(tempchain[cnt].prev_hash)
        print(tempchain[cnt].hash)
        print(tempchain[cnt].amount)
        print(tempchain[cnt].name)
        temphash += str(tempchain[cnt].hash)
        i += 1
        cnt += 1
 
    elif (x == 1 and i > 0 and cnt == 0):
        print("Enter The Amount ")
        am = int(input())
        print("Enter your Name ")
        name = input()
        transaction.append(Transaction(datetime.now(), am, name, prevhash))
        tempchain.append(Transaction(datetime.now(), am, name, prevhash))
        z = int(sz / 3)
        if (Transaction.verify(tempchain[cnt].prev_hash, prevhash)):
            verified.append(tempchain[cnt])
        else:
            unverified.append(tempchain[cnt])
            tempchain.pop()
            transaction.pop()
            cnt -= 1
            i -= 1
 
        print(tempchain[cnt].timestamp)
        print(tempchain[cnt].prev_hash)
        print(tempchain[cnt].hash)
        print(tempchain[cnt].amount)
        print(tempchain[cnt].name)
        temphash += str(tempchain[cnt].hash)
        i += 1
        cnt += 1
 
    if (x == 6):
        break
 
    if (x == 5):
        if (integrity):
            print("Your blockchain is verified")
        else:
            print("Your blockchain is not verified")
 
    if (x == 3):
        print("Type the block which you want to see")
        p = int(input())
        j = 3 * (p - 1)
        k = j + 3
        print("Details of Block:")
        while j < k:
            print(transaction[j].timestamp)
            print(transaction[j].prev_hash)
            print(transaction[j].hash)
            print(transaction[j].amount)
            print(transaction[j].name)
            j += 1
 
    if (x == 4):
        print("Type the transaction you want to see ")
        y = int(input())
        y=y-1
        print(transaction[y].timestamp)
        print(transaction[y].prev_hash)
        print(transaction[y].hash)
        print(transaction[y].amount)
        print(transaction[y].name)
 
    if (x == 2):
        count = 1
        j = 0
        while j < sz:
            print("Details of Block:", count)
            print(transaction[j].timestamp)
            print(transaction[j].prev_hash)
            print(transaction[j].hash)
            print(transaction[j].amount)
            print(transaction[j].name)
            j += 1
 
            print(transaction[j].timestamp)
            print(transaction[j].prev_hash)
            print(transaction[j].hash)
            print(transaction[j].amount)
            print(transaction[j].name)
            j += 1
 
            print(transaction[j].timestamp)
            print(transaction[j].prev_hash)
            print(transaction[j].hash)
            print(transaction[j].amount)
            print(transaction[j].name)
            j += 1
            count += 1
 
 
if(integrity == False):
    print("Blockchain integrity failed")
 
print("If you want to see the unverified pool, Press 1")
tt = int(input())
if (tt):
    if(len(unverified) == 0):
        print("No unverified transactions")
    else:
        print(unverified)