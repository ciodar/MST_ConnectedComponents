class Nodo:

    def __init__(self, id):
        self.id = id
        self.color = 0       # 0 --> White , 1 --> Gray , 2 --> Black
        self.p = None       #riferimento a nodo precedente