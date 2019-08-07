#TODO: Refatorar e adaptar
#TODO: Criar Script de Teste
#TODO: Criar função que permite adicionar listas por vez, ao inves de aresta por aresta
#Caso o Grafo seja direcional, só preciso alterar o .addEdge pra nao duplicar
class Graph(object):
    def __init__(self, size, digrafo = False):
        #Adicionar estudo caso seja m digrafo
        self.adjMatrix = []
        for i in range(size):
            #preenche com 0s
            self.adjMatrix.append([0] * size)
        self.size = size
    def addVertice(self, v1, v2, weight = 1):
        #consertando o indice das listas, pois costumamos usar v1 e nao v0
        v1 -= 1
        v2 -= 1
        
        
        self.adjMatrix[v1][v2] = weight
        self.adjMatrix[v2][v1] = weight
    def removeVertice(self, v1, v2):
        v1 -= 1
        v2 -= 1
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between vertice {} and vertice {}".format(v1, v2))
            return None
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    def containsAresta(self, v1, v2):
        #Checa se há uma aresta entre os vertices
        return True if self.adjMatrix[v1][v2] > 0 else False

    def getAdjacentes(self,v1):
        '''Essa função recebe apena como parametro um Vertice.
            E Retorna uma Lista com todos os elementos adjacentes dele.'''
        if(int == type(v1)):
            v = v1
        else:
            x,v = v1.split('v')
            v = int(v)
            v -= 1
        auxList = []
        for ind, val in enumerate(self.adjMatrix[v]):
            if (val == 1):
                auxList.append('v' + str(ind+1))
        #print(auxList)
        return auxList

    def ehRegular(self):
        auxLista = []
        matrix = self.adjMatrix
        x = None
        for i in range(self.size):
            if(x==None):
                x = len(self.getAdjacentes(i))
            elif(x != len(self.getAdjacentes(i))):
                return False
        return True
        '''
        for row in matrix:
            for item in row:
                if(len(auxLista) == 0):
                    auxLista.append(row.count(1))
                elif(item in auxLista):
                    continue
                else:
                    print(row)
                    auxLista.append(row.count(item))
        return(auxLista)'''
            
    def __len__(self):
        return self.size
        
    def showGrafo(self):
        #Função que Representa o Grafo
        print('\n################################')
        print('Grafo apresentado como uma Matriz de Adjacência\n')
        for row in self.adjMatrix:
            print(*row)
        print('\n')
def main():
        g = Graph(7)
        g.addVertice(1, 2);
        g.addVertice(1, 3);
        g.addVertice(1, 5);
        g.addVertice(1, 7);
        g.addVertice(2, 3);
        g.addVertice(2, 4);
        g.addVertice(2, 5);
        g.addVertice(3, 4);
        g.addVertice(4, 6);
        
        #g.removeEdge(5,6);
        
        g.showGrafo()
        print(g.getAdjacentes(0))
        print(g.ehRegular())
            
if __name__ == '__main__':
   main()
   
