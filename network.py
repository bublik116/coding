class Packet:
    def __init__(self, src, dst, data):
        self.src = src      # Имя отправителя
        self.dst = dst      # Имя получателя
        self.data = data    # Сообщение

    def __repr__(self):
        return f"Packet(src={self.src}, dst={self.dst}, data={self.data})"


class Computer:
    def __init__(self, name, router=None):
        self.name = name         # Имя компьютера
        self.router = router     # Ссылка на роутер

        if router:
            router.connect(self)

    def send(self, dst, data):
        """Создаёт пакет и отправляет его через роутер"""
        packet = Packet(self.name, dst, data)
        if self.router:
            self.router.route(packet)
        else:
            print(f"{self.name}: Нет подключенного роутера для отправки сообщения.")

    def receive(self, packet):
        """Получает пакет и выводит сообщение в консоль"""
        print(f"{self.name} получил от {packet.src}: {packet.data}")


class Router:
    def __init__(self):
        self.devices = {}  # Словарь подключенных устройств: {name: device}

    def connect(self, device):
        """Подключает устройство к роутеру"""
        if device.name in self.devices:
            print(f"{device.name} уже подключен.")
        else:
            self.devices[device.name] = device
            print(f"{device.name} успешно подключен к роутеру.")

    def route(self, packet):
        """Пересылает пакет получателю, если он подключен к этому роутеру"""
        if packet.dst in self.devices:
            self.devices[packet.dst].receive(packet)
        else:
            print(f"Роутер: Получатель '{packet.dst}' не найден среди подключённых устройств.")
            
            
            
# Создаем роутер
router = Router()

# Создаем компьютеры и подключаем их к роутеру
comp1 = Computer("Alice", router)
comp2 = Computer("Bob", router)

# Отправляем сообщение от Alice к Bob
comp1.send("Bob", "Привет, Боб!")

# Попробуем отправить сообщение несуществующему получателю
comp2.send("Charlie", "Тестовое сообщение")            
