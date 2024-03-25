def main():
    try:
        number = int(input("Enter number: "))

        while number != 1:
            number = collatz(number)
    except ValueError:
        print("Not a integer!")


def collatz(number):
    # Checks if number is even
    if number % 2 == 0:
        n = number // 2
    if number % 2 == 1:
        n = 3 * number + 1
    print(n)
    return n


main()
