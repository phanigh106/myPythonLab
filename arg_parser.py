import argparse
import sys


def main():
    parser = argparse.ArgumentParser(prog='demo argument parser',description="test script to demo argparse",
                                     epilog="test epilog")
    parser.add_argument("-m","--message",help= "message for print function")
    parser.add_argument("-a",type=int,help="first value")
    parser.add_argument("-b", type=int,help="second value")
    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)
    args=parser.parse_args()
    if args.message:
        print_message(message=args.message)
    if args.a and args.b:
        print_summation(a=args.a,b=args.b)


def print_message(message=None):
    print(f'user provided message {message}')


def print_summation(a=0,b=0):
    print(a+b)


if __name__ == '__main__':
    main()
