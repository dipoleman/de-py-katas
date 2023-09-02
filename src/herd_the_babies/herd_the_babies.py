
def herd_the_babies(string):

    parents = sorted(set(string.upper()))
    output = ''

    for parent in parents:
        output += parent
        output += parent.lower() * string.count(parent.lower())
        # print(output)

    return output

