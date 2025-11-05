from OCP.ExerciseO2.classes.payment import Payment

class PayPalPayment(Payment):
    def __init__(self,amount):
        self.amount = amount

    def pay(self):
        print(f"pay pal amount: {self.amount}")