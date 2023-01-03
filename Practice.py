import os
import threading

class ReadFile:
    def __init__(self, file):
        self.file = file

    def read(self):
        selected_file = self.file
        with open(selected_file, 'r') as file:
            return file.read().strip()

    def write_over(self, write):
        selected_file = self.file
        with open(selected_file, 'w') as file:
            return file.write(write)

    def append_to(self, append):
        selected_file = self.file
        with open(selected_file, 'a') as file:
            return file.write(append)

    def file_to_list(self):
        selected_file = self.file
        with open(selected_file, 'r') as file:
            return file.read().split()

    def one_word_at_time(self):
        selected_file = self.file
        with open(selected_file, 'r') as file:
            new = file.read().split()
            for word in new:
                print(word)

    def clear_file(self):
        selected_file = self.file
        with open(selected_file, 'w') as file:
            print("The contents in this file will be deleted.")
            print("Use the write_over function to add to the file.")
            print("The whitespace under this print statements shows the empty file.")
            return file.write('')


a = ReadFile("input1.csv")

a.write_over("We are going to make a new line")

print()

print(a.read())

print()

split = a.file_to_list()

print(split)

print()

a.one_word_at_time()

print()

a.clear_file()

print(threading.active_count())
print(threading.current_thread())

