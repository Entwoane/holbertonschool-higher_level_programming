#!/usr/bin/python3
<<<<<<< HEAD
for i in range(122, 96, -1):
    if (122 - i) % 2 == 0:
        print(chr(i), end='')
    else:
        print(chr(i - 32), end='')
=======
for i in range(26):
    print("{:c}".format(122 - i - (i % 2 * 32)), end="")
>>>>>>> 49bab1a8039503eb3848742a0dafd30c4916693f
