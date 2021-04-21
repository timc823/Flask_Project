# CS5 Gold, hw3pr2
# Filename: hw3pr2.py
# Name:
# Problem description: Sleepwalking student

import random
import sys
import time
sys.setrecursionlimit(50000)
#count = 0
sdelay= 0.1

def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return random.choice([-1, 1])

def rwpos(start, nsteps):
    '''give a start point and how many steps need to move
        return the final position after the program finished.
    '''

    '''print the start position'''
    print('start is:', start)
    '''if finish the step, return the start position, else + the random step and nstep-1'''
    if nsteps == 0:
        #print('start is2:', start)
        return start
    else:
        #print('start is:', start)
        #nsteps = nsteps - 1
        #start = start + rs()
        return rwpos(start+rs(), nsteps-1)
        #return start


def rwsteps(start, low, high):

    start = int(start)
    low = int(low)
    high = int(high)

    count = 0
    form = {}
    output = []

    line = 'Dorm|' + ' ' * (start - low) + '(˘o˘ )' + ' ' * (high - start) + '|Class'
    # print(line)
    form['line'] = line
    output.append(form)

    while start != low or start != high:
        start = start + rs()
        if low < start < high:
            form = {}
            line = 'Dorm|' + ' ' * (start - low) + '(˘o˘ )' + ' ' * (high - start) + '|Class'
            # print(line)
            form['line'] = line
            output.append(form)
            # time.sleep(sdelay)
            count += 1
        elif start == low or start == high:
            form = {}
            line = 'Dorm|' + ' ' * (start - low) + '(˘o˘ )' + ' ' * (high - start) + '|Class'
            # print(line)
            form['line'] = line
            output.append(form)
            # print(count)
            return output


    # print(output)



a = rwsteps(10, 5, 15)

    # print('Class|' + ' ' * (start - low) + '(˘o˘ )' + ' ' * (high - start) + '|Dorm')
    # time.sleep((sdelay))
    # if start == low or start == high:
    #     return 0
    # else:
    #     return 1 + rwsteps(start + rs(), low, high)




'''
     print('Dorm|' + ' ' * (start - low) + '(˘o˘ )' + ' ' * (high - start) + '|Class')
    # print('Here is program start')
    count = 0
    place = ''
    while start != low or start != high:
        start = start + rs()
        if low < start < high:
            print('Dorm|' + ' ' * (start - low) + '(˘o˘ )' + ' ' * (high - start) + '|Class')
            time.sleep(sdelay)
            count += 1
        elif start == low or start == high:
            if start == low:
                place = 'Dorm'
                print('Dorm|' + ' ' * (start - low) + '(˘o˘ )' + ' ' * (high - start) + '|Class')
                break
            else:
                place = 'Class'
                print('Dorm|' + ' ' * (start - low) + '(˘o˘ )' + ' ' * (high - start) + '|Class')
                break
    print('stop')
    print('student take', count, 'steps to walk to', place)
'''

