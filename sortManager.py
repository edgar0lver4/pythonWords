class SortManager:
    def isGreaterThan(self,val):
        return val['repeat']

    def findSimple(self,lista = [], desc = False):
        print('Find Simple Method')
        lista.sort(reverse=desc,key=self.isGreaterThan)
        return lista