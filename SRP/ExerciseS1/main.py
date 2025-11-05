from SRP.ExerciseS1.classes.book import Book
from SRP.ExerciseS1.classes.saving_to_file import SavingToFile

if __name__ == "__main__":
    book = Book("Harry potter","j k rolling","harry lorning in hagworts")
    SavingToFile.saving_to_file("harry data",book)


