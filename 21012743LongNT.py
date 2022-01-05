def bai2():
    while True:
        try:
            n= int(input("moi ban nhap n= "))
            dayso= [int(input("hay nhap day so: ")) for i in range(0,n)]
            break
        except ValueError:
            print("hay nhap lai n hoac mang! ")
            continue
    return dayso
def bai3(dayso):
    print("Cac so co chu so dau la so le: ")
    for i in dayso:
        k = i
        if int(k %2 != 0):
            print(k,end='')
    
print("\nHo va ten: Nguyen Thanh Long")
print("Ma so sinh vien: 21012743")
print("Bai kiem tra giua ki.  De le\n\n")
bai2()
while True:
    dayso = bai2()
    bai3(dayso)
    check =input("Ban co muon tiep tuc chuong trinh? (y/n): ")
    if check == "y":
        continue
    elif check == "n":
        print("Ket thuc chuong trinh.")
        break