import socket 
import argparse
import json
import sys
import os
from itertools import cycle


MAX_BYTES = 65432

class Server:
	def __init__(self, interface, port):
		self.interface = interface
		self.port = port
		self.sock = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
	

	def start(self):
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADRR,1)
		self.sock.bind((self.interface, self.port))
		self.sock.listen(1)
		print('Listening at.....', self.sock.getsockname())

		

		while True:
			s, address = self.sock.accept()
			m, file1, file2 = s.recv(MAX_BYTES).decode('utf-8').split('%')
			
			if m =='change_text':
				modified_file = file1
				json_file = file2
				j_Obj = json.loads(json_file)


				for key in j_Obj:
					modified_file = modified_file.replace(key,j_Obj[key])

				s.send(modified_file.encode())


			elif m == 'encode_decode':
        			key = file2
        			xor = [chr(ord(a) ^ ord(b)) for a,b in zip(modified_file, cycle(key))]
       				xor_txt = "".join(xor)

       				s.sendall(xor_txt.encode())


			s.close()


class Client:
	MAX_BYTES = 65432

	def __init__(self,interface, interface, mode):
		self.interface = interface
		self.port = port
		self.mode = mode
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


	def change_txt(self, file1, file2):
		main_file = open(file1, 'r')
		f1_text = main_file.read()
		main_name = main_file.name.split('.txt')[0]
		main_file.close()


		j_file = open(file2,'r')
		f2_text = j_file.read()
		j_file.close()

		self.sock.sendall(str.encode('%'.join([self.mode, f1_text, f2_text])))


		changed_txt = self.sock.recv(self.MAX_BYTES)
		new_file = open(main_name + '_changed' +'.txt', wb)
		new_file.write(changed_text)
		new_file.close()


	def en_dec(self,file1, file2):
		plaintext_f = open(file1, "r")
		plaintext = plaintext_f.read()
		plain_name = plaintext_f.name.split('.txt')[0]
		plaintext_f.close()

		key_f = open(file2,"r")
		key_txt = key_f.read()
		key_f.close()


		self.sock.sendall(str.encode('%'.join([self.mode, plaintext, key_txt])))



		changed_text = self.sock.recv(self.MAX_BYTES)
		changed_f = open("new_file" + ".txt", "wb")
		changed_f.write(changed_text)
		changed_f.close()


	def start(self,file1,file2):
		self.sock.connect((self.interface,self.port))

		print('Client has been assigned socket name', self.sock.getsockname())
        
        if self.mode == "change_text":
            self.case_1(file1,file2)
    	elif self.mode == "encode_decode": 
    		self.case_2(file1,file2)

		


if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "TCP")
    choices = {"server": Server, "client": Client}
    parser.add_argument('role', choices = choices, help = "server or client")
    parser.add_argument("--interface", default='127.0.0.1' help="IP address")
    parser.add_argument("-p", metavar="PORT", type=int, default=5432, help="Port (default 5432)")
    
    if sys.argv[1] == "client":
        parser.add_argument('--mode', type = str,help="mode (change_text or encode_decode)")
        parser.add_argument('file1', type = str, help = "1st filename")
        parser.add_argument('file2', type = str, help = "2nd filename")
    
    args = parser.parse_args()
    class_n = choices[args.role]

    if args.role == "client":
        obj = class_n(args.interface, args.p,args.mode)
        obj.start(args.file1, args.file2)
    elif args.role == "server":
        obj = class_n(args.interface,args.p)
        obj.start()
