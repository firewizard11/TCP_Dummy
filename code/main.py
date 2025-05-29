import argparse
import socket

from classes import TCPClient


if __name__ == '__main__':
    test = TCPClient(timeout=5)
    test.start_connection('172.19.218.20', 4444)
    test.send_data('Hello, World!')
    test.receive_data()

    test.start_connection('127.0.0.1', 4444)