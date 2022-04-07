##Day08

# butun telebeler ad ve soyadlarini asagida sablon formada ekrana cap edin
# Ad: Ehmed,Soyad:Ehmedov
# Ad: Memmed,Soyad:Salehov
# 
# version 01


# adlar=['Ehmed','Memmed','Sabir','Ekrem','Namiq']
# soyadlar=['Ehmedov','Salehov','Quliyev','Tahirov','Rustemov']
# telebeler=[adlar,soyadlar]
# adlar=['Ehmed','Memmed','Sabir','Ekrem','Namiq']
# soyadlar=['Ehmedov','Salehov','Quliyev','Tahirov','Rustemov']
# telebeler=[adlar,soyadlar]
# print(telebeler[0][1])
# print(f"Ad:{telebeler[0][0]}, Soyad:{telebeler[1][0]}")
# print(f"Ad:{telebeler[0][1]}, Soyad:{telebeler[1][1]}")
# print(f"Ad:{telebeler[0][2]}, Soyad:{telebeler[1][2]}")
# print(f"Ad:{telebeler[0][3]}, Soyad:{telebeler[1][3]}")
# print(f"Ad:{telebeler[0][4]}, Soyad:{telebeler[1][4]}")

# i=0
# while i<len(adlar):
#     print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
#     i+=1

# ###Tapsiriq
# i=0
# while i<len(adlar):

#      print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
#      i+=1

# i=0
# for adlar in telebeler:
#     print((adlar[0]+soyadlar[0]),(adlar[1]+soyadlar[1]),(adlar[2]+soyadlar[2]))


# version 02

# telebeler=[
#     ['Ehmed','Memmed','Sabir'],
#     ['Ehmedov','Salehov','Quliyev']
# ]

# print(telebeler[1][2])

###Tapsiriq
telebeler=[
    ['Ehmed','Memmed','Sabir'],
    ['Ehmedov','Salehov','Quliyev']
 ]
# i=0
# while i<len(telebeler):
#     print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
#     i+=1



i=0
for telebe in telebeler:
       print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
         

#version 03
# telebe01={
#     "ad":"Ehmed",
#     "soyad":"Ehmedov"
# }
# telebe02={
#     "ad":"Memmed",
#     "soyad":"Salehov"
# }
# telebe03={
#     "ad":"Sabir",
#     "soyad":"Quliyev"
# }
# telebeler=[telebe01,telebe02,telebe03]
# print(telebeler[3]["ad"])

###Tapshiriq

# i=2
# while i<len(telebeler):
#     print(telebeler)
#     i+=1

# i=2
# for x in telebeler:
#     x=telebeler
#     print(x)
    

#version 04
# telebeler=[
# {
#     "ad":"Ehmed",
#     "soyad":"Ehmedov"
# },
# {
#     "ad":"Memmed",
#     "soyad":"Salehov"
# },
# {
#     "ad":"Sabir",
#     "soyad":"Quliyev"
# }
# ]
# print(telebeler[1]["ad"])


###Tapshiriq

# i=0
# while i<1:
#     print(telebeler)
#     i+=1


# i=0
# for x in telebeler:
#     print(x)

# #version 05
# telebeler={
#     "adlar":['Ehmed','Memmed','Sabir'],
#     "soyadlar":['Ehmedov','Salehov','Quliyev']
# }
# print(telebeler["adlar"][1]) 
# print(telebeler["adlar"][1])
# i=0
# while i<len(telebeler):
#    print(telebeler["adlar"][2]) 
#    i+=1
# i=0
# for x in telebeler:
    
#     print(telebeler["adlar"][2])
#     print(telebeler["soyadlar"][2])


# def FindFullname(ad):

#     pass

# FindFullname("Memmed")
# Axtardığınız tələbənin tam adı Memmed Salehov-dur


###Tapshiriq
# i=0
# while i<len(telebeler):
#     print(telebeler["adlar"][1])
#     i+=1


# i=0
# for telebe in telebeler:
#        print(telebe)
#        

# i=0
# while i<len(adlar):
#     print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
#     i+=1

# telebeler={
#     "adlar":['Ehmed','Memmed','Sabir'],
#     "soyadlar":['Ehmedov','Salehov','Quliyev']}

############################

adlar=['Ehmed','Memmed','Sabir','Ekrem','Namiq']
soyadlar=['Ehmedov','Salehov','Quliyev','Tahirov','Rustemov']
# fullnames=["Memmed Salehov","Ehmed Ehmedov" ]
#print (fullnames [1])

# for i in range(len(adlar)):
#     fullnames.append(adlar[i]+' '+soyadlar[i])

# for fullname in fullnames:
#     print(fullname)

##########################

def FindFullname(name):
    for ad in adlar:
        if ad==(name):
          print([ad],[soyadlar])
        
print("Axtardigininz telebenin adi", )
FindFullname("Ehmed")
    
# FindFullname("")
# def Axtardiğiniz_tələbənin_tam_adi
# adlar=['Ehmed','Memmed','Sabir','Ekrem','Namiq']
# soyadlar=['Ehmedov','Salehov','Quliyev','Tahirov','Rustemov']


# def adlaricapet(ad,soyad="Celilova"):
#     print(ad+soyad)
#     def Salamlama():
#         print(" Salamlar")
#     Salamlama()
# adlaricapet("Narmin") #burada NarminCelilova Salamlar verecek

# FindFullname("Memmed")
# Axtardığınız tələbənin tam adı Memmed Salehov-dur

