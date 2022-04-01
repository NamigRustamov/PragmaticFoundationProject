### Day11

          ### Görüləcək işlər

# #quote daxilində necə xarakter olduğunu tapın

#quote="""Programming isn't about what you know; it's about what you can figure out."""

# print(len(quote))


#quote daxilində necə boşluq olduğunu tapın
# 1 variant

# def Necebosluqvar(string):
#     cem=0
#     for i in range(0,len(string)):
#         if string[i]==" ":
#             cem+=1
#     return cem

# string = """Programming isn't about what you know; it's about what you can figure out."""
# print("number of spaces",Necebosluqvar(string) )

# 2 variant

# def Necebosluqvar(quote):
#     cem=0
#     for i in quote:
#         if i==" ":
#           cem+=1
#     return cem
# quote="""Programming isn't about what you know; it's about what you can figure out."""

# print("number of spaces",Necebosluqvar(quote))


#quote ifadəsini sözlərini ayrı ayrı ekrana çap edin
# print(quote.split())


#quote daxilində olan ' işarəsini silərək yeni əldə edilən ifadəni ekrana çap edin
# x=quote.replace("'", "")
# print(x)

#quote daxilində necə hərf olduğunu tapın
#print(len(quote))

#quote daxilində necə ədəd o hərfi olduğunu tapın
#print(quote.count("o"))


nums=[23,56,78,100,14,70,300,236]
#list-i tərs çevirərək ekrana çap edin
# nums.reverse()
# print('Reversed List:',nums)

#- sadəcə iki reqemli ededlerin cemini tapin
#rint(cem)
cem=0
for eded in nums:
    if eded<100:
        print(cem)

