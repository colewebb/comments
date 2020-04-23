class Line:
    def __init__(self, line, comment_block, line_number):
        self.contents = line
        self.comment_block = comment_block
        self.line_number = line_number

    def startswith(self, find):
        return self.contents.startswith(find)

    def add_comment(self, comment, longest):
        self.contents = self.contents.strip() + (longest - len(self.contents) + 4) * " " + self.comment_block + " " + comment + '\n'

    def __str__(self):
        return self.contents
