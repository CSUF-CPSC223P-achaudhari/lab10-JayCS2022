import threading
import time
import json

def bot_clerk(items):
    cart = []
    fetcher = {1: [], 2: [], 3: []}
    for i, item in enumerate(items, start=1):
        fetcher[i % 3 + 1].append(item)
    threads = []
    for i in range(1, 4):
        thread = threading.Thread(target=bot_fetcher, args=(fetcher[i], cart, threading.Lock()))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return cart

def bot_fetcher(items, cart, lock):
    f = open('inventory.dat', 'r')
    file = json.load(f)
    f.close()
    for item in items:
        time.sleep(file[item][1])
        with lock: cart.append([item, file[item][0]])