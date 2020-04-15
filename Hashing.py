"""This file has been created for converting the password to hash and add salt to it
So it can be more secure. The functionality would have been added to the application if
option of creating and/or updating the passwrod was given"""

import hashlib

def hashThePassword(password):
    salt= '5gz'
    password= password+salt
    password= hashlib.md5(password.encode())
    return password.hexdigest()

print(hashThePassword('cloud'))
