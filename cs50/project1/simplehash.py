def hidePass(orginPassword,key):
    newPass = ""
    codeNewPass = ""
    arrayOfMarkers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","z","1","2","3","4","5","6","7","8","9","0","@","!","#","$","%","^","&","*","(",")","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","W","Z","-"]
    i = 0;
    j = 0;
    k = 0;
    cezar = {}
    
    leng = len(arrayOfMarkers)
    for any_marker in arrayOfMarkers:
        if (j+key)<leng:
            cezar[any_marker]=arrayOfMarkers[j+key] 
            j+=1    
        elif(j<leng):
            cezar[any_marker]=arrayOfMarkers[k]
            j+=1; k+=1            
    for letterIn in orginPassword:
        newPass = newPass + letterIn + arrayOfMarkers[i] 
        i+=1;        
    for letterChanged in newPass:
        codeNewPass = codeNewPass + cezar[letterChanged]
    
    if(key<10):
        key = "0" + str(key) 
    else:
        key = str(key)      
    return codeNewPass+key
        

def shwoPass(hiddenPassword):
    last = hiddenPassword[-2:]
    hiddenPassword = hiddenPassword[:-2]
    newPass = hiddenPassword[::2]
    codeNewPass = ""
    arrayOfMarkers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","z","1","2","3","4","5","6","7","8","9","0","@","!","#","$","%","^","&","*","(",")","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","W","Z","-"]
    i = 0;
    j = 0;
    k = 0;
    cezar = {}
    
    leng = len(arrayOfMarkers)
    key = int(last)
    for any_marker in arrayOfMarkers:
        if (j+key)<leng:
            cezar[arrayOfMarkers[j+key]]=any_marker
            j+=1    
        elif(j<leng):
            cezar[arrayOfMarkers[k]]=any_marker
            j+=1; k+=1
      
    for letterChanged in newPass:
        codeNewPass = codeNewPass + cezar[letterChanged]  
    
    return  codeNewPass


orginPassword = "h@s7o-p01$Kaa"
klucz = 3


#print(hidePass(orginPassword,klucz)," : ",shwoPass(hidePass(orginPassword,klucz)))

#for k in range(0,50):
#    print(hidePass(orginPassword,k)," : ",shwoPass(hidePass(orginPassword,k)))

#print(shwoPass('A$c%K^Z&H*#(I)bAPBfC1D$E$F35'))