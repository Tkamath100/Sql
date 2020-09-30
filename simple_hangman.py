#importing time module
import time

word='s'
name=(input("What\'s your name?   :"))
print(f"Hello {name}")
attempt=5
guess=''
while attempt>0:
    if guess.lower()==word.lower(): 
        print("you won!!!")
        break
    else:
        guess=input("guess one more letter  :")
    attempt-=1
else:
    print("Better luck next time")       
