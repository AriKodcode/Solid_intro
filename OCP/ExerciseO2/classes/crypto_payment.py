from OCP.ExerciseO2.classes.payment import Payment

class CryptoPayment(Payment):
    def __init__(self,amount):
        self.amount = amount

    def pay(self):
        print(f" Crypto Payment amount: {self.amount}")