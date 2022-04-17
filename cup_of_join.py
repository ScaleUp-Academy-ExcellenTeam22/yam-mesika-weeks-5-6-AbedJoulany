
# function to join lists separated by symbol
def join(*args, sep='-'):
    new_lst = []
    if len (args) == 0:
        return new_lst

    new_lst = new_lst + args[0]
    for i in range (1, len (args)):
        new_lst.append (sep)
        new_lst.extend (args[i])
    return new_lst


if __name__ == "__main__":
    print (join ([1, 2], [8], [9, 5, 6], sep='@'))
    print (join ([1, 2], [8], [9, 5, 6]))
    print (join ([1]))
