# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems: #iterate over items in addedItems
        if item in inventory.keys(): #check if the item exists in the inventory
            inventory[item] = inventory[item] + 1
        else: #if item does not exist
            inventory.setdefault(item,1) #add 1 quantity of the item to the inventory
    return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        item_total += v
        print(k + ' ' + str(v))

    print("Total number of items: " + str(item_total))


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
stuff = addToInventory(stuff, dragonLoot)

displayInventory(stuff)



