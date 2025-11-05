from SRP.ExerciseS3.classes.order import Order


class InvoicePrinter:
    @staticmethod
    def invoice_printer(items: Order):
        for item in items.items:
            print(item)

