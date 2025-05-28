import argparse
import socket


class Client:

    def __init__(self, timeout: int = -1):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timeout = timeout
        self.connected = False

    def start_connection(self, host: str, port: int):
        if self.timeout > -1:
            self.sock.settimeout(self.timeout)

        try:
            self.sock.connect((host, port))
            self.connected = True
            print('[+] Connection Success')
        except TimeoutError:
            print('[!] Connection Timeout')
        except ConnectionRefusedError:
            print('[!] Connection Refused')

    def interactive_session(self):
        if not self.connected:
            print('[!] No Active Connection')

        while True:
            data = input("$ ")
            if data == 'quit':
                break

            print(data)

            b_data = data.encode()
            
            self.sock.sendall(b_data + b'\n')

            while True:
                try:
                    response = self.sock.recv(4096)
                    print(response)
                    continue
                except TimeoutError:
                    break

    def __del__(self):
        self.sock.close()


if __name__ == '__main__':
    test = Client(timeout=5)
    test.start_connection('172.19.218.20', 4444)
    test.interactive_session()