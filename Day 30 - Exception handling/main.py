
try:
    file = open("a_file.txt")
    lists = [1, 2, 3]
except FileNotFoundError as error_message:
   print(error_message)
   print(lists)