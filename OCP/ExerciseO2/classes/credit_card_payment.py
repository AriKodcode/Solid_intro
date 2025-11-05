from OCP.ExerciseO2.classes.payment import Payment

class CreditCardPayment(Payment):
    def __init__(self,amount):
        self.amount = amount

    def pay(self):
        print(f"credit card amount: {self.amount}")
