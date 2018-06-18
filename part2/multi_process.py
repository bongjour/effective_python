import multiprocessing
import time


def clock(interval):
    while True:
        print("The time is %s" % time.ctime())
        time.sleep(interval)


class ClockProcess(multiprocessing.Process):

    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print("The time is %s " % time.ctime())
            time.sleep(self.interval)


if __name__ == "__main__":
    # p = multiprocessing.Process(target=clock, args=(15,))
    # print(p.pid)
    # p.start()

    p = ClockProcess(5)
    p.start()
