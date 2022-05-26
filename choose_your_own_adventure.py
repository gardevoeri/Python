name = input("Type your name: ")
print("Welcome", name, "to this adventure! ")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Wich way would you like to go? ").lower()

if answer == "left":

    answer = input("You come to a river, you can walk around it os swim accross. Type walk to walk around or swim to swim accross: ")
        
    if answer == "swim":
        print('You swam accross and were eaton by an alligator. You lost the game!')
    elif answer == "walk":
        print('You walked for many miles and ran out of water and died of thirst. You lost the game!')
    else:
        print('Not a valid option. You lose.')

elif answer == "right":

    answer = input('You come to a bridge, it looks wobbly. Do you want to cross it or head back? (cross/back) ')
    if answer == "back":
        print('You went back to the main road and get lost. You lost the game!')
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk do them? (yes/no)").lower()
        if answer == 'yes':
            print('You talk to the stranger and they give you gold. You won the game!')
        
        elif answer == 'no':
            print('You ignore the stranger and they are offended. You lose!')

        else:
            print('Not a valid option. You lose.')

    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')