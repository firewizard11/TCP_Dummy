import argparse
from classes import TCPClient, TCPServer


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        add_help=False,
        usage='main.py [--help] mode options'
    )

    parser.add_argument('--help', action='help')

    subparsers = parser.add_subparsers(title='mode', dest='mode')

    # Client Options
    c_parser = subparsers.add_parser('client', add_help=False)
    c_parser.add_argument('--help', action='help')
    c_parser.add_argument('-h', '--host', help='The IPv4 Address of the Host to connect to')
    c_parser.add_argument('-p', '--port', type=int, help='The port to connect to on the host')
    c_parser.add_argument('-i', '--interactive', action='store_true', help='Will keep connection open and allow you to send and receive messages like a text chat')
    c_parser.add_argument('-d', '--data', help='The argument for this option will be sent to the host')
    c_parser.add_argument('-r', '--reply', action='store_true', help='Setting this option will make the client wait for the host response before disconnecting')

    # Server Options
    s_parser = subparsers.add_parser('server', add_help=False)
    s_parser.add_argument('--help', action='help')

    args = parser.parse_args()

    match args.mode:
        case 'client':
            client = TCPClient()
            host = args.host
            port = args.port
            interactive = args.interactive
            reply = args.reply

            if args.data:
                data = args.data
            else:
                data = None

            client.start_connection(host, port)
            if interactive:
                client.interactive_session()

            if data:
                client.send_data(data)

            if reply:
                client.receive_data()

        case 'server':
            pass

        case _:
            parser.print_help()
        
