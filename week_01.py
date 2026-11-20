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


def shop():
    print("=== Fantasy Item Shop ===")
    for i in range(0,len(shop_item)):
        shop_item2 = shop_item[i]
        c = i+1
        print(f"{i+1}. Buy {shop_item2[0]} ({shop_item2[1]} gold)")
    print(f"{c+1}. View Inventory")
    print(f"{c+2}. Exit Shop")
    a = int(input("maak een keuze: "))
    keuze(a)
def keuze(k):
    global player_gold
    player_gold = int(player_gold)
    match k:
        case 1:
            shop_item2 = shop_item[k-1]
            if shop_item2[1] <= player_gold:
                player_gold -= shop_item2[1]
                print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
                print(f"je hebt nog {player_gold} over")
                shop()
            else:
                print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
                shop()
        case 2:
            shop_item2 = shop_item[k-1]
            if shop_item2[1] <= player_gold:
                player_gold -= shop_item2[1]
                print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
                print(f"je hebt nog {player_gold} over")
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
                shop()
            else:
                print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
                shop()
        case 4:
            shop_item2 = shop_item[k-1]
            if shop_item2[1] <= player_gold:
                player_gold -= shop_item2[1]
                print(f"je hebt {shop_item2[0]} gekocht voor {shop_item2[1]}")
                print(f"je hebt nog {player_gold} over")
                shop()
            else:
                print(f"je komt {shop_item2[1] - player_gold} gold te kort voor {shop_item2[0]}")
                shop()
        case 5:
            print(list(inventory))
            shop()
        case 6:
            return
            
shop()
