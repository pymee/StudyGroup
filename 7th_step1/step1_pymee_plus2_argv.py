#!/usr/bin/python3
# coding:utf-8

import sys

# �������琔�����擾
num1 = sys.argv[1]
num2 = sys.argv[2]

# �����Z
wa = int(num1) + int(num2)
print(str(num1) + " �{ " + str(num2) + " = " + str(wa))

# �����Z
if int(num1) >= int(num2) :
    sa = int(num1) - int(num2)
    print(str(num1) + " �| " + str(num2) + " = " + str(sa))
else :
    sa = int(num2) - int(num1)
    print(str(num2) + " �| " + str(num1) + " = " + str(sa))

# �|���Z
seki = int(num1) * int(num2)
print(str(num1) + " �~ " + str(num2) + " = " + str(seki))

# ����Z
if int(num1) >= int(num2) :
    try :
        sho = int(num1) // int(num2)
        rem = int(num1) % int(num2)
        print(str(num1) + " �� " + str(num2) + " = " + str(sho) + " ���܂� " + str(rem))
    except ZeroDivisionError :
        print(str(num1) + " �� " + str(num2) + " = " + "�y�G���[�z0�ŏ��Z���Ă��܂�")
else :
    try :
        sho = int(num2) // int(num1)
        rem = int(num2) % int(num1)
        print(str(num2) + " �� " + str(num1) + " = " + str(sho) + " ���܂� " + str(rem))
    except ZeroDivisionError :
        print(str(num2) + " �� " + str(num1) + " = " + "�y�G���[�z0�ŏ��Z���Ă��܂�")