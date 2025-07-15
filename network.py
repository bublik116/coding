class Packet:
    def __init__(self, src, dst, data):
        self.src = src      # MAC-адрес отправителя
        self.dst = dst      # MAC-адрес получателя
        self.data = data    # Сообщение

    def is_broadcast(self):
        """Проверяет, является ли пакет широковещательным"""
        return self.dst == "FF:FF:FF:FF:FF:FF"

    def __repr__(self):
        return f"Packet(src={self.src}, dst={self.dst}, data='{self.data}')"


class Computer:
    def __init__(self, mac_address, router=None):
        self.mac = mac_address   # Теперь используем MAC вместо имени
        self.router = router

        if router:
            router.connect(self)

    def send(self, dst, data):
        packet = Packet(self.mac, dst, data)
        if self.router:
            self.router.route(packet)
        else:
            print(f"{self.mac}: Нет подключенного роутера для отправки сообщения.")

    def receive(self, packet):
        print(f"[{self.mac}] Получено от {packet.src}: {packet.data}")


class Router:
    def __init__(self):
        self.devices = {}  # Ключ — MAC-адрес устройства

    def connect(self, device):
        if device.mac in self.devices:
            print(f"[Роутер] Устройство {device.mac} уже подключено.")
        else:
            self.devices[device.mac] = device
            print(f"[Роутер] Устройство {device.mac} успешно подключено.")

    def route(self, packet):
        if packet.is_broadcast():
            print(f"[Роутер] Рассылка широковещательного пакета от {packet.src}")
            for mac, device in self.devices.items():
                if mac != packet.src:  # Не отправляем себе же
                    device.receive(packet)
        else:
            if packet.dst in self.devices:
                self.devices[packet.dst].receive(packet)
            else:
                print(f"[Роутер] Получатель '{packet.dst}' не найден.")
                
                
                
# Создаем роутер
router = Router()

# Создаем компьютеры с MAC-адресами
pc1 = Computer("00:1A:2B:3C:4D:5E", router)
pc2 = Computer("00:1A:2B:3C:4D:5F", router)
pc3 = Computer("00:1A:2B:3C:4D:60", router)
pc4 = Computer("00:1A:2B:3C:4D:61", router)


# Широковещательный адрес — FF:FF:FF:FF:FF:FF
pc1.send("FF:FF:FF:FF:FF:FF", "Привет всем от PC1!")
