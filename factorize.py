import time
from multiprocessing import Pool


def factorize(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


if __name__ == '__main__':
    start_time = time.time()

    with Pool() as pool:
        factorizations = pool.map(factorize, [128, 255, 99999, 10651060])

    end_time = time.time()
    running_time = end_time - start_time

    print(*factorizations)
    print('Time:', running_time)

    assert factorizations[0] == [1, 2, 4, 8, 16, 32, 64, 128]
    assert factorizations[1] == [1, 3, 5, 15, 17, 51, 85, 255]
    assert factorizations[2] == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert factorizations[3] == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790,
                 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]