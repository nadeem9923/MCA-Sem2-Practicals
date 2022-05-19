import os
a_file = open("C:/Users/Samadhan/PycharmProjects/pythonPracticals/example.txt", "r")
lines = a_file.readlines()
last_lines = lines[-5:]

print(last_lines)
a_file.close()