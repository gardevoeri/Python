def main():
    list = [1, 2, 3, 4, 5]

    size = counting(list)
    print(f"The size of the list is {size}")


def counting(l):
    s = 0
    for i in l:
        s += 1
    return s


main()
