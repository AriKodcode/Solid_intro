from SRP.ExerciseS3.classes.order import Order
from SRP.ExerciseS3.classes.print_invoice import InvoicePrinter

if __name__ == "__main__":
    order = Order(["shirt","shoes","belt"],600)
    printer = InvoicePrinter()
    printer.invoice_printer(order)