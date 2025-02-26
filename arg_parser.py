import argparse
import sys


def main():
    #parent parser imported to import args from parent parser
    parent_parser = argparse.ArgumentParser(prog="parent_parser", description="desc for parent parser",add_help=False)
    parent_parser.add_argument("-c", type=int)

    parser = argparse.ArgumentParser(prog='demo_argument_parser',description="test script to  \n $$$$$$$$$$$ \n demo argparse",formatter_class=argparse.MetavarTypeHelpFormatter,
                                     epilog="test epilog",usage="demo_argument_parser [options]",parents=[parent_parser])
    parser.add_argument("message",type=str,default="dssfdsfdsf",help= "message for print function(positional argument)")
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
    if args.c:
        print(args.c)


def print_message(message=None):
    print(f'user provided message {message}')


def print_summation(a=0,b=0):
    print(a+b)


if __name__ == '__main__':
    main()
