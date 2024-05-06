class Ingredient:
    def __init__(self, label, amount):
        self.label = label
        self.amount = amount

    def __eq__(self, other):
        return self.label == other.label and self.amount == other.amount

    def __hash__(self):
        return hash((self.label, self.amount))

    def __str__(self):
        return f'{self.label} : {self.amount}'
    
    def __repr__(self):
        return f'{self.label} : {self.amount}'
