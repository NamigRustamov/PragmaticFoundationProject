# arr=[1,34,23,90,230,1400,600,300,240] #bu listi nəzərə alaraq aşağıdakı problemləri həlledin

    #- Ən böyük 3 ədədi ekrana çap edin

#1,23,34,90,230,240,300,600,1400
#Listin xususiyetlerini oyrenirem
#En boyuk ededi tapmaq
#listin siralanmasi

# def enboyukededitap():
#     arr.sort(reverse=True)
#     print(arr[0],arr[1],arr[2])
# enboyukededitap()

# 2 variant
# def enboyukededitap():
#     arr.sort(reverse=True)
#     i=0
#     while i<4:
#        print(arr[i])
#        i+=1
# enboyukededitap()

# 3 variant
# def enboyukededitap(n): #En optimal while variant
#     arr.sort(reverse=True)
#     i=0
#     while i<n:
#        print(arr[i])
#        i+=1
# enboyukededitap(5)  #en boyuk 5 ededi cixaracaq

# 4 variant
# def enboyukededitapwithWhile(n):
#     arr.sort(reverse=True)
#     i=0
#     while i<n:
#        print(arr[i])
#        i+=1
  #enboyukededitapwithWhile(n):#en boyuk n sayda ededi cixaracaq


# 5 variant
# range(20)
# def enboyukededitapwithFor():
#     arr.sort(reverse=True)
#     for i in range(20):
#        print(i)

# enboyukededitapwithFor()  # 1-19 ededi cixaracaq

# 6 variant  #En optimal For variant
# range(20)
# def enboyukededitapwithFor(n):
#     arr.sort(reverse=True)
#     for i in range(n):
#        print(arr[i])

# enboyukededitapwithFor(4)  # 3 boyuk ededi cixaracaq PRODOLJENIE


#- Ən böyük 3 ədədi ekrana çap edin
#print(sorted(arr, reverse=True[:3])) # internetden tapdim

############

#Ədədlərin ortalamasından böyük olan ədədləri ekrana çap edin
#ortalamani tap
#ededlerin cemini tap
##ededlerin sayini tap
#ortalama=ededlerin cemi/ededlerin sayi
# def ortalamadanboyukeded():
    # cem=0
    # for eded in arr:
    #     cem+=eded
    # average=cem/len(arr) 
    # for eded in arr:   
    #    if eded>(cem/len(arr)):
    #      print(eded)

# ortalamadanboyukeded()       #VEYA

# 

 # - 2 rəqəmli ədədləri ekrana çap edin. 
# cem=0
# for eded in arr:
#     if eded>10 and eded <100:
      # print(eded)


#VEYA
# for eded in arr:
#   if len(str(eded))==2:
#     print(eded)


# Bu listin içərisində olan ədədlərin rəqəmlərinin cəmini ekrana çap edin (nüm: 34->3+4=7)

#butun ededleri cap et
# riyazi hell yolu
# def EdedlerinReqemlerininCeminiTap():
# eded="samir"  #eger str olsa

# for herf in eded:
#     print (herf)  #butun herfleri verdi

  #veya

#   for eded in arr:
#       cem=0
#       for reqem in str(eded):
#        cem=cem+int(reqem)
#       print(cem)

# EdedlerinReqemlerininCeminiTap()

# countries=['Azərbaycan','Turkiyə','Polsa','Macaristan','Ingiltere','Gurcustan']
# def herfsayinitap():
#     mtn="Memmed"
#     print(len(mtn))
# herfsayinitap() 


# def herfsayinitap():
#     for country in countries:
#         print(country,len(country))

# herfsayinitap()


# def enuzunolkeadinitap():
    #butun olkelerin ad uzunlugunun tap
    #butun olke adlarinin uzunlugunu bir liste yig
    #hazirlanan listi boyukten kiciye dogru sirala
    #ilk elementi cap et
#   aduzunluqlari=[]
#   for country in countries:
#     aduzunluqlari.append(len(country))
#   aduzunluqlari.sort(reverse=True)
#   print(aduzunluqlari[0])

# enuzunolkeadinitap()

  
# countries= ("Azərbaycan','Turkiyə','Polsa','Macaristan','Ingiltere','Gurcustan")
# x = countries.count("a")
# for x in countries:
#     z = countries.count("a")
#     x = countries.count("A")
# print(x)  
# print(z)





#
## Day10 [30 Mart 2022]

#### Görüləcək işlər

"""- Aşağıdakı tələbləri yerinə yetirən proqram yazmaq tələb olunur.
  1. Yeni istifadəçi əlavə et
  2. Bütün istifadəçiləri gör
  3. İstifadəçi sil
  4. İstifadəçi məlumatlarını dəyişdir"""



# ekran=""""1. Yeni istifadəçi əlavə et
  # 2. Bütün istifadəçiləri gör
  # 3. İstifadəçi sil
  # 4. İstifadəçi məlumatlarını dəyişdir"""

# emr=input("Yeni emeliyyat nomresini yaz:")
# istifadeciler=[]
# if emr=="1":
#   print("Adinizi daxil edin:")"""
  





# adlar=[]
# while True:
#     ad=input("Yeni istifadeci elave et : ")
#     adlar.append(ad)
#     secim=input('''Emeliyyati dayandirmaq ucun 1,istifadecileri gormek ucun 2,
#     istifadecini silmek ucun 3, davam ucun 4 secin:''' )
#     if secim=='1':
#       break
#     elif secim=="2":
#       print(adlar)
#     if secim=="3":
#       adlar.remove(ad)

# print(adlar)  
#  PRODOLJENIE 




reqem=[25,3525,85,1350,158,850,665,2582]

# def findthebignum(n):
#   reqem.sort(reverse=True)
#   i=0
#   while i<n:
#     print(reqem[i])
#     i+=1
# findthebignum(2)

# range(6)
# def findthebignum(n):
  
#   reqem.sort(reverse=True)
#   for i in range(n):
#     print(reqem[i])
# findthebignum(3)

# def findbignum(n):
#   range(n)
#   reqem.sort(reverse=True)
#   for i in range(n):
#       print(reqem[i])

# findbignum(2)

# def ortalamadanbignum():
#     cem=0
#     for eded in reqem:
#         cem=cem+eded
#         say=len(reqem)
#         ortalama=cem/say
#     for eded in reqem:
#       if eded>ortalama:
#          print(eded)
# ortalamadanbignum()


# for eded in reqem:
#   if len(str(eded))==2:
#      print(eded)

# def vahidlerincemi():
#   for eded in reqem:
#    cem=0
#    for vahid in str(eded):
#     cem=cem+int(vahid)
#     print(cem)
# vahidlerincemi()


countries=["Tunis","Aljeria","Russia","Turkey"]
# def herfsaytap():
#   for country in countries:
#     print(country,len(country))

# herfsaytap()

# def thelongestcountryname():
#   aduzunluqlari=[]
#   for country in countries:
#     aduzunluqlari.append(len(country))
#   aduzunluqlari.sort(reverse=True)
#   print(aduzunluqlari[0])
# thelongestcountryname()


def herfsahibiolan(soz,axtarilanherf):
  herfsayi=0
  for herf in soz:
    if herf==axtarilanherf:
      herfsayi+=1
  if herfsayi==0:
    print(f'{soz} sozunde {axtarilanherf} herfi yoxdur')
  else:
    print(f'{soz} sozunde {herfsayi} eded {axtarilanherf} herfi var')
herfsahibiolan('Russia','s')



