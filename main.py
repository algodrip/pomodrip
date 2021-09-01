import time
from timer import Timer

def main():
    t = Timer(8)
    t.start()

    print("Starting pomodoro timer...")
    while not t.timer_is_up():
        time.sleep(1)

    print("Time's up! 🎊")
    t.stop()


if __name__ == '__main__':
    main()
