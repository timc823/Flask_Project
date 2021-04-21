import numpy as np
import cv2 as cv
import os
# import scipy.misc


# fn = "../steg/images/small_flag.png"
# msg = "Pixels are awesome!"
# img = cv.imread(fn, cv.IMREAD_COLOR)

def file_in(filename):

    file = cv.imread(filename, cv.IMREAD_COLOR)
    img = cv.cvtColor(file, cv.COLOR_BGR2RGB)
    return img

def file_out(img):

    img_out = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    return img_out


def steg_message(filename,message):
    img = file_in(filename)
    msg = message
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
    # cv.imwrite(os.path.join('/steg/images', 'out_image.png'), out_img)
    cv.imwrite("out_image.png", out_img)
    print('All done')
    return out_img


out = steg_message('message.png','I love CS 5 and Prof Dodds')
# Try: desteg('out_image.png')




# Here is the code to test it's correct
# test1 = msgl
# test2 = b[:152]
# here is the code to encode message to image
# STOP = 152
# c = 0
# read the image and transfer it to string
# def fun():
#     global c, img, b
#     for i in range(len(img)):
#         for j in range(len(img[i])):
#             for k in range(len(img[i][j])):
#                 img[i][j][k] = b[c]
#                 c = c+1
#                 if c==STOP: return
#
# fun()


# for i in range(len(msgl)):
#     if b[i] % 2 == int(msgl[i]):
#         continue
#     else:
#         print(i)
#         print('This one is wrong')
# print('test complete and they are all correct')



#img2 = steg(img, msg)
  # write to file
#msg2 = desteg(img2)
# print("message is \"" + msg2 + "\"")
#assert(msg == msg2)


# cv.imwrite('output2.jpg',b)
# img2 = cv.imread('output2.jpg', cv.IMREAD_COLOR)
# img3 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
# cv.imwrite('output2.jpg',img3)

# new = []
# for l in range(0,len(b),3):
#     new.append([b[l],b[l+1],b[l+2]])
#
# evennew = []
#
# for m in range(0,len(new),50):
#     evennew.append(new[m:m+50])
#
# print(evennew[0])
# print(len(evennew[0]))
# print(len(evennew))
# newimg = np.array(new,dtype=np.unit8)


# # Image size
# width = 50
# height = 50
# channels = 3
# newimg = np.zeros((height, width, channels), dtype=np.uint8)
# xx, yy = np.mgrid[:height, :width]


# for y in range(img.shape[0]):
#     for x in range(img.shape[1]):
#         r, g, b = new[y][0], new[y][1], new[y][2]
#         print(r,g,b)
#         break
#         newimg[y][x][0] = r
#         newimg[y][x][1] = g
#         newimg[y][x][2] = b

# # scipy.misc.imshow(img)
# # img2 = cv.cvtColor(newimg, cv.COLOR_RGB2BGR)
# # cv.imshow('image',img2)
# # cv.waitKey(0)
# # cv.destroyAllWindows()

