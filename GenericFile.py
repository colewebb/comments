import File
import Line
import sys


class GenericFile(File):
    def __init__(self, filename):
        self.filename = filename
        self.file = [[]]
        self.longest = 0
        try:
            f = open(filename)
        except FileNotFoundError:
            print("File cannot be opened.")
            sys.exit(1)
        for line in f:
            if len(line) > self.longest:
                self.longest = len(line)
        f.seek(0)
        i = 1
        for line in f:
            self.file[-1].append(Line.Line(line, "#", i))
            i += 1
        f.close()

    def __str__(self):
        to_return = ""
        for block in self.file:
            for line in block:
                to_return += line
        return to_return

    def write(self):
        f = open(self.filename, 'w')
        f.write(self)
        f.close()
