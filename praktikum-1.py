while True:

    print('Berikut menu di kalkulator')
    print('1.Tambah')
    print('2. Kurang')
    print('3. Kali')
    print('4.Bagi')
    print('Krtik Q untuk menghentikan')

    n = input("Masukkan pilihan: ")

    if n == 'Q':
        break

    a = int(input('a: '))
    b = int(input('b:'))
    if n == "1":
        print(a+b)
    elif n == "2":
        print(a-b)
    elif n == "3":
        print(a*b)
    elif n == "4":
        print(a/b)
