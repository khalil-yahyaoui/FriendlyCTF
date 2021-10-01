#This challenge contains a base 64 encoded message and all we have to do is decode it using python
# we have a pre-installed python module called base64
# f"" in print is used just to format

from base64 import b64decode
c = "U2VjdXJpbmV0c3tiYXNlNjRfc3RyaW5nc19hcmVfZXZlcnl3aGVyZV90b299"
print(f"Flag is {b64decode(c)}")
