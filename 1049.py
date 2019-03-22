class Animal():

    def classifica(self, tipos):
        self.tipos=tipos
        n1=tipos[0]
        n2=tipos[1]
        n3=tipos[2]

        if n1=='vertebrado':
            if n2=='ave':
                if n3=='carnivoro':
                    print('aguia')
                elif n3=='onivoro':
                    print('pomba')
            elif n2=='mamifero':
                if n3=='onivoro':
                    print('homem')
                elif n3=='herbivoro':
                    print('vaca')
        elif n1 == 'invertebrado':
            if n2=='inseto':
                if n3 =='hematofago':
                    print('pulga')
                elif n3 == 'herbivoro':
                    print('lagarta')

            elif n2 == 'anelideo':
                if n3=='hematofago':
                    print('sanguessuga')
                elif n3 == 'onivoro':
                    print('minhoca')



entrada=input().split(' ')
animaizinhus=Animal()
animaizinhus.classifica(entrada)
