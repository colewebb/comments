import sys


class Comments:
    def __init__(self):
        pass

    def add_line(self, line, length):
        return line.rstrip() + (length - len(line)) * " "

    def add_comment(self, line, length):
        l = self.add_line(line, length) + "# "
        print(l, end="")
        comment = input("")
        return l + comment


if __name__ == "__main__":
    f = open(sys.argv[1])
    longest = 0
    for line in f:
        if len(line) > longest:
            longest = len(line)
    c = Comments()
    f.close()
    f = open(sys.argv[1])
    write = []
    for line in f:
        write.append(c.add_comment(line, longest))
    f.close()
    f = open(sys.argv[1], 'w')
    for a in write:
        f.write(a + "\n")
    f.close()