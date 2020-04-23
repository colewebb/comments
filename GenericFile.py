import File
import Line
import sys


class GenericFile(File.File):
    def __init__(self, filename):
        self.filename = filename
        self.comment_block = "#"
        self.file = []
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
            self.file.append(Line.Line(line, "#", i))
            i += 1
        f.close()

    def __str__(self):
        to_return = ""
        for block in self.file:
            for line in block.contents:
                to_return += line
        return to_return

    def write(self):
        f = open(self.filename, 'w')
        f.write(self.__str__())
        f.close()
