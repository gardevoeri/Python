import inventory


def main():
    inv = {"gold coin": 42, "rope": 1}
    dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

    # Decidi colocar no mesmo arquivo de inventory
    inv = inventory.addToInventory(inv, dragonLoot)

    inventory.displayInventory(inv)


main()
