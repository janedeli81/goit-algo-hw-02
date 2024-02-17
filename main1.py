from queue import Queue
import time

# Ініціалізація черги
request_queue = Queue()

# Глобальний лічильник для унікальних номерів заявок
request_counter = 0

def generate_request():
    global request_counter
    request_counter += 1
    print(f"Генеруємо заявку #{request_counter}")
    request_queue.put(f"Заявка #{request_counter}")

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляємо {request}")
    else:
        print("Черга пуста")

def main_loop():
    for _ in range(5):  # Симуляція генерації та обробки 5 заявок
        generate_request()
        time.sleep(1)  # Імітація часу на генерацію заявки
        process_request()
        time.sleep(1)  # Імітація часу на обробку заявки

if __name__ == "__main__":
    main_loop()
