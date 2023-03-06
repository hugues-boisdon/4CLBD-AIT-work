class Node:

    data = None
    nextNode = None

    def __init__(self, _data):
        self.data = _data



class LinkedList:

    head = None
    size = 0

    def getPreviousNode(self,k):
        previousNode = self.head
        if (k > 0):
            for i in range(k-1):
                previousNode = previousNode.nextNode
        return previousNode


    def isEmpty(self):
        return self.head == None




    def insert(self, _data, k):
        self.size += 1
        # Si notre liste est vide et qu'on veut donner la 1ere valeur
        if(self.isEmpty() and k == 0):
            self.head = Node(_data)
        # Si on veut insérer a la tete
        elif(k == 0):
            nextNode = self.head
            self.head = Node(_data)
            (self.head).nextNode = nextNode
        # Sinon
        elif k <= self.size - 1:
            # Obtention du noeud à l'indice k-1
            previousNode = self.getPreviousNode(k)

            # Obtention du noeud à l'indice k (qui deviendra k+1)
            nextNode = previousNode.nextNode

            # Insertion du noeud
            previousNode.nextNode = Node(_data)
            (previousNode.nextNode).nextNode = nextNode
        else:
            self.size -= 1
            print("Erreur: indice trop grand")
    

    def append(self, _data):
        if isinstance(_data,list):
            appends = _data
        else:
            appends = [_data]

        for subData in appends:
                if(self.isEmpty()):
                    self.insert(subData, 0)
                else:
                    self.insert(subData, self.size)


    def delete(self, k):
        ret = None
        # Si notre liste est non vide
        if( not self.isEmpty()):
            self.size -= 1
            # Si on souhaite supprimer le 1er element
            if(k == 0):
                ret = self.head.data
                self.head = (self.head).nextNode
            else :
                # Obtention du noeud à l'indice k-1
                previousNode = self.getPreviousNode(k)

                # Obtention du noeud à l'indice k+1 (qui deviendra k)
                nextNode = (previousNode.nextNode).nextNode
                ret = (previousNode.nextNode).data

                # Supression du noeud d'indice k
                previousNode.nextNode = nextNode
        return ret
    


    def find(self, _data):
        # Initialisation de la recherche
        i = -1
        # Si la liste est non vide
        if( not self.isEmpty()):
            currentNode = self.head
            i = 0
            # Si on ne trouve pas à l'indice 0
            if (currentNode.data != _data):
                # Tant qu'on ne trouve pas 
                while (currentNode.data != _data):
                    # Si on est à la queue
                    if(currentNode.nextNode == None):
                        # On n'a pas trouvé
                        i = -1
                        break
                    currentNode = currentNode.nextNode
                    i += 1
        return i



    # Affiche la liste dans le terminal
    def print(self):
        aff = "["
        if(not self.isEmpty()):
            currentNode = self.head
            aff += str(currentNode.data)
            while(currentNode.nextNode != None):
                currentNode = currentNode.nextNode
                aff += ", " + str(currentNode.data)
        aff += "]"
        print(aff)


# Tests
if __name__ == '__main__':    
    print("")


    l = LinkedList()

    l.append(5)
    l.print()

    l.append("oui")
    l.print()

    l.append("yaya")
    l.print()

    l.insert("non", 15)


    print("")








