x=5
print(x)
# butun telebeler ad ve soyadlarini asagida sablon formada ekrana cap edin
# Ad: Ehmed,Soyad:Ehmedov
# Ad: Memmed,Soyad:Salehov
# 
# version 01

adlar=['Ehmed','Memmed','Sabir','Ekrem','Namiq']
soyadlar=['Ehmedov','Salehov','Quliyev','Tahirov','Rustemov']
telebeler=[adlar,soyadlar]
# adlar=['Ehmed','Memmed','Sabir','Ekrem','Namiq']
# soyadlar=['Ehmedov','Salehov','Quliyev','Tahirov','Rustemov']
# telebeler=[adlar,soyadlar]
# print(telebeler[0][1])
# print(f"Ad:{telebeler[0][0]}, Soyad:{telebeler[1][0]}")
# print(f"Ad:{telebeler[0][1]}, Soyad:{telebeler[1][1]}")
# print(f"Ad:{telebeler[0][2]}, Soyad:{telebeler[1][2]}")

i=0
while i<len(adlar):
    print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
    i+=1
# i=0
# while i<len(adlar):
#     print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
#     i+=1
# version 02

# telebeler=[
#     ['Ehmed','Memmed','Sabir'],
#     ['Ehmedov','Salehov','Quliyev']
# ]
# print(telebeler[1][2])
# version 03
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
# print(telebeler[1]["ad"])
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
# #version 05
# telebeler={
#     "adlar":['Ehmed','Memmed','Sabir'],
#     "soyadlar":['Ehmedov','Salehov','Quliyev']
# }
# print(telebeler["adlar"][1]) 
# print(telebeler["adlar"][1])


# def FindFullname(ad):

#     pass

# FindFullname("Memmed")
# Axtardığınız tələbənin tam adı Memmed Salehov-dur
