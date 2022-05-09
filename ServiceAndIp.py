import socket


def cari_nama_service(nomor_port, protokol):
    nama_service = socket.getservbyport(nomor_port, protokol)
    print("Port %d : %s" %(nomor_port, nama_service))

def cari_ip(hostname):
    address = socket.gethostbyname(hostname)
    print('IP address %s adalah %s' %(hostname, address))
    pc = socket.gethostname()
    print('Anda mengakses dari komputer', pc)
    print('Alamat IP komputer anda adalah', socket.gethostbyname(pc))

if __name__ == '__main__':
    while(True):
        print("-------------------------Menu Pilihan-------------------------")
        print("[1] Mengetahui Service dan Protocol dari Jaringan")
        print("[2] Mengetahui alamat IP dari sebuah website")
        print("[3] Keluar")
        print("--------------------------------------------------------------")

        pilihan = ''
        try:
            pilihan = int(input('Pilih (ketikkan angka): '))
        except:
            print('Input salah, Masukkan angka')
        
        if pilihan == 1:
            cari_nama_service(int(input("Masukkan nomor port: ")), "tcp")
        elif pilihan == 2:
            cari_ip(str(input('Ketikkan website: ')))
        elif pilihan == 3:
            exit()
        else:
            print("Pilih 1-3 saja")

        
        

