<<<<<<< HEAD
Its the repository for client server chatbox with AES encryption support 
Requirements are [python 2.7.9] and both the client and server python code on the machine.
Basically multithreadedserver.py sets up the server listening on a port and similarly clientlocalhost.py sets up the client to connect to that port on which server is listening , 256 bit key is provided with 16byte iv for AES encryption , you can change the key and iv  as per your requirements, the symmetrically encrypted chatroom has been given multithreading support for multiple clients to chat with each other , you just need to type "quit" to get logged out.This whole setup works on TCP connection , always preferred over udp even though slow but reliable.
ERROR:- Sometimes it might happen that port is used by some other service so make sure to change the port to any other port that is accessible. 
=======
# EncRyPto_Chat
An Encrypted client server chatbox using python with AES 256 bit encryption support.
>>>>>>> e761f47ca5c75eff4c84b51010a256bdab223d0a
