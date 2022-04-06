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
users=[]
# İstifadəçi istehsal etmək üçün bir qəlib təyin etdim
class User:
    def __init__(self,_ad,_soyad,_email):
        self.Ad=_ad
        self.Soyad=_soyad
        self.Email=_email
    def getUserData(self):
        return f'{self.Ad} | {self.Soyad} | {self.Email}'


# İstifadəçiləri qeydiyata alan funksiya təyin etdim   
def UserRegistration():
    daxilEdilenAd=input('Zəhmət olmasa adınızı daxil edin:')
    daxilEdilenSoyad=input('Zəhmət olmasa soyadınızı daxil edin:')
    daxilEdilenEmail=input('Zəhmət olmasa email adresinizi daxil edin:')
    user=User(daxilEdilenAd,daxilEdilenSoyad,daxilEdilenEmail)
    users.append(user)
# İstifadəçi məlumatlarını ekranda göstərmək üçün funksiya təyin etdim
def ShowAllUser():
    for user in users:
        print(user.getUserData())

del User
print(User)

















