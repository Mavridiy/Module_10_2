import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Начальное количество врагов
        self.days = 0  # Счетчик дней

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            time.sleep(1)  # Задержка в 1 секунду (1 день)
            self.days += 1
            self.enemies -= self.power

            # Убедимся, что количество врагов не становится отрицательным
            if self.enemies < 0:
                self.enemies = 0

            print(f"{self.name} сражается {self.days}..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} {'дней' if self.days > 1 else 'день'}!")



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()
second_knight.start()

# Ждем завершения обоих потоков
first_knight.join()
second_knight.join()

print("Все битвы окончены!")