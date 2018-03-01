

import os

class Phonebook(object):

    def __init__(self, dir):
        self.entries = {}
        self.dir = str(dir)
        self.filename = 'phonebook.txt'

        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        self.file_cache = open(os.path.join(self.dir, self.filename), 'w')

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def get_names(self):
        return self.entries.keys()

    def get_numbers(self):
        return self.entries.values()

    def is_consistent(self):
        numbers = list(self.get_numbers())

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[j].startswith(numbers[i]) or\
                   numbers[i].startswith(numbers[j]):
                    return False
        return True

    def clear(self):
        self.entries = {}
        self.file_cache.close()
        os.remove(os.path.join(self.dir, self.filename))
        os.rmdir(self.dir)