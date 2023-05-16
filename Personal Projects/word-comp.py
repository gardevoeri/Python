while True:
    try:
        size = int(input("Quantas palavras você quer comparar? "))
        if size < 2:
            print("Escolha pelo menos duas palavras.")
        else:
            print(f"Palavras Comparadas = ", size)
            break
    except:
        print("Por favor digite um número válido!")


words = []

while len(words) < size:
    word = input("Informe uma palavra: ")
    if len(word) < 2:
        print("Digite uma palavra válida!")
    else:
        words.append(word)


word_counting = {}
for word in words:
    word_counting[word] = len(word)

# ver o que é esse __getitem__ - descobri como usar o sorted online, não sei pra q isso serve.
sorted_words = sorted(words, key=word_counting.__getitem__)

smaller = sorted_words[0]
bigger = sorted_words[len(sorted_words) - 1]

print(f"A maior palavra é: {bigger}, com {len(bigger)} letras")
print(f"A menor palavra é: {smaller}, com {len(smaller)} letras")
