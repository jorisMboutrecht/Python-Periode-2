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
    



def exit():
    print(f"bedankt voor je bezoek, {player_name}!")
    print(f"je hebt {player_gold} gold over ")
    quit()
shop()
