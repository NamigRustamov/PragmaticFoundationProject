#ad=input("Adinizi daxil edin:")
#print(ad + " Xoş gəlmisən!")

#print(5+6)

#Calculator New

# what = input( "What to do?(+, -):")

#x=input("X deyerini daxil et")
#y=input("Y deyerini daxil et")
#z=int(x)+int(y)
#print(f"{x}+{y}={z}")

# a = float(input( "Write first number: ")) 
# b = float(input("Write second number: "))
# if what == "+":
#  c = a + b
# print("Result:" + str(c))
# if what == "-": 
#  c = a - b
# print("Result:" - str(c)) 

#x=5
#y=6
#print(x+y)

#x=5; y=10 
#print(x+y)
#print(5+5*3)

#str
#ad="Namiq"

#int,float,complex
# x=5.5
# x=10
#print(type(ad))
#print(type(x))

#boolean
# rightanswer=True

#print(type(rightanswer))

#datatype List
# telebe01="Namiq"
# telebe02="Vahid"
# telebe03="Nargiz"
#print(telebe03)

# telebeadlari=["Namiq","Vahid","Nargiz"]
# namiq={
#     "ad":"Namiq",
#     "soyad":"Rustamov",
#     "yas":42,
#     "veten":"Azerbaycan",
#     "evlilikdurumu":False

#print(telebeadlari[0])
#print(namiq["soyad"])

#reqem indexdir, soz keydir

#print(type(telebeadlari))
#print(type(namiq))

#print([2,3,4]+[25,15,35])
#print("salam"+5)

#print(int(5.35))
#print(int(float("5.35")))
#print(5+int(bool("True")))
#print(bool(" "))
#print(bool("soz"))
#print(bool(""))
#print(bool(5))
#operator presedence - ardicil siralamaya gore emeliyatin aparilmasi

#Day06
#list,tuple,dict

#print(4>4)

# adlar=("Nargiz,""Vafa,""Narmin")
# #print(adlar[1])

# telebeadlari=["Namiq","Vahid","Nargiz"]
# namiq={
#     "ad":"Namiq",
#     "soyad":"Rustamov",
#     "yas":42,
#     "veten":"Azerbaycan",
#     "evlilikdurumu":False
    # }
#yas=int(input("Yasinizi daxil edin:"))

#x=int(input("X deyerini daxil edin:"))
#y=int(input("Y deyerini daxil edin:"))
#emeliyyat+input("Emeliyyatin isaretini daxil edin:")

#def toplama():
    #z=x+y
    #print(z)

#def cixma():
    #z=x-y
    #print(z)  

#if emeliyyat=="+"




#Day07

# ilkeded=1
# araeded=ilkeded
# soneded=30
# print(araeded)
# araeded=araeded+1
# print(araeded)
# araeded=araeded+1
# print(araeded)
# araeded=araeded+1
# print(araeded)
# araeded=araeded+1
# print(araeded)
# araeded=araeded+1
# print(araeded)
# araeded=araeded+1
# print(araeded)
# araeded=araeded+1
# print(araeded)
# araeded=araeded+1
# print(araeded)
# araeded=araeded+1
# print(araeded)

#bunu function halina getirek
ilkeded=1
araeded=ilkeded
soneded=30
def artir():
     global araeded
     print(araeded)
     araeded=araeded+1
     if araeded<30: #30 kimim atriracaq
        artir()
artir()

# def greeting():
#     print("Salam")
# greeting()

# ad="Namiq"
# def Foo():
#     ad="Resul"
#     print(ad)
# #print(ad) 

# Foo()
# print(ad)


# ad="Namiq"
# def Foo():
#      global ad # burada global oldugu ucun 2 defe Resul yazacaq. Yani globalda olan adi da evez edecek.
#      ad="Resul"
#      print(ad)
 

# Foo()
# print(ad) #name 'ad' is not define" verecek

# def SumNumbers():
#     x=5
#     y=6
#     z=x+y
#     print(z)
# SumNumbers() #bunun isi 5 ve 6 toplayir

# def SumNumbers(x,y): #burada x ve y- function parametersdir
#         z=x+y
#         print(z)
#SumNumbers(5,15) # 5 ve 15 function arguments
#burada f(x,y)=x+y->f(5,6), yani 5 ve 6 toplayacaq

# def adlaricapet(ad,soyad="Celilova"):#avtomatik bos soyadi olan yeri dolduracaq
#     print(ad+soyad)

# adlaricapet("Marif", "Gasimov")
# adlaricapet("Narmin", "Xalilova")
# adlaricapet("Nargiz","Celilova")
# adlaricapet("Narmin")


# def adlaricapet(ad,soyad="Celilova"):
#     print(ad+soyad)
#     def Salamlama():
#         print(" Salamlar")
#     Salamlama()
# adlaricapet("Narmin") #burada NarminCelilova Salamlar verecek

# ilkeded=1
# araeded=ilkeded
# soneded=30
#  def artir():
#       global araeded
#       print(araeded)
#       araeded=araeded+1
#       if araeded<30: #30 kimim atriracaq
#          artir()
#Bunu daha qisa sekile salaq

###Loops

# while araeded<100:
#     print(araeded)
#     araeded=araeded+1


#1-200 e geder ededleri cap et
# i=1
# while i<201:
#     i=i+1
#     print(i)

#1-200 geder ededlerin cemini cap et
# i=1
# cem=0
# while i<10:
#     i=i+1
#     cem=cem+i
    
# print(cem)    
#1-500 geder tek ededleri tap

#while loop istifadesi



### Day08

maaslar=[600,400,800,550,320]
#butun isci maaslarini ekranda
# i=0
# while i<5:#5 isci oldugu ucun
#     print(maaslar[i])
#     i+=1

# for maas in maaslar:
#     print(maas)

#toplam isci maasi
cem=0
for maas in maaslar:
    #cem=cem+maas
    cem+=maas
    #print(cem) 600,100,..2670
#print(cem) #2670


#ortalama maas
#ortalamamaas=cem/5 
ortalamamaas=cem/len(maaslar)
#print(ortalamamaas) #534.0

iscilerinyaslari=[23,34,19,45,34]

#ortalama yas
yaslarincemi=0
i=0
while i<5:
    yaslarincemi+=iscilerinyaslari[i]
    i+=1
ortalamayas=yaslarincemi/5
#print(ortalamayas)    


#ortalamadan kicik yaslar
# for yas in iscilerinyaslari:
#     if yas<ortalamayas:
#         print(yas)


j=0
while j<5:
    if iscilerinyaslari[j]<ortalamayas:
        print(maaslar[j]*1.1,iscilerinyaslari[j]) #660 23 ve 880 19
    j+=1










