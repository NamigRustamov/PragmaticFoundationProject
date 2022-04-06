"""#### Görüləcək işlər
1. arr = [10,20,30,20,10,50,60,40,80,50,40]
  - Verilən listdəki ədədlərin kvadratlarını hesablayaraq ayrı bir listin içərisində toplayın
  - Verilən listin içərisəndə təkrarlanan dəyərləri silərək geri qalan deyerlerin olduğu list yaradın
  - Verilən listdə cüt yerdə duran ədədlərlə tək yerdə duran ədədlərin yerini dəyişdirin
2. Aşağıdakı şərtləri yerinə yetirən proqram yazın
  - input metodu vasitəsi ilə istifadəçidən username və password yazmasını tələb edin
    - daxil edilən username və password admin,123456 dəyərlərinə bərabərdirsə ekranda "Sistemə daxil oldunuz təşəkkür edirik" mesajı göstərilsin
    - daxil olunan username və password-dan hər hansı boş buraxılıbsa ekranda "Dəyərlər boş buraxıla bilməz" mesajı göstərilsin
    - daxil edilən dəyərlərdən hər hansı biri səhvdirsə hansı dəyərin səhv olduğunu göstərən mesaj göstərilsin
3. Şans oyunu yazın.Tələblər aşağıdakı kimidir
  - İstifadəçi ekrandan 1-20 arasında sıra ilə 3 ədəd daxil edir. (məsələn 3,14,18)
  - Sistem 1-20 arasında təsadüfi 3 ədəd seçir
  - İstifadəçinin daxil etdiyi dəyərlər ilə sistem tərəfindən seçilən dəyərlər üst üstə düşürsə ekrana təbrik edirik mesajı yazılsin.
  - İstifadəçiyə bu əməlyatı təkrarlamaq üçün 3 şans verilsin
  - 3 haqqını istifadə etdikdən sonra "Siz oyunu uduzdunuz " mesajı verilsin"""


from multiprocessing.managers import BaseManager


arr = [10,20,30,20,10,50,60,40,80,50,40] 
# squares = []
# for number in arr:
#     arr.append(number*number)
#     squares+=number
#     print(squares)
# print(arr)



 
j = 0
for i in range(int(len(arr)/2)):
  arr[j], arr[j+1] = arr[j+1], arr[j]
  j += 2
 
print(arr) # internetden tapdim


li = []
for i in arr:
  if i not in li:
    li.append(i)

print ("список после удаления дубликатов : " + str(li)) #internetden tapdim



#2. Aşağıdakı şərtləri yerinə yetirən proqram yazın






while True:
    username=input("Zehmet olmasa username yazin :")
    password= input("Zehmet olmasa password yazin:")
    if username=='admin':
     continue
    elif " ":
        print("Dəyərlər boş buraxıla bilməz")
    else:
        print("Deyer sehv daxil edilmisdir")
        
    if password=='123456':
        print("Sistemə daxil oldunuz təşəkkür edirik")
        break
        print("Sistemə daxil oldunuz təşəkkür edirik")
    elif "":
        print("Dəyərlər boş buraxıla bilməz")
    else:
        print("Deyer sehv daxil edilmisdir")
    
