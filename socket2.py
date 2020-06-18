import socket, sys

host=sys.argv[1]
port= int(sys.argv[2])
sock = socket.socket((socket.AF_INET, socket.SOCK_STREAM)) 
try:
  sock.connect((host, port))
  print “[+] Bağlantı başarılı!”
except socket.error as e:
  print “Hata! ”, e

sock.send(“gönderilecek veri”) 

# Argümanları komut satırından belirtiyoruz.
# Örnek kullanım: python socket2.py localhost 4444
