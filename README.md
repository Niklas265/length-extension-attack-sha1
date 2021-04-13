# SHA-1 Length Extension Attack POC
Implementation of the Length Extension attack on SHA1

## SHA-1 Implementation
The implementation of SHA-1 in this repo is taken from [ajalt/python-sha](https://github.com/ajalt/python-sha1). It was adjusted, so that the initial state of the SHA1 implementation can be freely modified for the calculation. This was necessary, because the hashlib implementation of SHA1 does not allow to set the initial state to a specific value. Comments have been made inside of the source code, to identify the changes mad.  


## Length Extension Attacks
Hash functions can be used in MACs to protect integrity. The hash functions SHA1, SHA2 & MD5 hash inputs using Merkle-Damgard construction. This means, that the hash value that they compute is the internal state of the Hash function at the end of the computation. This makes insecure MAC designs,like MAC(m) = H(m||k), in which those hash functions are used, vulnerable to length extension attacks. <br>
In length extension attacks an attacker can use a valid hash h = H(x), which was computed from a unknown value x, to create a valid hash of an extension x||y for an arbitrary string y. This string y consits out of the padding p1 of the original message and a string z, that can be freely chosen by an attacker.

## Input parameters

* <b>Hash of message:</b> internal state at the end of the computation of SHA1(key || message || padding). This is needed to set the internal state for the computation.

* <b>Length of the original message: </b> length of the original message without the padding for the original message. This length is needed, so that the correct padding p2 can be computed for (key || message || p1 || append || p2)

* <b>Message to append:</b> Message that should be appended to the original message. It is inserted after the original padding.

## Usage
```
$ python3 sha1LengthExtensionAttack.py 

Usage: python3 sha1LengthExtensionAttack.py <SHA-1 hash> <length of original message> <message to append>
```
