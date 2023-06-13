class mammals:
    lungs = 'alveolar structure'
    limbs = 4
    ears = 2
    eyes = 2
    tail = 1

    def __init__(self,name, breed):
        self.name = name
        self.breed = breed

wolf = mammals('wolf', 'Canis lupus')
horse = mammals('horse','Equus caballus' )