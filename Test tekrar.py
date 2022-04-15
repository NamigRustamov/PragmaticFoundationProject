

## DAY 03

# # print("Hello World")
# ad=input("Adinizi yazin: ")
# print(ad+ " Salam, necesen?")

#print(5+6) #ekrana 11 yazacaq

# x=input("X deyerini daxil edin:")
# y=input("Y deyerini daxil edin:")
# z=int(x)+int(y)
# print(f"{x}+{y}={z}")


# x=56
# y=65
# z=int(x)+int(y)
# print(f"{x}+{y}={z}") #121olur




## DAY 04

# x=5; y=6
# z=x+y
# print(z)
# print("salam")
# print(4-2*6)

#print(telebeadlari[1])

# telebeadlari=["Reshad","Namiq","Alim","Farid",]
# Namiq={
#     "ad":"Namiq",
#     "soyad":"Rustamov",
#     "yas":24,
#     "veten":"Azerbaycan",
#     "evlilikdurumu":False
# }

# print(Namiq["soyad"])
# print(type(Namiq))


## DAY 05
 


## DAY 06

# adlar=["Namiq","Farid","Alim"] #eyni tipli melumatlari yigiriq

# print(adlar[2])




# telebe={
#     "ad":"Namiq",
#     "soyad":"Rustamov",
#     "yas":30,
#     "evlilikstatusu":True
# }

# print(telebe["ad"])

# x=int(input("x ededini daxil et:"))
# y=int(input("y ededini daxil et:"))
# emeliyyat=input("emeliyyatin isaresini daxil edin:")

# def toplama():
#     z=x+y
#     print(z)

# def cixma():
#     z=x-y
#     print(z)

# if emeliyyat=="+":
#     toplama()

# if emeliyyat=="-":
#     cixma()

# say=[1,2,3,4,5]

# print(say)





## DAY 06 ##25.03.22
# x=int(input("Ilk reqemi daxil edin :"))
# y=int(input("ikinci reqemi daxil edin:"))

# def sum(a,b):
#     return a+b
# print(sum(x,y))    

# a=1
# b=a
# c=30
# def artir():
#     global b
#     print(b)
#     b=b+1
#     if b<c+1:
#         artir()
# artir()   

## DAY 07 ##28.03.22







# maaslar=[600,400,800,550,320,700]
#toplam isci maasi
#ortalama maas

# i=0
# while i<5:
#     print(maaslar[i])
#     i+=1


# for maas in maaslar:
#     print(maas)


# cem=0
# for maas in maaslar:
#     cem+=maas
# print(cem)

# ortalamamaas=cem/len(maaslar)
# print(ortalamamaas)

# iscilerinYaslari=[23,34,19,45,34]
# #ortalama yas
# yaslarincemi=0
# i=0
# while i<5:
#     yaslarincemi+=iscilerinYaslari[i]
#     i+=1
# ortalamayas=yaslarincemi/len(iscilerinYaslari)
#(ortalamayas)


# for yas in iscilerinYaslari:
#     if yas<ortalamayas:
#         print(yas)

# j=0
# while j<len(iscilerinYaslari):
#     if iscilerinYaslari[j]<ortalamayas:
#         print(maaslar[j],iscilerinYaslari[j])
#     j+=1


# ortalamayasdan az olanin maasini 10 faiz artirmaq
# j=0
# while j<len(iscilerinYaslari):
#     if iscilerinYaslari[j]<ortalamayas:
#         print(maaslar[j]*1.1,iscilerinYaslari[j])
#     j+=1



# butun telebeler ad ve soyadlarini asagida sablon formada ekrana cap edin
# Ad: Ehmed,Soyad:Ehmedov
# Ad: Memmed,Soyad:Salehov

#Version 01
# adlar=["Ehmed","Memmed","Sabir"]
# soyadlar=["Ehmedov","Salehov","Memmedov"]
# fullnames=[]
# print(telebeler[1][1],telebeler[0][1],telebeler[1][2],telebeler[0][2])

# print(f"Ad:{telebeler[0][0]}, Soyad:{telebeler[1][0]}")
# print(f"Ad:{telebeler[0][1]}, Soyad:{telebeler[1][1]}")
# print(f"Ad:{telebeler[0][2]}, Soyad:{telebeler[1][2]}")

# i=0
# while i<len(adlar):
#     print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
#     i+=1

# for i in range(len(adlar)):
#     fullnames.append(adlar[i]+' '+soyadlar[i])

# for fullname in fullnames:
#     print(fullname)
        

###########Burada




#Version 02

# telebeler=[
#     ["Ehmed","Memmed","Sabir"],
#     ["Ehmedov","Salehov","Memmedov"]
# ]
# # print(telebeler[1][2])

# i=0
# while i<len(telebeler[0]):
#     print(f"Ad:{telebeler[0][i]}, Soyad:{telebeler[1][i]}")
#     i+=1


# for i in range(len(telebeler[0])):
#     print(telebeler[0][i]+' '+telebeler[1][i])

#Version 03
# telebe01={
#     "ad":"Ehmed",
#     "soyad":"Ehmedov"    
# }
# telebe02={
#     "ad":"Ali",
#     "soyad":"Aliyev"
# }
# telebe03={
#     "ad":"Alim",
#     "soyad":"Agayev"
# }

# telebeler=[telebe01,telebe02,telebe03]
# print(telebeler[1]["ad"],telebeler[1]["soyad"],telebeler[0]["ad"],telebeler[0]["soyad"])

# for i in range(len(telebeler[0])):
#     print(telebe01,telebe02,telebe03)

##Version 04

# telebeler=[
#  {
#     "ad":"Ehmed",
#     "soyad":"Ehmedov"
#  },
#  {
#     "ad":"Ali",
#     "soyad":"Aliyev"
# },
# {
#     "ad":"Alim",
#     "soyad":"Agayev"
# }
#  ]
   
# print(telebeler[1]["ad"],telebeler[1]["soyad"])
# for i in telebeler:
#     print(telebeler[1]["ad"],telebeler[1]["soyad"])
# i=0
# for telebe in telebeler:
#     print(telebe)

# for telebe in telebeler:
#     if telebe["ad"]=="Ehmed":
#      print(telebe["ad"],telebe["soyad"])


##Version 05
# telebeler={
#    "adlar":["Ehmed","Memmed","Sabir"],
#     "soyadlar":["Ehmedov","Salehov","Memmedov"]
# }
# # print(telebeler["adlar"][1])

# for i in telebeler:
#     print(telebeler["adlar"][1])



#### Day 09 #########

# def FindWithName(name):  FUNCTION FUNCTION FUNCTION
#   for telebe in telebeler:
#     if telebe["ad"]==name:
    #  print(telebe["ad"],telebe["soyad"])

# FindWithName("Ehmed")

# ededler=[235,350,250,158,255,65,1250]
# cem=0
# for eded in ededler:
#     cem+=eded
# print(cem) #2563 olur



#ededlerin cemini tapan bir funksiya yazin

#tek ededleri tapan bir funksiya yazin
# ededler=[235,350,250,158,255,65,1250]
# cem=0
# for eded in ededler:
#     if eded%2==0:
#         continue
#     else:
#         cem+=eded
# print(cem)

#200 den < ve <600 olan ededleri tapan bir funksiya yazin
# ededler=[235,350,250,158,255,65,1250]
# cem=0
# for eded in ededler:
#     if eded>200 and eded<600:
#         print(eded)


# ededler=[235,350,250,158,255,65,1250]
# cem=0
# def Ededleriekranacapet(kicikeded,boyukeded):
#   for eded in ededler:
#     if eded>kicikeded and eded<boyukeded:
#        print(eded)
# Ededleriekranacapet(100,320)

# ededler=[25,18,36,85,65]
# def CemiTap():
#     cem=0
#     for eded in ededler:
#         cem+=eded
#     print(cem)
# CemiTap() ###229 olur

##Daha funksional 
# ededler=[25,18,36,85,65]
# def CemiTap(lst):
#     cem=0
#     for eded in lst:
#         cem+=eded
#     print(cem)

# CemiTap(ededler) ## ededler yazaraq 229 olur

#ededlerin ceminin 5 bolunmesinden qalan qaligi tapan funksiya
# ededler=[25,18,36,85,65]

# def CemiTap(lst):
#     cem=0
#     for eded in lst:
#         cem+=eded
#     return cem
# def QalanQaligiTap():
#     EdedlerinCemi=CemiTap(ededler)
#     print(EdedlerinCemi%5)

# QalanQaligiTap() ## 229/5, qaliq 4

# ededler.append(100)
# ededler.remove(85)
# # ededler.clear()
# ededler.sort()
# print(ededler)

# ad="Ali"
# yeniad=ad.capitalize()
# print(yeniad)





"""Esas oxunacaq :
-Functions
-Loops
-Data Structures
-OOP Basic"""