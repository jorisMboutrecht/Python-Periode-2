player_name = input("voor je speler naan in: ")
player_gold = 100
inventory = []
# item, kost, max1 is 1,
shop_item = [
    ["Sword", 50, 1],
    ["Shield",40, 1],
    ["Potion",20, 0],
    ["bow", 60, 0]
]
c= 0

run = True

print(f"Hallo {player_name} je hebt {player_gold} gold")



def exit():
    print(f"bedankt voor je bezoek, {player_name}!")
    print(f"je hebt {player_gold} gold over ")
    quit()

def show_menu():
    print("=== Fantasy Item Shop ===")
    for i in range(0,len(shop_item)):
        shop_item2 = shop_item[i]
        c = i+1
        print(f"{i+1}. Buy {shop_item2[0]} ({shop_item2[1]} gold)")
    print(f"{c+1}. View Inventory")
    print(f"{c+2}. Verkoop items")
    print(f"{c+3}. Exit Shop")
    a = int(input("maak een keuze: "))
    keuze(a)
    
def show_inventory(inventory):
    if not inventory:
        print("Your inventory is leeg")
    else:
        print("Your inventory")
        for i in inventory:
            print(f"- {i}")
    
def zoek_price(item):
    for i in range(0, len(shop_item)):
        if shop_item[i][0] == item:
            return int(shop_item[i][1])
        
def can_buy(gold, price):
    if gold
def keuze(k):
    global player_gold
    player_gold = int(player_gold)
    if k in range(0, len(shop_item)+1):
        shop_item2 = shop_item[k-1]
        if shop_item2[1] <= player_gold:
            if shop_item2[2] == 1 and shop_item2[0] in inventory:
               print(f"Je hebt {shop_item2[0]} al")
            else:
                player_gold -= shop_item2[1]
                print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
                print(f"je hebt nog {player_gold} over")
                inventory.append(shop_item2[0])
    if k == len(shop_item)+1:
        show_inventory(inventory)
    if k == len(shop_item)+2:
        if len(inventory) == 0:
            print("je hebt geen items om te verkopen")
        else:
            for i in inventory:
                
                print(f"{inventory.index(i) + 1}- {i} voor {zoek_price(i)/ 2} normale prijs {zoek_price(i)}")
            print("kies een item om te verkopen voor de helf van de waarde")
            print("Ales je niks wil verkopen kies 0")
            a = int(input("wat wilt u doen"))
            if a == 0:
                return
            else:
                print(f"je hebt {inventory[a - 1] } verkocht voor {(zoek_price(inventory[a - 1])) / 2}")
                player_gold += zoek_price(inventory[a - 1])/2
                print(f"je hebt {player_gold} gold")
                inventory.pop(a - 1)
                
    #match k:
    #        print(f"{i+1}. {inventory[i]} voor {shop_item}")
    #    case 1:
    #        shop_item2 = shop_item[k-1]
    #        if shop_item2[1] <= player_gold:
    #            if shop_item2[0] in inventory:
    #                print(f"Je hebt {shop_item2[0]} al")
    #            else:
    #                player_gold -= shop_item2[1]
    #                print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
    #                print(f"je hebt nog {player_gold} over")
    #                inventory.append(shop_item2[0])
    #        else:
    #            print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
    #    case 2:
    #        shop_item2 = shop_item[k-1]
    #        if shop_item2[1] <= player_gold:
    #            if shop_item2[0] in inventory:
    #                print(f"Je hebt {shop_item2[0]} al")
    #            else:
    #                player_gold -= shop_item2[1]
    #                print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
    #                print(f"je hebt nog {player_gold} over")
    #                inventory.append(shop_item2[0])
    #        else:
    #            print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
    #    case 3:
    #        shop_item2 = shop_item[k-1]
    #        if shop_item2[1] <= player_gold:
    #            player_gold -= shop_item2[1]
    #            print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
    #            print(f"je hebt nog {player_gold} over")
    #            inventory.append(shop_item2[0])
    #        else:
    #            print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
    #    case 4:
    #        shop_item2 = shop_item[k-1]
    #        if shop_item2[1] <= player_gold:
    #            if shop_item2[0] in inventory:
    #                print(f"Je hebt {shop_item2[0]} al")
    #            else:
    #                player_gold -= shop_item2[1]
    #                print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
    #                print(f"je hebt nog {player_gold} over")
    #                inventory.append(shop_item2[0])
    #        else:
    #            print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
    #    case 5:
    #        show_inventory(inventory)
    #    case 6:
    #        print("kies een item om te verkopen voor de helf van de waarde")
    #        if len(inventory) == 0:
    #            print("je hebt geen items om te verkopen")
    #        for i in range(0, len(inventory)):
    #            print(f"{i+1}. {inventory[i]} voor {shop_item}")
    #    case 7:
    #        run = False
    
while run:
    show_menu()