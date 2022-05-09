import socket

host = socket.gethostname()
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        pesan = s.recv(1024)
        pesan = pesan.decode()
        print('Pesan yang dikirim oleh server:',pesan)
        pesan = input(str("Berikan balasan: "))
        s.send(pesan.encode())