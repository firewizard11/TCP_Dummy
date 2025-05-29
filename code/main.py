import argparse
from classes import TCPClient, TCPServer


if __name__ == '__main__':
    TARGET1 = '172.19.218.20'
    TARGET2 = '127.0.0.1'
    PORT = 4444

    test_client = TCPClient(3)
    test_client.start_connection(TARGET1, PORT)
    test_client.interactive_session()
    test_client.close_connection()

    test_client.start_connection(TARGET2, PORT)
    test_client.send_data(f'GET / HTTP/1.1\nHost: {TARGET2}\n\n')
    test_client.receive_data()
