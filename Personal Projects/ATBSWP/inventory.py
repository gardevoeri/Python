# def main():
# stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}

# displayInventory(stuff)


def displayInventory(inventory):
    print("Inventory: ")

    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v

    print(f"Total number of items: {item_total}")


def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)

    for i in addedItems:
        for k in inventory.keys():
            if i == k:
                inventory[k] += 1

    return inventory


# main()
