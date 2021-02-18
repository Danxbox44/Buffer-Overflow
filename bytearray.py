from __future__ import print_function 

bad_chars = "".split("\\x")
for x in range(1, 256):
	if "{:02x}".format(x) not in bad_chars:
		print("\\x" + "{:02x}".format(x),end='')
print()