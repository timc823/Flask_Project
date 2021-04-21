

def countletter(r):

    file = open(r)
    line = file.read()
    file.close()

    alpha_dict = {}

    for i in line:
        # print(i)
        # print(i.isalpha())
        if i.isalpha():
            i = i.lower()
            try:
                alpha_dict[i] += 1
            except:
                alpha_dict[i] = 1
        else:
            continue

    output = []
    for key in sorted(alpha_dict.keys()):
        letter_dict = {}
        letter_dict['line'] = str(key)+ ' : ' + str(alpha_dict[key])
        output.append(letter_dict)

    # print(letter_dict)
    return output
