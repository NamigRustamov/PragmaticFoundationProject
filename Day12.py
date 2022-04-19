quote="""İpoteka kreditinin illik faiz dərəcəsi müştərinin ümumi gəlirindən asılı olaraq dəyişə bilər. 
ABB ilə siz də sərfəli şərtlərlə yeni və gözəl evinizə sahib olun."""

def xaraktersayinitap(content):
   return(len(content))


xaraktersayi=xaraktersayinitap(quote)

def abbinfometnihesabla(content,persent):
    abbmetniuzunlugu=int(xaraktersayi*persent)
    abbmetni=content[0:abbmetniuzunlugu]
    # for i in range(abbmetniuzunlugu):
    #     abbmetni+=quote[i]
    return(abbmetni)

abbmetni=abbinfometnihesabla(quote,0.2)

# bunu qisa yazmaq yolu - return content [0:int(xaraktersayinitap(content)*persent)]
