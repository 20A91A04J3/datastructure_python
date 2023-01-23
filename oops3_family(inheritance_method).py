class bigfamily:
    s1='family'
    def __init__(self,grandmom,grandfather,mother,father,sister,brother):
        self.grandmom=grandmom
        self.grandfather=grandfather
        self.mother=mother
        self.father=father
        self.sister=sister
        self.brother=brother
    def display(self):
        print(self.grandmom,self.grandfather,self.mother,self.father,self.sister,self.brother)
class smallfamily(bigfamily):
    def __init__(self,grandmom,grandfather,mother,father,sister,brother,husband,wife,children):
        self.husband=husband
        self.wife=wife
        self.children=children
        super().__init__(name,grandmom,grandfather,mother,father,sister,brother)
    def display(self):
        print(self.husband,self.wife,self.children)
        super().display()
s1=family('saraswathi','chakarao','lakshmi','ramesh','siri','sai','swamy','venkata','surya')
s1.display()

    



