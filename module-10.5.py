import os
from time import monotonic
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    folders_path = './files'
    filenames = [
        os.path.join(folders_path, file)
        for file in os.listdir(folders_path)
        if os.path.isfile((os.path.join(folders_path, file)))
                 ]

    start_time = monotonic()
    for filename in filenames:
        read_info(filename)
    end_time = monotonic()
    print(f"Линейный вызов: {end_time - start_time:.2f} сек")

    start_time = monotonic()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = monotonic()
    print(f"Многопроцессный вызов: {end_time - start_time:.2f} сек")