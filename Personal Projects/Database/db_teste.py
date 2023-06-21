import sqlite3

# Create a conection
connection = sqlite3.connect("teste.db")

# Create a cursor
db = connection.cursor()


# Testando a relação de coleta do banco
people = db.execute("SELECT * FROM pessoa")

for person in people:
    if person[2] == "F":
        s = "Mulher"
    else:
        s = "Homem"
    print(f"Nome: {person[0]} | {person[1]} anos | {s}")


# Coletando informações para povoar o banco
nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
sexo = input("Qual o seu sexo: M ou F ? ")


# Testando a relação de inserção no banco
new_person = db.execute(
    "INSERT INTO pessoa (nome, idade, sexo) VALUES (?, ?, ?)", (nome, idade, sexo)
)

print("Agora você faz parte de uma lista de pessoas!")


# Commit the commands to the database
connection.commit()

# Close the connection
connection.close()
