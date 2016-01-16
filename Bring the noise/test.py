import SocketServer as ss
import struct
import os
from binascii import hexlify
import hashlib

def randint(bound):
    return struct.unpack('<L', os.urandom(4))[0] % bound


def learn_with_vibrations():
    q, n, eqs = 8, 6, 40
    solution = [randint(q) for i in range(n)]
    print 'solution'
    print solution
    equations = []
    for i in range(eqs):
        coefs = [randint(q) for i in range(n)]
        result = sum([solution[i]*coefs[i] for i in range(n)]) % q
        vibration = randint(3) - 1
        result = (result + q + vibration) % q
        equations.append('%s, %d' % (str(coefs)[1:-1], result))
    return equations, solution

def solve(equations):
    q, n, eqs = 8, 6, 40
    a=[1,2,3,4,5,6]
    for a[0] in range(q):
        for a[1] in range(q):
            for a[2] in range(q):
                for a[3] in range(q):
                    for a[4] in range(q):
                        for a[5] in range(q):
                            flag=True
                            for equation in equations:
                                eq=equation.split(',')
                                result = sum([a[i]*int(eq[i]) for i in range(n)]) % q
                                tempFlag=False
                                for i in range(3):
                                    if(result+q+i-1)%q==int(eq[-1]):
                                        tempFlag=True
                                        break
                                if not tempFlag:
                                    flag=False
                                    break
                            if flag:
                                return a

if __name__ == '__main__':
    equations, solution = learn_with_vibrations()
    # for equation in equations:
    #     print(equation + '\n')

    result=solve(equations)
    print 'result'
    print result
#
# s = socket.socket(
#     socket.AF_INET, socket.SOCK_STREAM)
#
# s.connect(('localhost',1111))
#
#
# data = s.recv(512)
# print data
# s.send('12345')
# s.close()