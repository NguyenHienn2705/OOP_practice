import math

class TuLanh:
    #Ham xay dung
    def __init__(self, *args):
        if len(args) == 0:
            self.__nhanhieu = "Elextrolux"
            self.__maso = "UNKNOWN"
            self.__nuocsx = "Việt Nam"
            self.__tkdien = True
            self.__dungtich = 256
            self.__gia = 7,000,000
        elif len(args) == 1 and isinstance(args[0], TuLanh):
            tl = args[0]
            self.__nhanhieu = tl.__nhanhieu
            self.__maso = tl.__maso
            self.__nuocsx = tl.__nuocsx
            self.__tkdien = tl.__tkdien
            self.__dungtich = tl.__dungtich
            self.__gia = tl.__gia
        elif len(args) == 6:
            self.__nhanhieu = args[0]
            self.__maso = args[1]
            self.__nuocsx = args[2]
            self.__tkdien = args[3]
            self.__dungtich = args[4]
            self.__gia = args[5]
    #sao chep
    def makeCopy(self,tl):
        self.__nhanhieu = tl.__nhanhieu
        self.__maso = tl.__maso
        self.__nuocsx = tl.__nuocsx
        self.__tkdien = tl.__tkdien
        self.__dungtich = tl.__dungtich
        self.__gia = tl.__gia
    #nhap thong tin
    def nhapThongTin(self):
        self.__nhanhieu = input()
        self.__maso = input()
        self.__nuocsx = input()
        s = input()
        self.__tkdien = (s == "TRUE")
        self.__dungtich = str(input())
        self.__gia = str(input())
    #hien thi 
    def print(self):
        print("Nhãn hiệu:", self.__nhanhieu)
        print("Mã số:", self.__maso)
        print("Nước SX:", self.__nuocsx)
        print("T/K điện:", "Có" if self.__tkdien else "Không")
        print("Dung tích:", str(self.__dungtich) + "L")
        print("Giá:", str(self.__gia) + "VNĐ")
    #getter
    def layNhanHieu(self):
        return self.__nhanhieu
    def layGia(self):
        return self.__gia
    #so nguoi sdung
    def soNguoiSD(self):
        return self.__dungtich // 100
    #cung nhan hieu
    def cungNhanHieu(self, tl):
        return self.__nhanhieu == tl.__nhanhieu
    #nho hon dung tich
    def nhHon(self, tl):
        return self.__dungtich < tl.__dungtich
    



    