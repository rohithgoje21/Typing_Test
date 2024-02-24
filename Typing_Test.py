from time import *
import random
import sys
print('Welcome to Typing Test')
print('----------------------')
print()

sentence_list=[
"George has never traveled with a train", 
"I have never seen a famous person",
"I've visited four of our clients today", 
"I have already ironed the shirts"
]

def Typing(sentence, score, error):
    print()
    print('Your Sentence : ',sentence)
    sleep(1)
    print()
    print("Time starts in..")
    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    sleep(1)
    
    start_time=time()
    userinput= input('Enter now : ')
    end_time=time()
    
    time_diff=round(end_time-start_time,2)
    speed=len(userinput)/time_diff
    wPerSec=round(speed)
    
    check=min(len(userinput),len(sentence))
    for i in range(check):
        if userinput[i]==sentence[i]:
            score+=1
        else:
            error+=1
    sleep(1)       
    print('----------------')
    print('Your score : ',score) 
    print('Errors     : ', error)
    print('Words/sec  : ',wPerSec)
    print('----------------')    
    print()
   

def start():
    sentence=random.choice(sentence_list)
    score=0
    error=0
    Typing(sentence, score, error)




#main...
ch=input("Are you ready...(y/n) ")       
if ch in ['y','Y']:
        sleep(1)
        start()
elif ch in ['n','N']:
        print('Thankyou\n')
        sys.exit()
else:
        print('Error in entering... \n')
        sys.exit()
        
while True:
    ch=input('Want to try again... (y/n) ')
    if ch in ['y','Y']:
        start()
        
    elif ch in ['n','N']:
        print('Thankyou\n')
        break
    else:
        print('Error in entering... \n')
        break