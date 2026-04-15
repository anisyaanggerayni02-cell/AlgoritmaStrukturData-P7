while True:
    print("\nMenu Pilihan")
    print("1. Barisan Fibonacci")
    print("2. M x N")
    print("0. Keluar")

    pilih = input("Pilih Menu: ")

    if pilih == "1":
        n = int(input("Masukkan Jumlah Suku: "))

        a, b = 1, 1
        print("Barisan Fibonacci:")
        
        for i in range(n):
            print(a, end=", " if i < n-1 else "")
            a, b = b, a + b

    elif pilih == "2":
        m = int(input("Masukkan Suatu Bilangan Bulat: "))
        n = int(input("Masukkan Suatu Bilangan Pengali: "))

        hasil = m * n
        print(f"{m} x {n} = {hasil}")

    elif pilih == "0":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi!")