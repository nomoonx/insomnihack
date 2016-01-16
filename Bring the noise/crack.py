import socket
from binascii import hexlify
import hashlib

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

s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

s.connect(('bringthenoise.insomnihack.ch',1111))

data = s.recv(512)
print data
challenge=data[-6:-1]
print challenge

request=-1

print 'before'

for i in range(1048976):
    responsehash = hashlib.md5(str(i)).hexdigest().strip()
    if responsehash[:5] == challenge:
        request=i
        break

print 'after '

if request!=-1:
    print 'im in'
    s.send(str(request)+"\n")
    equations=[]
    data = s.recv(4096)
    if data!="":
        equations.extend(data.split('\n')[:-1])
    print equations
    # print data
    while "Enter" not in data:
        data = s.recv(4096)
        if data!="" and data[:5]!="Enter" and data!="\n":
            equations.extend(data.split('\n')[:-1])
        print equations
        print data

    print 'length:'
    print len(equations)
    solution=solve(equations[:-1])
    print 'solution'
    print solution
    s.send(str(solution)[1:-1]+'\n')

    print 'sent'

    data = s.recv(1024)
    print data

#s.send('12345\n')





s.close()


