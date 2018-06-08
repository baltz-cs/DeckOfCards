import Deck
#War.py @baltz_jay 2018
d = Deck.Deck()
d.shuffle()

user = []     
cpu = []
userpot = []        
cpupot = []         

def deal():
    global user, cpu, userpot, cpupot
    #deal the cards, even cards to user and odd to cpu
    for eachCard in range(len(d.deck)):
        if eachCard%2 == 0:
            user.insert(0, d.deck[eachCard])
        else:
            cpu.insert(0, d.deck[eachCard])

def flipCard():
    global user, cpu, userpot, cpupot
    userpot.insert(0, user.pop())   
    cpupot.insert(0, cpu.pop())     
    #flip the top card from user and cpu

def compare():
    global user, cpu, userpot, cpupot
    print('User has ' + userpot[0].CardToString() + ' and cpu has ' + cpupot[0].CardToString() + '.')
    if userpot[0].face > cpupot[0].face:
        userWin()
    elif userpot[0].face < cpupot[0].face:
        cpuWin()
    else:
        draw()
    #compare the user card and the cpu card

def userWin():
    global user, cpu, userpot, cpupot
    #user gets both pots
    print('User won')
    for cards in range(len(userpot)):
        user.insert(0, userpot.pop())    
    for cards in range(len(cpupot)):
        user.insert(0, cpupot.pop())
    print('CPU has ' + str(len(cpu)) + ' and User has ' + str(len(user)) + '.')
    
def cpuWin():
    global user, cpu, userpot, cpupot
    #cpu gets both pots
    print('CPU won')
    for cards in range(len(userpot)):
        cpu.insert(0, userpot.pop())
    for cards in range(len(cpupot)):
        cpu.insert(0, cpupot.pop())
    print('CPU has ' + str(len(cpu)) + ' and User has ' + str(len(user)) + '.')

def draw():
    global user, cpu, userpot, cpupot
    #tie should flip 4 cards from each player
    print('War!')
    if len(user) == 3 or len(cpu) == 3:
        flipCard()
        flipCard()
        flipCard()
        compare()
    elif len(user) == 2 or len(cpu) == 2:
        flipCard()
        flipCard()
        compare()
    elif len(user) == 1 or len(cpu) == 1:
        flipCard()
        compare()
    elif len(user) == 0 or len(cpu) == 0:
        if len(user) == 0:
            cpuWin()
            print('CPU won!')
        else:
            userWin()
            print('User won!')
    else:
        flipCard()
        flipCard()
        flipCard()
        flipCard()
        compare()

def newGame():
    global user, cpu, userpot, cpupot
    user = []
    cpu = []
    userpot = []
    cpupot = []
    d.shuffle()
    deal()

def game():
    global user, cpu, userpot, cpupot
    newGame()
    #game loop
    Continue = True
    GameOver = False
    while Continue:
        newGame()
        
        while not GameOver:
            flipCard()
            compare()
            
            if len(user) == 0:
                GameOver = True
            elif len(cpu) == 0:
                GameOver = True
            
            userInput = input('Press enter to continue and Q to quit.').lower()
            print('')
            if userInput == 'q':
                GameOver = True
                
        userInput = input('Enter P to play again and Q to quit.').lower()
        if userInput == 'p':
            Continue = True
            GameOver = False
        elif userInput == 'q':
            Continue = False
