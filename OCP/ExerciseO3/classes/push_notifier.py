from OCP.ExerciseO3.classes.notifier import Notifier

class PushNotifier(Notifier):
    def __init__(self,message):
        self.message = message

    def send(self):
        print(f"{self.message}")