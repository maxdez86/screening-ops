import random
import time


def sleep_random():
    """Sleep a random number of seconds between 20 and 40 and return 'ok'."""
    seconds = random.randint(20, 40)
    time.sleep(seconds)
    return "ok"
