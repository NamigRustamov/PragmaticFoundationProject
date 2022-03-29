#Day03-Day04
"""Suallar:
1- Source code deyəndə nə nəzərdə tutulur? Source code insan terefinden her hansi program dilinde yazilan koddur.  
Translator bu kodu machine dilinde koda cevirir.
2- Source code və machine code arasında fərq nədir? Source code insan yazir ki computer machine coda cevirib programcinin emrlerini icra etsin. 
Machine code or machine language  instructionlardi ki,  birbasa  computerin  prosessoru terefinden icra olunur.
3- Niyə bizim yazdığımız kodlar tərcümə edilir? Cunku computer birbasha bizim emrleri anlamir. 
4- İnterpreter proqram necə  işləyir? İnterpreter proqram yazilan emrleri birbasha icra edir
5- Compiler program necə işləyir? Compiler program once yazilan codu high-level programming language-dan lower level language cevirir ki 
icra olunabilsin.
6- Dəyişənlər proqramlaşdırma dilində niyə istifadə olunur? Dəyişənlər proqramlaşdırma dilində istifade olunan deyerleri saxlanmasinda 
istifade olunur.
7- Dəyişən təyin edərkən hansı formada ad verilə bilər? Kicik ve ya boyuk herfle baslayabiler ve ancaq herf, regem ve alt xett icerebiler, 
ama reqemle baslayabilmez. Boyuk, kicik veya tam boyuk/tam kicik olmasi ferqli deyiskenler olacaq, buna da case sensitive deyilir.
8- Mən Azərbaycan əlifbası ilə dəyişən təyin edə bilərəmmi? Beli.
9- Biz niyə dataları tiplərə bölürük? Cunku deyiskenlere verilen deyerler ferqli ola biler. Ve ferqli data tipleriyle gorulen emeliyyatlari 
mueyyenlesdirir.
10- Pythonda olan data tiplərindən hansıları Javascript və C#da da var? Js ile number, str, boolen, list-array. C# ile int, float, dool,str.
11- Sizcə hər dildə fərqli sayda data tiplərinin olmasının səbəbi nədir? fərqli novde məlumatlarla işləmək üçün.

"""


#Day05.
"""
Pythonda neçə tip operator var? 
Python operatorlari asagidaki 7 gruplara ayrilir:

Arithmetic operators- matematik emeliyyatlar ucun
Assignment operators- deyerleri deyiskenlere tanitmaq ucun
Comparison operators- deyerleri muqayese etmek ucun
Logical operators- sherti statementlari kombine yazmaq ucun(and, or, if)
Identity operators- yaddashda olan eyni obyektleri mueyyen edir
Membership operators- obyekt daxilinde ardicilligi mueyyen edir
Bitwise operators- binar reqemleri muqayese edir"""

"""Python + operatoru fərqli data tipləri ilə necə işləyir? reqemleri(int) toplayir, sozleri(str) birlesdirir.
Type Conversion nədir və niyə ehtiyac duyuruq. Bir data type basqasina cevirir. 
Type Conversion 2 nov olur: Implicit Type Conversion - avtomatik datanin cevrilmesi ve Explicit Type Conversion - istifadecinin telebi uzere
cevirme. 
Müqaisə operatorları və şərtlər arasında əlaqə necə qurulur? 2 deyerler arasinda muqayese etmek yoluyla, yani:
x == y: burada x y deyerine bereberdimi?
x != y: burada x y deyerine bereber olmadigini gostermek ucun
x > y veya x < y : burada x y deyerinden boyuk veya kicik olmasini gosterer
x >= y veya x <= y: burada x y deyerinden boyukya da beraber veya kicik ya da beraber olmasini gosterer


indentation nədir? Python sintaksisində əhəmiyyəti nədir? Yazilan melumatin onunde boslugun buraxilmasidir.
Python indentation Python interpretera mueyyen grup melumatin mueyyen block of code-a aid olmasini gosterir.
"""
#Day06

#print(1,2,3,4,5,6,7,8,9,10)

#i = 1
#while i < 6:
  #print(i)
  #i += 1

#i = 1
#while i < 6:
 # print(i)
  #if (i == 3):
   # break
  #i += 1

#i = 1
#while i < 10:
 #   print(i)
  #  if (i == 10):
   #     break
    #i += 1
    
#i=1
#while i<11:
  #  print(i)
   # if (i == 11):
    #    break
    #i+=1

#i=1
#while i<11:
   # print(i)
   # if(i==11):
      # break
   # i+=1



#count from 1 to 20
#i=1
#while i<21:
  #  print(i)
  #  if (i==21):
   #     break
   # i+=1




#def my_function(Adlar):
  #  print(Adlar+ " Bravo")

#my_function("Aydin")       
#my_function("Aynur")
#my_function("Bahar")

#def my_function(fname, lname, uname):
   # print(fname + uname)

#my_function("Aynur", "Bravo", "kassir")    


#*arg
#def my_function(*worker):
  ##print("the newest worker is" + worker[3])
  

#my_function("emil", "ramin", "farid", " Aynur")

#keywords arguments

#workers
#def my_function(worker1, worker2,worker3):
   # print("the newest worker is " + worker1)

#my_function (worker1="Aynur", worker2= "Nargiz", worker3="Farid")

#Bank clients 
#def my_function(client1, client2, client3):
  # print("The valuable client is " + client1)

#my_function(client1="Vahid", client2="Aynur", client3="Namiq")    



#if, else, elif
# a=55
# b=35
# if   b>a:
#       print("b is greater than a")

# elif b<a:
#       print("a is greater than b")


# a=55
# b=55
# if a>b:
#     print("a is greater than b")

# elif a==b:
#     print("a is equal to b")    

# a=55
# b=59
# if a>b:
#     print("a is greater than b")

# elif a==b:
#     print("a is equal to b")

# else: print("a less than b")


# x=35
# y=25
# if x==y:
#     print("x is equal to y")
# elif x<y:
#     print("x is less than y")
# else: print("x is greater than y")


#Short Hand If ... Else

# a=150
# b=200
# print("A") if a>b else print("B")

# a=255
# b=155
# print("A") if a<b else print("false")

# a=24
# b=24
# print("A") if a>b else print("a=b") if a==b else print("a=b")

##And

a=25
b=35
c=85
if a>b and b>c: print("true") 
else: print("false")