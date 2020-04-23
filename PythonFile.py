import sys
import File
import Line


class PythonFile(File.File):
    def __init__(self, filename):
        self.filename = filename
        self.file = [[]]
        self.longest = 0
        try:
            f = open(filename)
        except FileNotFoundError:
            print("File cannot be opened.")
            sys.exit(1)
        in_function = False
        i = 1
        for line in f:
            if line.startswith("import"):
                pass
            elif line.startswith("from"):
                pass
            elif line.strip().startswith("#"):
                pass
            elif line == '\n':
                if in_function:
                    in_function = False
                self.file[-1].append(Line.Line(line, "#", i))
            elif line.strip().startswith("def"):
                in_function = True
                self.file.append([Line.Line(line, "#", i)])
            else:
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