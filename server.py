from pstats import SortKey
import socket

host = socket.gethostname()
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    print('Menunggu koneksi...')
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            pesan = input(str("Ketikkan pesan yang akan dikirim "))
            conn.send(pesan.encode())
            pesan = conn.recv(1024)
            pesan = pesan.decode()
            print('Pesan balasan yang diterima:', pesan)