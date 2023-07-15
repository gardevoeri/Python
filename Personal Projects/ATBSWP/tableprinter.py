def main():
    tableData = [
        ["apples", "oranges", "cherries", "banana"],
        ["Alice", "Bob", "Carol", "David"],
        ["dogs", "cats", "moose", "goose"],
    ]

    printTable(tableData)
    return


def printTable(table):
    colWidths = [0] * len(table)

    for i in range(len(table)):
        for j in table[i]:
            if len(j) > colWidths[i]:
                colWidths[i] = len(j)

    for i in range(len(table[0])):
        for j in range(len(table)):
            if j >= 0:
                print(table[j][i].rjust(colWidths[j]), end=" ")
        print()


main()
