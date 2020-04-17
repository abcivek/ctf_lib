import base64
import codecs

def hex_dec(value):
	decoded = bytearray.fromhex(value).decode()
	return decoded
def base64_dec(value):
	decoded = base64.b64decode(value).decode('utf-8')
	return decoded
def rot13_dec(value):
	decoded = codecs.decode(value,'rot13')
	return decoded
def bigint_dec(value):
	decoded = bytearray.fromhex(value[2:]).decode()
	return decoded
def utf8_dec(value):
	decoded = chr(value)
	return decoded
