#From the hint we can see that we need to convert hex to bytes using python
c = "5365637572696e6574737b6865785f737472696e67735f6172655f657665727977686572657d"
print(f"Flag is {bytes.fromhex(c)}")
