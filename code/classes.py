from socket import socket, AF_INET, SOCK_STREAM


class TCPClient:
    
    def __init__(self, timeout: int = -1):
        self.sock = None
        self.connected = False
        self.timeout = timeout
        print('[+] Created Client')

    def start_connection(self, host: str, port: int) -> None:
        if self.is_connected():
            self.close_connection()

        self._create_socket()

        try:
            self.sock.connect((host, port))
            self.connected = True
            print(f'[+] Connection Success ({host}:{port})')
        except:
            print(f'[!] Connection Failed ({host}:{port})')

    def close_connection(self) -> None:
        if not self.is_connected():
            print('[!] No Active Connection')
            return None

        self._close_socket()
        self.connected = False
        print('[+] Connection Closed')

    def is_connected(self) -> bool:
        return self.connected

    def send_data(self, data: str) -> None:
        print('[*] Sending data...')
        self.sock.sendall(data.encode())
        print('[+] Data Sent!')

    def receive_data(self) -> None:
        print('[*] Waiting for response...')

        while True:
            try:
                response = self.sock.recv(4096)
                if len(response) == 0:
                    break

                print('[+] Received Data')
                print(response.decode())
            except:
                break

    def interactive_session(self):
        if not self.is_connected():
            print('[!] No Active Connection')
            return None

        while True:
            data = input('$ ')

            if data == 'quit':
                break
                
            self.send_data(data)
            
            self.receive_data()

    def _create_socket(self):
        self.sock = socket(AF_INET, SOCK_STREAM)

        if self.timeout > -1:
            self.sock.settimeout(self.timeout)

    def _close_socket(self):
        self.sock.close()
        self.sock = None

    def __del__(self):
        if self.sock is not None:
            self._close_socket()


class TCPServer:
    
    def __init__(self, ip: str = ''):
        self.ip = ip
        self.open_ports: dict[int,socket] = dict()

    def start_listener(self, port: int) -> None:
        self.open_ports[port] = socket(AF_INET, SOCK_STREAM)
        current_port = self.open_ports[port]

        current_port.bind((self.ip, port))
        current_port.listen(5)

        while True:
        
            conn, in_addr = current_port.accept()

            print(f'[+] Connection From {in_addr[0]}:{in_addr[1]}')

            while True:
                request = conn.recv(4096).decode()

                if len(request) == 0:
                    break

                print(request)


if __name__ == '__main__':
    test_server = TCPServer()
    test_server.start_listener(4444)