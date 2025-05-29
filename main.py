import argparse
import socket


class Client:

    def __init__(self, timeout: int = -1):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.timeout = timeout
        self.connected = False

    def start_connection(self, host: str, port: int) -> None:
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

    def send_data(self, data: str) -> None:
        if not self.connected:
            print('[!] No Active Connection')
            return None
        
        self.sock.sendall(data.encode())
        print('[+] Data Transfer Success')

    def receive_data(self) -> None:
        print('[*] Waiting for data...')
        
        while True:
            try:
                response = self.sock.recv(4096)
                print(response)
                continue
            except TimeoutError:
                break

    def interactive_session(self) -> None:
        if not self.connected:
            print('[!] No Active Connection')
            return None

        while True:
            data = input("$ ")
            if data == 'quit':
                break

            self.send_data(data)
            self.receive_data()

    def __del__(self):
        self.sock.close()


if __name__ == '__main__':
    pass