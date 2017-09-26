import socket,os,sys
import threading 
from Crypto.Cipher import AES
target_host="192.168.43.195"
target_port=5009
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
response1=client.recv(1024)
print response1
b=raw_input("Enter your name:")
client.send(b)
ok=client.recv(4096)
print ok
key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
iv = "abcdefghijklmnop"
def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
def encrypt(message,iv,key,key_size=256):
    message = pad(message)
    cipher = AES.new(key, AES.MODE_CBC,iv)
    return cipher.encrypt(message)
def decrypt(ciphertext,key,iv):
    	cipher = AES.new(key, AES.MODE_CBC,iv)
    	plaintext = cipher.decrypt(ciphertext)
    	return plaintext.rstrip(b"\0")
def message_send():
	while True:
                a=raw_input("[::Enter Message to send to everyone::]")
                encrypted_message=encrypt(a,iv,key)
    		if(a=="quit"):
                        print "\n[You are Logged out from chat room]"
        		client.close()
    		else:
        		client.send(encrypted_message)
        client.close() 
def message_response():
        while True:
        	response=client.recv(4096)
                decrypted_message=decrypt(response,key,iv)
                print "\n%s" %(decrypted_message)
                print "::Type [Below] to send message to everyone::"
	client.close()
for i in range(5):
	threading.Thread(target=message_send).start()
        threading.Thread(target=message_response).start()
