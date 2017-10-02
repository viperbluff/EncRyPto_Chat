[EncRyPto_chat] Version -> 1.0 @tikoo_sahil
--------------------------------------------
Client Server chatbox with AES encryption support 
Requirements are [python 2.7.9] and both the client and server python code on the machine.
Basically multithreadedserver.py sets up the server listening on a port and similarly clientlocalhost.py sets up the client to connect to that port on which server is listening by providing ip address of the server and port, 256 bit key is provided with 16byte iv for AES encryption , you can change the key and iv  as per your requirements, the symmetrically encrypted chatroom has been given multithreading support for multiple clients to chat with each other , you just need to type "quit" to get logged out.This whole setup works on TCP connection , always preferred over udp even though slow but reliable.
# At a time 10 clients can be connected to the server simultaneously to chat.
ERROR:- Sometimes it might happen that port is used by some other service so make sure to change the port to any other port that is accessible. 
