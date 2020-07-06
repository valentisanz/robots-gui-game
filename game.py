from tkinter import *
from Fighter import *
from Healer import *
from Tank import *
from Kralamar import *
import random
rnd = random.randint(1, 3)
username = 'Player'
if(rnd == 1):
    player1 = Fighter(username)
if(rnd == 2):
    player1 = Healer(username)
if(rnd == 3):
    player1 = Tank(username)
enemy = Kralamar()

# game window settings
main = Tk()
frame = Frame(main, width=600, height=480)
main.resizable(False, False)
main.title('VERSUS')
frame.pack()

# dynamic text
enemyInfo = StringVar()
playerInfo = StringVar()
gameInfo = StringVar()
enemyInfo.set(f'{enemy.name}: {enemy.health} PdV\nPower: {enemy.power}\nMagic: {enemy.magic}')
playerInfo.set(f'{player1.name}: {player1.health} PdV\nType: {player1.type}\nPower: {player1.power}\nMagic: {player1.magic}')
gameInfo.set('Attack or Heal to START')


def playerAttacks(enemy):
    playerResult = player1.attack(enemy)
    enemyResult = enemy.decision(player1)
    enemyInfo.set(f'{enemy.name}: {enemy.health} PdV\nPower: {enemy.power}\nMagic: {enemy.magic}')
    playerInfo.set(f'{player1.name}: {player1.health} PdV\nType: {player1.type}\nPower: {player1.power}\nMagic: {player1.magic}')
    if(enemyResult[0] == '-'):
        gameInfo.set(f'{player1.name} attacks\n{enemy.name}: {playerResult} PdV\n{enemy.name} attacks\n{player1.name}: {enemyResult} PdV')
    else:
        gameInfo.set(f'{player1.name} attacks\n{enemy.name}: {playerResult} PdV\n{enemy.name} heals\n{enemy.name}: {enemyResult} PdV')
    if(player1.health <= 0):
        gameInfo.set(f'{enemy.name} WINS')
    elif(enemy.health <= 0):
        gameInfo.set(f'{player1.name} WINS')


def playerHeals():
    playerResult = player1.heal()
    enemyResult = enemy.decision(player1)
    enemyInfo.set(f'{enemy.name}: {enemy.health} PdV\nPower: {enemy.power}\nMagic: {enemy.magic}')
    playerInfo.set(f'{player1.name}: {player1.health} PdV\nType: {player1.type}\nPower: {player1.power}\nMagic: {player1.magic}')
    if(enemyResult[0] == '-'):
        gameInfo.set(f'{player1.name} heals\n{player1.name}: {playerResult} PdV\n{enemy.name} attacks\n{player1.name}: {enemyResult} PdV')
    else:
        gameInfo.set(f'{player1.name} heals\n{player1.name}: {playerResult} PdV\n{enemy.name} heals\n{enemy.name}: {enemyResult} PdV')
    if(player1.health <= 0):
        gameInfo.set(f'{enemy.name} WINS')
    elif(enemy.health <= 0):
        gameInfo.set(f'{player1.name} WINS')

#def playerAction(*enemy,action):




################################ VIEW ################################
# game info label
infoLabel = Label(frame, bg='yellow', textvar=gameInfo,
                  width='20', height='10', justify='left')
infoLabel.place(x=40, y=40)

# player info label
playerStats = Label(frame, textvar=playerInfo, bd='5',
                    bg='green', justify='left', font=('Courier New', 15))
playerStats.place(x=40, y=273)

# enemy info label
enemyStats = Label(frame, textvar=enemyInfo, bd='5',
                   bg='red', justify='left', font=('Courier New', 15))
enemyStats.place(x=350, y=20)

# attack button
btnAttack = Button(frame, text='Attack', bd='2', bg='red', font=(
    'Courier New', 20, 'bold'), command=lambda: playerAttacks(enemy))
btnAttack.place(x=300, y=360)

# heal button
btnHeal = Button(frame, text='Heal', bd='2', bg='green', font=(
    'Courier New', 20, 'bold'), command=lambda: playerHeals())
btnHeal.place(x=450, y=360)

main.mainloop()
