from functools import lru_cache
from time import sleep

@lru_cache(maxsize=None)
def cached_func(data):
    sleep(2)
    return(data)
    # print(data) -> this wont get executed ?

print(cached_func(1))
print(cached_func(2))
print("Cached")
print(cached_func(1))
print(cached_func(2))