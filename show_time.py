import time
import datetime


def test_time():
    while True:
        # print('\rВремя: {}'.format(datetime.datetime.now().strftime('%H:%M:%S.')), end='')
        print(f"\rВремя: {datetime.datetime.now().strftime('%H:%M:%S')}", end='')
        time.sleep(1)


if __name__ == "__main__":
    test_time()
