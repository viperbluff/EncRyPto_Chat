import threading
import socket
from Crypto.Cipher import AES
i=socket.gethostbyname(socket.gethostname())
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=[port no]
add=((i,port))
server.bind(add)
client_add=[]
print "[*]waiting for request at %s : %d" %(i,port)
server.listen(10)
def handle_client():
    conn,addr=server.accept()
    client_add.append(conn)
    print"[*]Received connection from %s at %d" %(addr[0],addr[1])
    conn.send("\t\t\t<<<*** Welcome to The EncRyPto_Chat ****>>>\n\t\t\t{------->Version 1.0@tikoo_sahil<-------}")
    response1=conn.recv(4096)
    conn.send("Hello %s" %(response1))
    key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
    iv = "abcdefghijklmnop"
    def pad(s):
    	return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
    def encrypt(message,iv,key):
    	message = pad(message)
    	cipher = AES.new(key, AES.MODE_CBC,iv)
    	return cipher.encrypt(message)
    def decrypt(ciphertext,key,iv):
    	cipher = AES.new(key, AES.MODE_CBC,iv)
    	plaintext = cipher.decrypt(ciphertext)
    	return plaintext.rstrip(b"\0") 
    print "User %s has joined the chatroom" %(response1)
    object1="[*]User %s has joined the chatroom" %(response1)
    broadcast(conn,object1)
    while True: 
        response2=conn.recv(4096)
        decrypted_message=decrypt(response2,key,iv)
        if decrypted_message=="quit":
        	message="[*]The user %s has logged out of the chatroom" %(response1)
                print message 
                enc_message2=encrypt(message,iv,key)
                broadcast(conn,enc_message2)
                conn.send("quitted")
                client_add.remove(conn)
                break
        else:
            message="[*]The user %s has sent a message=> %s" %(response1,decrypted_message) 
            enc_message2=encrypt(message,iv,key)
            broadcast(conn,enc_message2)
    conn.close()      
for i in range(10):
    threading.Thread(target=handle_client).start()
def broadcast(connection,enc_message):
	for client_conn in client_add:
        	if client_conn!=connection:
                	try:
                        	client_conn.send(enc_message)
                        except:
                        	client_conn.close()
