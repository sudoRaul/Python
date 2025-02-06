lista = ["hola", "caracola", "fulano", "de", "tal", "hola"]
wordUser = input("Introduzca una palabra: ")
wordReplace = input("Introduzca otra palabra: ")
if wordUser in lista:
    print("La palabra %s está en la lista" % wordUser)
    
print("La palabra %s aparece %d veces" % (wordUser, lista.count(wordUser)))
index = lista.index(wordUser)
lista[index]= wordReplace
#lista.pop(index)
for i in lista:
    print(i)