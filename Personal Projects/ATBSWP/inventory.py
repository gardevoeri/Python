def main():
    stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}

    displayInventory(stuff)


def displayInventory(inventory):
    print("Inventory: ")

    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v

    print(f"Total number of items: {item_total}")


main()
