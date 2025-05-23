from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while (1 == 1):
    print("\nCHUONG TRINH QUAN LI SINH VIEN")
    print("---------- MENU CHON MON ----------")
    print("| 1. Them sv                      |")
    print("| 2. Sua thong tin sv theo ma     |")
    print("| 3. Xoa sinh sv theo ma          |")
    print("| 4. Tim sv theo ten              |")
    print("| 5. Sap xep theo diem            |")
    print("| 6. Sap xep theo nganh           |")
    print("| 7. Hien danh sach               |")
    print("| 0. Thoat                        |")
    print("-----------------------------------")

    key = int(input("Chon mon: "))
    if (key == 1):
        print("\n1. Them")
        qlsv.nhapSinhVien()
        print("\nThanh cong!")
        
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Sua")
            print("\nNhap ma: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach trong")

    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa")
            print("\nNhap ma: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSv co ma = ", ID, " da bi xoa")
            else:
                print("\nSv co ma = ", ID, " khong ton tai")
        else:
            print("\nDanh sach trong")

    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim sv theo ten")
            print("\nNhap ten sv: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach trong")

    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep theo diem")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach trong")
    elif (key ==6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep theo ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach trong")

    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien danh sach")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach trong")

    elif (key == 0):
        print("\n0.Da thoat")
        break

    else:
        print("\nKhong co chuc nang")
        print("\nHay chon gia dung")