import sys
import FileFactory


def ui_line(line):
    print(str(line.line_number) + ": " + line.contents.rstrip() + (file.longest - len(line.contents) + 4) * " " + file.comment_block + " ", end="")


if __name__ == '__main__':
    factory = FileFactory.FileFactory()
    file = factory.makeFile(sys.argv[1])
    for line in file.file:
        ui_line(line)
        line.add_comment(input(), file.longest)
    file.write()
