#ad=input("Adinizi daxil edin:")
#print(ad + " Xoş gəlmisən!")

#print(5+6)

#Calculator New

#what = input( "What to do?(+, -):")

#x=input("X deyerini daxil et")
#y=input("Y deyerini daxil et")
#z=int(x)+int(y)
#print(f"{x}+{y}={z}")

#a = float(input( "Write first number: ")) 
#b = float(input("Write second number: "))
#if what == "+":
 #c = a + b
#print("Result:" + str(c))
#if what == "-": 
 #c = a - b
#print("Result:" - str(c)) 

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
#print(1)
#print(2)
#print(3)


# maaslar=[600,400,800,550,320]
# #butun isci  maaslari ekranda goster
# i=0
# while i<5:
#     print(maaslar[i])
#     i+=1
# cem=0
# for maas in maaslar:
#      cem=cem+maas
#      cem+=maas

iscilerinYaslari=[20,24,19,45,34]

yaslarinCemi=0
i=0
while i<5:
    yaslarinCemi+=iscilerinYaslari[i]
    i+=1
ortalamaYas=yaslarinCemi/5