from sortManager import SortManager
class ReadFileManager(SortManager):
    def __init__(self,archivo):
        file = open(archivo,'r')
        words= file.read().replace('.','').replace(',','').lower().split()
        self.archivo = words

    def viewWords(self):
        texto = self.archivo
        for line in texto:
            print(line)

    def find(self,order = 10):
        text = self.archivo
        lista = {}
        for word in text:
            lista[word] = lista.get(word,0)+1

        repeat = []
        for word in lista:
            k = {'palabra':word,'repeat':lista[word]}
            repeat.append(k)
        orderList = self.findSimple(repeat,True)
        i = 1
        for word in orderList[0:order]:
            print(f"{i} Palabra: {word['palabra']} - Repite: {word['repeat']}")
            i += 1
