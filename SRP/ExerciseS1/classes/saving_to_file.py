from SRP.ExerciseS1.classes.book import Book


class SavingToFile:
    @staticmethod
    def saving_to_file(file_name, book: Book):
        with open(f"{file_name}.txt", "a") as file:
            file.write(book.content + "\n")
