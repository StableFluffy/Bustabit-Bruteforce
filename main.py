import hashlib
import random
import time
from multiprocessing import Process, Queue

THREADS = 4

def program(cc):
    TARGET = "3ba12a9bc2deba608d678a2a449ca7874c4df22588eb593e5150b6f3caf9f81d" #Game 5728987
    STRING_POOL = "1234567890abcdef"

    generated_seed = ""
    for i in range(64):
        generated_seed += random.choice(STRING_POOL)
    print("Start Searching at :", generated_seed)

    seed = generated_seed

    start = time.time()

    # Looperino starting here
    for i in range(1000000):

        seed = hashlib.sha256(seed.encode()).hexdigest()
        # print(seed)

        if seed == TARGET:
            print("Found Target !", seed, "at seed :", generated_seed, "at x st :", i)
            end = time.time()
            with open('hit.txt', 'a') as f:
                f.write(f'\n{generated_seed} {i} {TARGET}')
            print(f"It took {end - start}")
            return

    end = time.time()

    print(f"Failed at seed {generated_seed} and took {end - start} sec")

    program("c")


if __name__ == '__main__':
    procs = []
    for i in range(THREADS):
        vysbufdi = Process(target=program, args=str(i))
        procs.append(vysbufdi)
        vysbufdi.start()

    for proc in procs:
        proc.join()
