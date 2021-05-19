from threading import Thread


def show():
    count = 0
    while 1:
        count += 1
        if count == 10000000:
            print("hello world")
            count = 0


if __name__ == "__main__":
    t = Thread(target=show)
    t.start()
    while 1:
        pass
