import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

def dealc():
    deck=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(deck)

def calsum(a):
    sum=0
    for i in range(0,len(a)):
        sum=sum+a[i]
    if sum==21 and len(a)==2:
        return 0
    if sum>21 and 11 in a:
        sum=sum-10

    return sum

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        print("You went over. You lose 😤") 
    if user_score == computer_score:
        print("Draw 🙃") 
    elif computer_score == 0:
        print("Lose, opponent has Blackjack 😱") 
    elif user_score == 0:
        print("Win with a Blackjack 😎") 
    elif user_score > 21:
        print("You went over. You lose 😭") 
    elif computer_score > 21:
        print("Opponent went over. You win 😁") 
    elif user_score > computer_score:
        print("You win 😃") 
    else:
        print("You lose 😤") 


pl=[]
dl=[]
pl.append(dealc())
pl.append(dealc())
dl.append(dealc())
dl.append(dealc())

t= True

while t:
    ps=calsum(pl)
    ds=calsum(dl)
    print(f"User cards: {pl} \n User score: {ps} \n\nDealer cards: {dl[0]}")

    if ps==0 or ds==0 or ps>21:
        t=False
    else:
        nexc=input("Enter y yo get another card: ")
        if nexc=="y":
            pl.append(dealc())
            ps=calsum(pl)
        else:
            t=False
    while ds!=0 and ds < 17:
        dl.append(dealc())
        ds=calsum(dl)

    compare(ps,ds)

