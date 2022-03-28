#Eric Malmström - Star Struck Studios - gruppnummer selector

import random
from tokenize import group

def kolla_name_lista(list,name):
    if name in list:
        return True
    else:
        return False

def main():
    groupNameList = ['AMANDA', 'ANITA', 'ERIC', 'IBRAHIM', 'SAYED', 'CLAUDIA']
    numList = [1,2,3,4,5]
    enteredNameList = []
    randomNumList = []

    nameInList = False

    print("Welcome to the game")
    while(True):
        print('='*15)
        
        while nameInList is False:
            name = str(input("Vad är ditt namn?\n")).upper()
            nameInList = kolla_name_lista(groupNameList,name)

        nameInList = False
        
        groupMemberId = random.choice(numList)
        print(f"Du har fått gruppId nummer {groupMemberId}")
        numList.remove(groupMemberId)
        groupNameList.remove(name)

        enteredNameList.append(name)
        randomNumList.append(groupMemberId)

        print(groupNameList)
        print(numList)

        if len(groupNameList) == 1:
            for count,i in enumerate(enteredNameList):
                
                name = enteredNameList[count]
                id = randomNumList[count]
                print(f"Name: {name}")
                print(f"Group ID number: {id}")
                print('='*15)
            exit()

if __name__ == '__main__':
    main()