
import argparse
import threading
import sys
from timer import Timer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    length_parser = subparsers.add_parser("length")
    length_parser.add_argument("seconds", nargs=1)
    subparsers.add_parser("start")
    subparsers.add_parser("stop")
    subparsers.add_parser("exit")

    help = """[TBA]
    """
    print(help)

    seconds = 60
    while True:
        user_input = input(">>> ")

        try:
            args = parser.parse_args(user_input.split())
        except SystemExit:
            continue

        if args.command == "length":
            seconds = args.seconds
        elif args.command == "start":
            timer = Timer(seconds)
            timer_thread = threading.Thread(target=timer.start)
            timer_thread.start()
        elif args.command == "stop":
            timer.stop()
        elif args.command == "exit":
            sys.exit("Exiting...")