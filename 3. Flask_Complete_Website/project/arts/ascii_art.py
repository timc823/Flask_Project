

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


def printTriangle(width,symbol,rightsideup):

    width = int(width)
    # to set the True False to bool
    rightsideup = eval(rightsideup)
    output = []
    if rightsideup == True:
        for i in range(1,width+1):
            form = {}
            line = (symbol+ ' ')*i
            form['line'] = line
            output.append(form)
            # print((symbol+ ' ')*i)
        return output
    if rightsideup == False:
        for j in range(width,0,-1):
            form = {}
            line = (symbol + ' ') * j
            form['line'] = line
            output.append(form)
        return output


def printBumps(num, symbol1, symbol2):
    num = int(num)
    output = []

    for i in range(1,num+1):
        a = printTriangle(i,symbol1,'False')
        output.append(a[0])
        b = printTriangle(i,symbol2, 'False')
        output.append(b[0])
    return output


def printDiamond(width, symbol) :
    width = int(width)
    output = []
    for i in range (1,width+1):
        form = {}
        line = ' '*(width-i)+(symbol+' ')*i
        form['line'] = line
        output.append(form)
    for j in range (width-1,0,-1):
        form = {}
        line = ' ' * (width - j) + (symbol + ' ') * j
        form['line'] = line
        output.append(form)
    return output


def printStripedDiamond(width, sym1, sym2):
    width = int(width)
    s = (' ' +sym1 + ' ' + sym2)*100

    output = []

    for i in range(1,width*2,2):
        # print(' '*(width-i//2), end = '')
        # print(s[:i+1])
        form1 = {}
        line1 = ' '*(width-i//2)+(s[:i+1])
        form1['line'] = line1
        output.append(form1)
        # print(line1)

    for j in range ((width-1)*2,0,-2):
        form2 = {}
        line2 = ' ' * (width - j // 2+2) +s[:j][::-1]
        form2['line'] = line2
        output.append(form2)
    return output
    # print(output)
        # print(' ' * (width - j // 2+2), end='')
        # p = (s[:j])
        # print(p[::-1])
        # print(line2)
    # print('done')



def printCrazyStripedDiamond(width, sym1, sym2, sym1Width, sym2Width):
    # width > sym1width > sym2width
    width = int(width)
    sym1Width = int(sym1Width)
    sym2Width = int(sym2Width)
    s = ((sym1+' ')*sym1Width + (sym2+' ')*sym2Width)*100
    output = []

    for i in range(1, width * 2, 2):
        form1 = {}
        line1 =  ' ' * (width - i // 2) + s[:i + 1]
        form1['line'] = line1
        output.append(form1)
        # print(' ' * (width - i // 2), end='')
        # print(s[:i + 1])

    for j in range((width - 1) * 2, 0, -2):
        form2 = {}
        line2 = ' ' * (width - j // 2) + s[2:j+2][::-1]
        form2['line'] = line2
        output.append(form2)
        # print(' ' * (width - j // 2), end='')
        # p = (s[2:j+2])
        # print(p[::-1])
    # print(output)
    return output

def printStarTree(height,symbol):
    n = int(height)
    output = []
    for i in range(1, n + 1):
        form = {}
        line = ' ' * (n - i) + symbol * (2 * i - 1)
        form['line'] = line
        output.append(form)
    return output

def printLuxuryTree(height, symbol1, symbol2):
    n = int(height)
    if n < 3:
        n = 3
    output = []
    form = {}
    

    form['line'] = str(' ' * (n - 1) + '*')
    output.append(form)

    for j in range(n - 2):
        for i in range(3):
            form1 = {}
            line1 = ' ' * (n - i - j - 1) + symbol1 * (2 * (i + j) + 1)
            form1['line']=line1
            output.append(form1)
    for k in range(n - 2):
        form2 = {}
        line2 = ' ' * ((n + 1) // 2) + symbol2 * (n - 2)
        form2['line'] = line2
        output.append(form2)

    return output
