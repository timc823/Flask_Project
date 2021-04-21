
import numpy as np
import cv2 as cv
import os
######################################################################
# functions
######################################################################

def file_in(filename):

    file = cv.imread(filename, cv.IMREAD_COLOR)
    img = cv.cvtColor(file, cv.COLOR_BGR2RGB)
    return img


def file_out(img):
    img_out = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    return img_out


def steg_message(filename,message):

    img = file_in(filename)
    msg = str(message)
    b = []
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # read the image and transfer it to string
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                b.append(img[i][j][k])

    # convert string to binary code
    s = [bin(ord(ch))[2:].zfill(8) for ch in msg]
    s.append('00000000')  # where to stop
    print(s)

    print('first part done! ')
    # add all the binary code to a list
    # msgl = []
    # for i in range(len(s)):
    #     for j in range(len(s[i])):
    #         num = s[i][j]
    #         msgl.append(num)
    msgl = ''.join(s)

    print('second part done!')
    # print('original image',b[:152])
    for k in range(len(msgl)):
        ''' check if the number is the same, if not replace it.'''
        if b[k] % 2 == int(msgl[k]) % 2:
            continue
        else:
            if b[k] % 2 == 0:
                b[k] += 1
            else:
                b[k] -= 1
    # print(b[:len(msgl)])
    print('third part done')
    STOP = len(msgl)+1
    # print(STOP)
    c = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                if c < STOP - 8:
                    img[i][j][k] = b[c]
                    c = c+1
                elif c == STOP+1:
                    break
                elif STOP - 8 <= c < STOP:
                    img[i][j][k] = 0
                    c += 1

    out_img = file_out(img)
    # TODO: how to select to images folder?!
    st = os.path.join('./project/steg/images', str('new_'+filename.split('/')[-1]))
    # currentpath = os.getcwd()
    cv.imwrite(st, out_img)
    # cv.imwrite("out_image30.png", out_img)
    print('All done')
    print(st)
    return st.split('/')[-1]


def desteg(filename):
    ### ========== TODO : START ========== ###
    # problem a
    # be sure to include a better docstring here!
    print('this is',filename)
    img = file_in(filename)
    S = ''

    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(len(img[i][j])):
                b = img[i][j][k]

                if b % 2 == 0:
                    S += '0'
                else:
                    S += '1'

                if S[-8:] == '00000000':
                    # print(S[:-8])
                    n =int(S,2)
                    h = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(('utf-8'))
                    h = h[:-1] # decode includes a final 0 byte! I'm removing it here!!
                    # print(len(h))
                    return h



# def main():
#     # test desteg (no need to convert)
#     fn = "./small_flag_with_message_rgb.png"
#     msg = "Wow! This worked!"
#     img = cv.imread(fn, cv.IMREAD_COLOR)
#     msg2 = deSteg(img)
#     print("message is \"" + msg2 +  "\"")
#     assert msg == msg2
#
#
# if __name__ == "__main__":
#     main()


