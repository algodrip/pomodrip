import time
from timer import Timer

def main():
    t = Timer()
    t.start()

    print("Starting pomodoro timer...")
    elapsed_seconds = 0
    while elapsed_seconds < 8:
        elapsed_seconds = time.perf_counter() - t._start_time
        time.sleep(0.1)

    t.stop()


if __name__ == '__main__':
    main()
