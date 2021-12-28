import zlib


s = 'hello world!hello world!hello world!hello world!'
y = bytes(s, 'utf-8')
x = (zlib.compress(y))
print(x)
print(zlib.decompress(x))
