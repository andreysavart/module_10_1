import threading
from time import sleep, time, strftime, gmtime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Функция для измерения времени выполнения
def measure_time(func, *args):
    start_time = time()
    func(*args)
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Работа функции {func.__name__} заняла {strftime('%H:%M:%S', gmtime(elapsed_time))}")

# Вызов функций без потоков
measure_time(write_words, 10, 'example1.txt')
measure_time(write_words, 30, 'example2.txt')
measure_time(write_words, 200, 'example3.txt')
measure_time(write_words, 100, 'example4.txt')

# Создание и запуск потоков
threads = []

start_time = time()

for args in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = threading.Thread(target=write_words, args=args)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time()
elapsed_time = end_time - start_time
print(f"Работа потоков заняла {strftime('%H:%M:%S', gmtime(elapsed_time))}")
