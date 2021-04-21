
# TODO: This is the file that you did earlier during the semester.
#  Try to modify the code you did earlier and return the output


def printRect(width,height,symbol):

    width = int(width)
    height = int(height)

    firstline = width * symbol
    output = []

    for i in range(height,0,-1):
        form = {}
        form['line'] = firstline
        output.append(form)

    return output


