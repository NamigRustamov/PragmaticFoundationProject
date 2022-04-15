### Day10



# arr=[1,34,23,90,230,1400,600,300,240] #bu listi nəzərə alaraq aşağıdakı problemləri həlledin
#1,23,34,90,230,240,300,600,1400
#Listin xususiyetlerini oyrenirem
#En boyuk ededi tapmaq
#listin siralanmasi



# def EnBoyukEded(): ## 1 variant
#     arr.sort(reverse=True)
#     print(arr[0],arr[1],arr[2])

    
# EnBoyukEded()

# def EnBoyukEded():
#     arr.sort(reverse=True)
#     i=0
#     while i<n:
#         print(arr[i])
#         i+=1
# EnBoyukEded()

###3-cu variant
##.......






    


#- Ən böyük 3 ədədi ekrana çap edin
#print(sorted(arr, reverse=True[:3])) # internetden tapdim
###########



#     - Ədədlərin ortalamasından böyük olan ədədləri ekrana çap edin

#ortalamani tap
#ededlerin cemini tap
# ededlerin sayini tap
#ortalama

# def Ortalamaenboyukeded():
#      for eded in arr:#????????????
#         cem=cem+eded
#         average=cem(len(arr))
#         if average>eded:
#          print(average)#?????????
# Ortalamaenboyukeded()


#     - Bu listin içərisində olan ədədlərin rəqəmlərinin cəmini ekrana çap edin 
# (nüm: 34->3+4=7)
#butun ededleri cap et
#riyazi hell yolu

# eded="samir"

# for herf in eded:
#     print (herf)



# for eded in arr:
#     cem+=eded
# print(cem)




#     - 2 rəqəmli ədədləri ekrana çap edin. ## 1ci variant
# cem=0
# for eded in arr:
#     if eded>10 and eded <100:
#         print(eded)
#
# 2ci variant
# for eded in arr:
#     if len(str(eded))==2:
#         print (eded)




# countries=['Azərbaycan','Turkiyə','Polsa','Macaristan','Ingiltere','Gurcustan']
# def herfsayinitap():
#     mtn="Memmed"
#     print(len(mtn))
# herfsayinitap() 


# def herfsayinitap():
#     for country in countries:
#         print(country,len(country))

# herfsayinitap()

#def enuzunolkeadinitap():
    #butun olkelerin ad uzunlugunun tap
    #butun olke adlarinin uzunlugunu bir liste yig
    #hazirlanan listi boyukten kiciye dogru sirala
    #ilk elementi cap et

# countries= ("Azərbaycan','Turkiyə','Polsa','Macaristan','Ingiltere','Gurcustan")
# x = countries.count("a")
# for x in countries:
#     z = countries.count("a")
#     x = countries.count("A")
# print(x)  
# print(z)




# print(len(countries))



#     - Bütün ölkələrin hərf sayını tapın [Link](https://www.youtube.com/watch?v=t176iXgG5PI)
#     - Ən uzun ölkə adını tapın
#     - Daxilində A hərfi olan ölkələri #tapın



from collections import deque


# test_list=[1,2,3,4,5]

# print("Original list:"+str(test_list))

# test_list.insert(0,25)
# print("Resultant list is:"+str(test_list))

# test_list=[30]+test_list
# print("Resultant list is:"+str(test_list))
# test_list[:0]=[8]
# print("Resultant list:"+str(test_list))

# test_list=deque(test_list)
# test_list.appendleft(8)
# test_list=list(test_list)
# print("Resultant list is:"+str(test_list))


# def prepend(list, str):
#     str+='{0}'
#     list=[str.format(i) for i in list]
#     return(list)
# list=[1,2,3,4]
# str='Geek'
# print(prepend(list,str))




test_string='geeksgeeks'

add_string="for"
print("The original string:"+test_string)
print("The add string:"+add_string)
N=5
# res=test_string[:N]+add_string+test_string[N:]

# print("The string after performing addition:"+str(res))

res=list(test_string)
res.insert(N,add_string)
res=''.join(res)

print("The string after performing addition:"+str(res))




