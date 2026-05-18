class Phone:
    def __init__(self, brand, storage, battery):
        self.brand = brand
        self.storage = storage
        self.battery = battery
        self.apps = []

    def info(self):
        print(self.brand)
        print(self.storage)
        print(self.battery)

    def install(self, app):
        self.apps.append(app)
        print(app, "o'rnatildi")

    def delete(self, app):
        if app in self.apps:
            self.apps.remove(app)
            print(app, "o'chirildi")

    def show_apps(self):
        for a in self.apps:
            print(a)

    def charge(self):
        self.battery = 100
        print("Zaryad to'ldi")

    def call(self):
        print("Qo'ng'iroq")

    def sms(self):
        print("SMS yuborildi")

    def internet(self):
        print("Internet yoqildi")

    def reset(self):
        self.apps.clear()
        print("Telefon tozalandi")


p1 = Phone("Samsung", 128, 60)

p1.info()
p1.install("Telegram")
p1.install("Instagram")
p1.show_apps()
p1.call()
p1.sms()
p1.internet()
p1.delete("Telegram")
p1.reset()