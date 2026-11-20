player_name = input("voor je speler naan in: ")
player_gold = 100
inventory = []
shop_item = [
    ["Sword", 50],
    ["Shield",40],
    ["Potion",20],
    ["bow", 60]
]
c= 0

print(f"Hallo {player_name} je hebt {player_gold} gold")

def shop():
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
def keuze(k):
    global player_gold
    player_gold = int(player_gold)
    match k:
        case 1:
            shop_item2 = shop_item[k-1]
            if shop_item2[1] <= player_gold:
                if shop_item2[0] in inventory:
                    print(f"Je hebt {shop_item2[0]} al")
                    shop()
                else:
                    player_gold -= shop_item2[1]
                    print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
                    print(f"je hebt nog {player_gold} over")
                    inventory.append(shop_item2[0])
                    shop()
            else:
                print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
                shop()
        case 2:
            shop_item2 = shop_item[k-1]
            if shop_item2[1] <= player_gold:
                if shop_item2[0] in inventory:
                    print(f"Je hebt {shop_item2[0]} al")
                    shop()
                else:
                    player_gold -= shop_item2[1]
                    print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
                    print(f"je hebt nog {player_gold} over")
                    inventory.append(shop_item2[0])
                    shop()
            else:
                print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
                shop()
        case 3:
            shop_item2 = shop_item[k-1]
            if shop_item2[1] <= player_gold:
                player_gold -= shop_item2[1]
                print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
                print(f"je hebt nog {player_gold} over")
                inventory.append(shop_item2[0])
                shop()
            else:
                print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
                shop()
        case 4:
            shop_item2 = shop_item[k-1]
            if shop_item2[1] <= player_gold:
                if shop_item2[0] in inventory:
                    print(f"Je hebt {shop_item2[0]} al")
                    shop()
                else:
                    player_gold -= shop_item2[1]
                    print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
                    print(f"je hebt nog {player_gold} over")
                    inventory.append(shop_item2[0])
                    shop()
            else:
                print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
                shop()
        case 5:
            print("Your inventory")
            for i in inventory:
                print(f"- {i}")
            shop()
        case 6:
            print("kies een item om te verkopen voor de helf van de waarde")
            if len(inventory) == 0:
                print("je hebt geen items om te verkopen")
                shop()
            for i in range(0, len(inventory)):
                print(f"{i+1}. {inventory[i]} voor {shop_item}")
        case 7:
            exit()
    print("geef een geldige invoer")
    shop()



def exit():
    print(f"bedankt voor je bezoek, {player_name}!")
    print(f"je hebt {player_gold} gold over ")
    quit()
shop()
