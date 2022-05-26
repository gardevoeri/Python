print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()
    
print("Okay! Let's Play!")
score = 0

answer = input("What is a banana? ")
if answer.lower() == "fruit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is a giraffe? ")
if answer.lower() == "animal":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is a willow ? ")
if answer.lower() == "tree":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is wine? ")
if answer.lower() == "drink":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " quesntions correct!")
print("You got " + str((score / 4) * 100) + "%.")

#colocar o if pra outros tipos de resposta incorretas
#colocar alerta de erro pra respostas incorretas
#colocar as respostas em multipla escolha


