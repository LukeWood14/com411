import os
import csv

# def cwd():
#     path = os.getcwd()
#     print(f"current Working Directory: {path}")
#     for file in os.listdir(path):
#         print(file)
#
# def processing():
#     cwd()
# processing()


# def display_chars(file_path, num_chars):
#     with open(file_path) as file:
#         data = file.read(num_chars)
#         print(data)
#
#
# def display_line(file_path):
#     with open(file_path) as file:
#         data = file.readline().strip()
#         print(data)
#
#
# def display_text(file_path):
#     with open(file_path) as file:
#         data = file.read()
#         print(data)
#
#
# def run():
#     display_chars("C:/Users/5woodl59/OneDrive - Solent University/Documents/python imports/library.txt", 5)
#     display_line("C:/Users/5woodl59/OneDrive - Solent University/Documents/python imports/library.txt")
#     display_text("C:/Users/5woodl59/OneDrive - Solent University/Documents/python imports/library.txt")
#
# if __name__ == "__main__":
#     run()

# def search(file_name):
#     print("searching")
#     with open(file_name) as file:
#         for line in file:
#             print(f"looked in {line} ")
#         print("done")
# def run():
#     search("C:/Users/5woodl59/OneDrive - Solent University/Documents/python imports/library.txt")
# run()

def search(file_path):
    print("searching")
    sections = ""
    books = "Books:\n"
    with open(file_path) as file:
        for line in file:
            if line.startswith("Section"):
                sections += line
            else:
                books += line
    print("done")
    print(f"{sections}\n\n{books}")
    return(f"{sections}\n\n{books}")

def save(file_path, data):
    print("saving")
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")
def run():
    data = search("C:/Users/5woodl59/OneDrive - Solent University/Documents/python imports/books.txt")
    save("exported_books.txt", data)

run()




