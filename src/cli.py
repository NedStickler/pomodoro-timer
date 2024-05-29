
import argparse
import sys
from timers import PomodoroTimer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    length_parser = subparsers.add_parser("set")
    length_parser.add_argument("seconds", nargs="?", type=int)
    subparsers.add_parser("start")
    subparsers.add_parser("stop")
    subparsers.add_parser("reset")
    subparsers.add_parser("remaining")
    subparsers.add_parser("exit")

    help = """[TBA]
    """
    print(help)

    timer = PomodoroTimer(10, 3)
    while True:
        user_input = input(">>> ")

        try:
            args = parser.parse_args(user_input.split())
        except SystemExit:
            continue
        
        if args.command == "set":
            timer.set_time(args.seconds)
        elif args.command == "start":
            timer.start()
        elif args.command == "stop":
            timer.stop()
        elif args.command == "reset":
            timer.reset()
        elif args.command == "remaining":
            print(timer.get_time_left())
        elif args.command == "exit":
            sys.exit("Exiting...")