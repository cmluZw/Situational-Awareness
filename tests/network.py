from scapy.all import *


def capture(x):
    if b'HTTP/' in x.lastlayer().original and x.lastlayer().original[0:4] != b'HTTP':
        print('dst ip:', x.payload.dst)
        print('request body:', x.lastlayer().original)


def main():
    sniff(filter="tcp", prn=lambda x: capture(x))


if __name__ == '__main__':
    main()

