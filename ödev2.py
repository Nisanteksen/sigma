def asal(sayi):
    asal = True
    if sayi < 2:
        return False
    else:
        for i in range(2,sayi):
            if sayi %i == 0:
                asal=False
                break
    if asal == True :
        return True
    else:
        return False
sayi=int (input("sayiyi gir:"))
while asal(sayi)== False:
    sayi += 1
print(sayi)


