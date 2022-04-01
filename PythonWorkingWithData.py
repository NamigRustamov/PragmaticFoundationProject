### Day09 [29 Mart 2022]

telebeler=[
{
    "ad":"Ehmed",
    "soyad":"Ehmedov"
},
{   "ad":"Memmed",
    "soyad":"Memmedov",
},
{    "ad":"Nariman",
    "soyad":"Narimanov"

}]

# for telebe in telebeler:
#     print(telebe["ad"]) #adlari verecek


# for telebe in telebeler:
#     if telebe["ad"]=="Memmed":
#         print(telebe["ad"],  telebe["soyad"]) #burada Memmedin adini ve soyadini verecek

# def FindWithName(_name): #burada ad ile axtaris verir
#     for telebe in telebeler:
#         if telebe["ad"]==_name:
#             print(telebe["ad"],telebe["soyad"])

# FindWithName("Nariman")


# ededler=[234,342,678,12,90,100,341,1459] 
# cem=0
# # ededlerin cemini tapan funksiya
# for eded in ededler:
#        cem=cem+eded #print(eded) veya
#        cem+=eded
# print(cem)


# ededlerin hamisi ekra cap ede biliremmi
#print(ededler) OR 

### BREAK VE CONTINUE Looplarda istifade olunur
# for eded in ededler:
#       if eded==341:
#           break
#       else:
#           cem+=eded
# print(cem) #1456

 
# for eded in ededler:
#       if eded==341:
#           continue
#       else:
#           cem+=eded
# print(cem)  #2915


# tek ededleri tapan bir funksiya yazin
#for eded in ededler:
    # if eded%2==0:
    #     continue
    # else:
    #     cem+=eded
#print(cem)   #1800 oldu


# 200 den boyukb600 den kicik olan ededleri tapan funksiya yaz   
# for eded in ededler:
#     if eded>200 and eded<600:
#         print(eded)  

#ededlerin hamisini ekrana cap edebileremmi   
# def EdedleriEkranaCapEt(kicikEded,boyukEded):
#     for eded in ededler:
#         if eded>kicikEded and eded<boyukEded:
#             print(eded)  

#EdedleriEkranaCapEt(300,1000) #yuxaridaki misal

####
ededler=[23,45,23,12,69,14]

#ededlerin cemini tapan funksiya yaz

# def CemiTap():
#     cem=0
#     for eded in ededler:
#         cem+=eded
#     print(cem)
# #CemiTap() #186 olur

# #VEYA
# ededle=[23,45,23,12,69,14]
# def CemiTap(_lst):
#     cem=0
#     for eded in _lst:
#         cem+=eded
#     print(cem)
#CemiTap(ededle) #186 olur VEYA

###ISENILEN LISTI hesablamaq
def CemiTap(_lst):
    cem=0
    for eded in _lst:
        cem+=eded
    print(cem)
#CemiTap([5,2,8]) #15 olur

#edelerin ceminin 5-e bolunmesinden qalan qaligi tapan funksiya yaz

def CemiTap(_lst):
    cem=0
    for eded in _lst:
        cem+=eded
    return cem

def QalanQaligiTap():
    ededlerinCemi=CemiTap(ededler)
    print(ededlerinCemi%5)

# QalanQaligiTap()



##  Buildin function ve Custom functionlar var

def CemiTap(_lst):
    cem=0
    for eded in _lst:
        cem+=eded
    return cem

def QalanQaligiTap():
    ededlerinCemi=CemiTap(ededler)
    print(ededlerinCemi%5)

#QalanQaligiTap()

ededler.append(34)# liste 34 elave edir
ededler.remove(12) #listden 12 silir
#ededler.clear() #listi temizleyir
ededler.sort() # listi siralayir
# print(ededler)

ad="nariman"

#yeniad=ad.upper() #butun herifleri boyudur - NARIMAN
#yeniad=ad.capitalize() #ilk herifi boyudur - Nariman
#print(yeniad)

   # "Axtardiginiz telebenin soyadi"
### Suallar: void və return funksiya nədir? 

   ### Day 10

