### Day14 

#### Görüləcək işlər
"""1. Dərsdə yazılan kodu analiz edərək bilmədiyiniz mövzuların siyahısı çıxarın
2. Bu mövzular üçün lazım gəlsə müəllimdən qaynaq tələb edin
3. Müəllimin yazdığı koda baxmadan problemi özünüz həlledin
4. Sinifdə yazılan proqrama aşağıdakı xüsusiyyəti əlavə edin.
 - ele funksiya yazın ki mən o funksiyaya istifadəçi adı daxil etdiyim zaman 
 funksiya o istifadəçinin bütün məlumatlarını users adlı listdən silsin"""

 # ad,soyad,email
# Istifadəçilərimi bir yerə yığmaq üçün bir baza təyin etdim
from sqlite3 import adapt


users=[]
# İstifadəçi istehsal etmək üçün bir qəlib təyin etdim
# class User:
#     def __init__(self,_ad,_soyad,_email):
#         self.Ad=_ad
#         self.Soyad=_soyad
#         self.Email=_email
#     def getUserData(self):
#         return f'{self.Ad} | {self.Soyad} | {self.Email}'


# # İstifadəçiləri qeydiyata alan funksiya təyin etdim   
# def UserRegistration():
#     daxilEdilenAd=input('Zəhmət olmasa adınızı daxil edin:')
#     daxilEdilenSoyad=input('Zəhmət olmasa soyadınızı daxil edin:')
#     daxilEdilenEmail=input('Zəhmət olmasa email adresinizi daxil edin:')
#     user=User(daxilEdilenAd,daxilEdilenSoyad,daxilEdilenEmail)
#     users.append(user)

# İstifadəçi məlumatlarını ekranda göstərmək üçün funksiya təyin etdim
# def ShowAllUser():
#     for user in users:
#         print(user.getUserData())

# class Book:
#     pass

# class Book():
#     def __init__(self, ad, yazar, sehifesayi):
#         self.Name= ad
#         self.Writer = yazar
#         self.Papercounts = sehifesayi

#     def showAllBookData(self):
#         print(self.Name, self.Writer,self.Papercounts)
#     def showBookNameGreaterThan(self,paper):
#         if self.Papercounts>paper:
#             print(self.Name)


# book01=Book("Dalga","Dior",500)
# book02=Book("Daglar","Chexov",320)
# book03=Book("ChaliGushu","YasharNuri",350)
    

# books=[book01,book02,book03]

# for book in books:
#     book.showBookNameGreaterThan(400)
class Worker:
    def __init__(self, ad, soyad, vezife):
        self.Ad=ad
        self.Soyad= soyad
        self.Vezife= vezife

    def showWorkerData(self):
        print(self.Ad, self.Soyad, self.Vezife)

    def SuperBonus(self,amount):
        print(f'Butun isci maaslarina {amount} Azn maas elave edilsin')

class ItDepartment(Worker):
    
    def checkServerStatus(self):
        print("Server melumatlarini her gun yoxla")


class SalesDepartment(Worker):
    
    def checkMonthlySales(self):
        print("AyliqSatislariYoxla")

class MarketingDepartment(Worker):
    
    def checkSosialMedia(self):
        print("Sosialmedia reklamlarini analiz et")


marketingWorker=MarketingDepartment("Ehmed","Memmedov","SMM")
ItWorker=ItDepartment("Ali","Memmedov","JuniorDeveloper")
SalesWorker=SalesDepartment("Alina","Memmedova","Sales Manager")
ItWorker.SuperBonus(200)






