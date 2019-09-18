import time
import os
import sys
import socket
import base64
import json
import re
import threading
import codecs


'''
main server has clientThread list
if connect client, make thread(Sender class) and and thread list(clientThreads)
and wait another connection from client
'''
class Client (threading.Thread):

	def __init__(self, ip, port, name, process):
		threading.Thread.__init__(self) 
		self.ip=ip
		self.port=int(port)
		self.name=name
		self.process_name = process
		self.NetworkInit()

	def NetworkInit(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print('connecting...')
		self.sock.connect((self.ip, self.port))
		print('connect complete')

		self.packet = {'IF_CODE' : 'Device', 'Client' : 'BACKEND/' + self.name, 'Type' : 'client' }
		self.NetworkWrite(self.packet)
		self.requests.clear()

	def run(self):
		self.RequestProcess()
		return


	def RequestProcess(self):
		# 서버에서 패킷 받기
		while True:
			while True:
				data=self.sock.recv(1024)

				if data:
					packet=data.decode('utf8')
					break

			packets=packet.split('<EOP')

			for str in packets:
				if str=='': break
				try:
					parse=json.loads(str)
				except:
					#print(str+'\n> ', end='')
					continue

				#실행중인 프로세스 종료 후 PC 종료.
				if parse['IF_CODE']=='SHUTDOWN':
					print(packets)
					os.system('taskkill.exe /f /im ' + self.process_name)
					os.system('shutdown -s -t 30')
					return
			
  # 테스트용 메소드
	def testRequestProcess(self):
		# 서버에서 패킷 받기
		while True:
			data=self.sock.recv(1024)

			if data:
				packet=data.decode('utf8')
				break

	def NetworkWrite(self, packet):
		str=json.dumps(packet)
		str+='<EOP>'
		#str+='python client connect'
		bytes=str.encode('utf8')
		self.sock.sendall(bytes)

def main():
	lines = codecs.open('conf.txt').readlines()

	SERVER_PORT=0
	SERVER_IP=''
	PC_NAME=''
	PROCESS_NAME=''

	for line in lines:
		name, value = line.strip().split('=')

		if name=='SERVER_PORT':
			SERVER_PORT=value
		elif name=='SERVER_IP':
			SERVER_IP=value
		elif name=='PC_NAME':
			PC_NAME=value
		elif name=='PROCESS_NAME':
			PROCESS_NAME=value

	#테스트 할때만 True
	check=True

	while check==False:
		process_list = ['System Idle Process', 'System', 'Registry', 'Memory Compression']
		regex = re.compile(".*[.]exe\s", re.I)
		all_ps = os.popen('tasklist').read()

		for process in regex.findall(all_ps) :
			# wol로 pc를 on 한 다음 자동으로 영상 프로그램 등이 실행되는 것을 확인해야 함
			if process == process_name:
				check=True
				break
	client = Client(SERVER_IP, SERVER_PORT, PC_NAME, PROCESS_NAME)
	client.start()

if __name__ == '__main__':
    main()