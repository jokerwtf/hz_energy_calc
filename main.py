from time import sleep

print("Loading")
sleep(0.3)
print('Coded')
sleep(0.3)
print('by')
sleep(0.3)
print('Jok3r - jokerwtf#1337')
sleep(1)
while True:
    missionOne_xp = int(input("Enter mission one XP: "))
    missionOne_ene = int(input("Enter mission one Cost: "))
    missionOne = missionOne_xp / missionOne_ene
    print(missionOne)
    missionTwo_xp = int(input("Enter mission two XP: "))
    missionTwo_ene = int(input("Enter mission two Cost: "))
    missionTwo = missionTwo_xp / missionTwo_ene
    print(missionTwo)
    missionThree_xp = int(input("Enter mission three XP: "))
    missionThree_ene = int(input("Enter mission three Cost: "))
    missionThree = missionThree_xp / missionThree_ene
    print(missionThree)
    sleep(1)
    if missionOne > missionTwo and missionThree:
        print("The best mission to do is number 1")
    elif missionTwo > missionOne and missionThree:
        print("The best mission to do is number 2")
    else:
        print("The best mission to do is number 3")
