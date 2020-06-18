import socket

sock = socket.socket((socket.AF_INET, socket.SOCK_STREAM)) 
try:
  sock.connect((“<ip adresi>”, <port no>))
  print “[+] Bağlantı başarılı!”
except socket.error as e:
  print “Hata! ”, e

sock.send(“gönderilecek veri”) 

# bir sokete bağlantı sağlamak
