# Day09 [29 Mart 2022]

telebeler=[
{
    "ad":"Ehmed",
    "soyad":"Ehmedov"
},
{   "ad":"Rashad",
    "soyad":"Memmedov",
},
{    "ad":"Nariman",
    "soyad":"Narimanov"

}]
#for telebe in telebeler:
    # print (telebe["ad"])
    # print (telebe["soyad"])


# for telebe in telebeler:
#     print(telebe["ad"])
#     print(telebe["soyad"])
    
# for telebe in telebeler:
#     if (telebe["ad"])=="Ehmed":
#         print(telebe["ad"], telebe["soyad"])

# def FindWithName(name):
#     for telebe in telebeler:
#         if (telebe["ad"])==name:
#             print(telebe["ad"], telebe["soyad"])

# FindWithName("Nariman")



# def AdlaAxtar(name):
#     for telebe in telebeler:
#        if(telebe["ad"])==name:
#            print("Axtardiginiz telebenin soyadi ", telebe["ad"], telebe["soyad"])

# AdlaAxtar("Rashad")
    



# ededler=[15,20,25,35,20,18,55]
# cem=0
# for eded in ededler:
#     cem+=eded
# print(cem)


# ededler=[25,56,36,85,55]
# cem=0
# for eded in ededler:
#     cem+=eded

# print(cem)

# print(ededler)



# for eded in ededler:
#     if eded==35:
#         break
#     else:
#         cem+=eded
# print(cem)    

# for eded in ededler:
#     if eded==20:
#         break
#     else:
#         cem+=eded       
# print(cem)

# for eded in ededler:
#     if eded==35:
#         continue
#     else:
#         cem+=eded
# print(cem)

# for eded in ededler:
#     if eded%2==0:
#         continue
#     else:
#         cem+=eded
# print(cem)   #130 olacaq

# for eded in ededler: 
#     if eded>20 and eded<55:
#         cem+=eded

# print(cem) #60 olacaq  #20-55 araliqda reqemleri toplayir

# for eded in ededler:
#     if eded >20 and eded<55:
#         cem+=eded
#         print(eded) # burada 25ve 35 reqemlerini qosterecek


ededler=[15,20,25,35,20,18,55]
cem=0

def EdedleriEkanaCapEt(KicikEded,BoyukEded):
    for eded in ededler:
        if eded>KicikEded and eded<BoyukEded:
            print(eded)

EdedleriEkanaCapEt()
##############to be continued

