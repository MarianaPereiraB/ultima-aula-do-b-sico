nome = ["joão", "carlos", "vitor", "hellen", "luiza"]
achar = input("digite o nome que você quer achar: ")
for k in range (5):
    if achar == nome[k]:
        print(f"o nome {achar} está na lista")
        break
    else:
        print("esse nome não está na lista")
        break