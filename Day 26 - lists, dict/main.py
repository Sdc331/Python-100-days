import pandas
# import random
# # list_1 = [1, 2, 3]
# # list_2 = [n+1 for n in list_1]
# # list_multiplied = [n*2 for n in range(1,5)]

# names = ['Angela', 'Pete', 'Jack', 'Josephine', 'Carol', 'Peter', 'Jule']

# # short_names = [name for name in names if len(name) < 5]
# # uppercased_names = [name.upper() for name in names if len(name) > 4]

# # print(short_names)
# # print(uppercased_names)
# student_score = {name:random.randint(1, 100) for name in names}
# passed_students = {name:"Passed" for (name, score) in student_score.items() if score > 60}
# print(student_score)
# print(passed_students)



user_input = input("What is your word?: ").upper()
split_word = user_input.split()
data = pandas.read_csv("nato_phonetic_alphabet.csv")
translated = {row.letter:row.code for (index,row) in data.iterrows()}
output = [translated[letter] for letter in user_input]
print(output)

# print(translated)
# output = [translated.code for translated.code in translated if translated.letter == split_word]
# print(output)
# for (index, row) in data.iterrows():
#     if row.letter == "Z":
#         print(row.code)


# for letter in split_word:
#     for (index, row) in data.iterrows():
#         print(row.get(letter))
#         if row.letter == letter.upper():
#             output.append(row.code)


# print(output)