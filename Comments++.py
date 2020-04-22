import sys                                                                     # 


class Comments:                                                                # 
    def __init__(self, tab_length=4):                                          # init
        self.tab_length = tab_length                                           # 

    def add_line(self, line, length):                                          # add line method
        return line.rstrip() + (length - len(line) + self.tab_length) * " "    # return stripped line plus spaces

    def add_comment(self, line, length, comment_block="#"):                    # add comment method
        if line == '\n':                                                       # if line is empty
            print()                                                            # print to keep things tidy
            return line                                                        # return an unmodified line
        l = self.add_line(line, length) + comment_block + " "                  # construct line
        print(l, end="")                                                       # print line
        comment = input("")                                                    # get comment from input
        if comment == '\n':
            return line
        return l + comment + "\n"                                              # return line with input and newline


if __name__ == "__main__":                                                     # main
    f = open(sys.argv[1])                                                      # open the file
    longest = 0                                                                # find longest line
    for line in f:                                                             # 
        if len(line) > longest:                                                # 
            longest = len(line)                                                # 
    c = Comments()                                                             # make comments object
    f.close()                                                                  # close the file and reopen to reset cursor position
    f = open(sys.argv[1])                                                      # 
    write = []                                                                 # make array to act as file buffer
    for line in f:                                                             # for each line
        write.append(c.add_comment(line, longest))                             # add the comment to write buffer
    f.close()                                                                  # close the file
    f = open(sys.argv[1], 'w')                                                 # reopen file in overwrite mode
    for a in write:                                                            # for each line in buffer
        f.write(a)                                                             # flush buffer
    f.close()                                                                   # close the file
