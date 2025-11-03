angka = int(input("Masukkan angka: "))

def matrixAngka(angka):
    if angka <= 3:
        print("Peringatan: salah input")
        return
    
    for x in range(angka):
        for y in range(angka):
            if angka % 2 == 1:  
                if y < x:
                    print("0", end="")
                else:
                    print(x + 1, end="")
            else:  
                if y > x:
                    print("0", end="")
                else:
                    print(x + 1, end="")
        print()  

matrixAngka(angka)
