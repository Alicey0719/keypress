import sys
import pydirectinput
from collections import deque

def keyDown(key):
    pydirectinput.keyDown(key)

def main():
    argv = deque(sys.argv)
    argv.popleft()

    if len(argv) > 0:
        try:
            while True:
                for k in argv:
                    print(k)
                    keyDown(k)
        except KeyboardInterrupt:
            print('exit')

if __name__ == '__main__':
    main()