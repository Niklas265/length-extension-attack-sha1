import hashlib
import struct
import binascii
from sha1 import Sha1Hash
import sys

def sha1padding(length):
    padding = b""
    blocksize = 64
    r = (length % blocksize)
    padding = padding + b'\x80'
    if(r >= 56 and r <=59):
        padding = padding + (64*b'\x00')
    while r != 59:
        padding = padding + b'\x00'
        r = (r + 1) % 64 

    bitlength = length*8
    padding = padding + struct.pack(">i",bitlength)
    return padding


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 " + str(sys.argv[0]) + " <SHA-1 hash> <length of original message> <message to append>")
        exit(-1)
    
    initialState = sys.argv[1]
    originalLength = int(sys.argv[2])
    padding = sha1padding(originalLength)
    append = sys.argv[3]
    hasher = Sha1Hash(initialState, originalLength + len(padding))
    hasher.update(bytes(append, 'utf-8'))
    print("Appended message: " + str(padding) + str(append))
    print("Hash:")
    print(binascii.hexlify(hasher.digest()))
