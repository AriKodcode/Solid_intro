from OCP.ExerciseO3.classes.notifier import Notifier

class SMSNotifier(Notifier):
    def __init__(self,message):
        self.message = message

    def send(self):
        print(f"the sms message is: {self.message}")