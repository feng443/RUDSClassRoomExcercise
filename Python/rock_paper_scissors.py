from random import choice

def get_win(a, b):
    if a == 'p' and b == 'r':
        return 1
    if a == 'r' and b == 's':
        return 1
    if a == 's' and  b == 'p':
        return 1
myHands = []
for i in range(3):
    h = input("what's hand: ")
    while h not in ['r','p', 'q']:
       h = input("must be r, p or q:")
    myHands.append(h)
print(myHands)
HANDS = ['r', 'p', 'q']
compHands = []

for i in range(3):
    compHands.append(choice(HANDS))

print(compHands)
wins = sum( map(get_win, zip(myHands, compHands)))

if sum(wins) >=2:
    print("I win")
else:
    print("I lost!")
