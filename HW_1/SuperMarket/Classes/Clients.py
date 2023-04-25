from abc import abstractmethod


class Actor:
    def __init__(self, name):
        self.name = name
        self.isTakeOrder = False
        self.isMakeOrder = False

    @abstractmethod
    def getName(self):
        pass


class VipClient:
    """Конструктор Vip-клиента с двумя параметрами"""
    def __init__(self, name, count, check_vip):
        self.name = name
        self.count = count
        self.check_vip = check_vip


class Market():
    def __init__(self):
        self.queue = []

    def acceptToMarket(self, actor):
        print(actor.getActor().getName() + " клиент пришел в магазин ")
        self.takeInQueue(actor)

    def takeInQueue(self, actor):
        self.queue.append(actor)
        print(actor.getActor().getName() + " клиент добавлен в очередь ")

    def releaseFromMarket(self, actors):
        for actor in actors:
            print(actor.getName() + " клиент ушел из магазина ")
            self.queue.remove(actor)

    def update(self):
        self.takeOrder()
        self.giveOrder()
        self.releaseFromQueue()

    def giveOrder(self):
        for actor in self.queue:
            if actor.isMakeOrder():
                actor.setTakeOrder(True)
                print(actor.getActor().getName() + " клиент получил свой заказ ")

    def releaseFromQueue(self):
        releaseActors = []
        for actor in self.queue:
            if actor.isTakeOrder():
                releaseActors.append(actor.getActor())
                print(actor.getActor().getName() + " клиент ушел из очереди ")
        self.releaseFromMarket(releaseActors)

    def takeOrder(self):
        for actor in self.queue:
            if not actor.isMakeOrder():
                actor.setMakeOrder(True)
                print(actor.getActor().getName() + " клиент сделал заказ ")


class OrdinaryClient(Actor):
    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        return super().name

    def isMakeOrder(self):
        return super().isMakeOrder

    def isTakeOrder(self):
        return super().isTakeOrder

    def setMakeOrder(self, makeOrder):
        super().isMakeOrder = makeOrder

    def setTakeOrder(self, pickUpOrder):
        super().isTakeOrder = pickUpOrder

    def getActor(self):
        return self


class SpecialClient(Actor):
    def init(self, name, idVIP):
        super().init(name)
        self.idVIP = idVIP

    def get_name(self):
        return super().name

    def get_id_VIP(self):
        return self.idVIP

    def is_make_order(self):
        return super().is_make_order

    def is_take_order(self):
        return super().is_take_order

    def set_make_order(self, make_order):
        super().is_make_order = make_order

    def set_take_order(self, take_order):
        super().is_take_order = take_order

    def get_actor(self):
        return self


class TaxService:
    def init(self):
        self.name = "Tax audit"
        self.isTakeOrder = False
        self.isMakeOrder = False


    def getName(self):
        return self.name

    def isMakeOrder(self):
        return self.isMakeOrder

    def isTakeOrder(self):
        return self.isTakeOrder

    def setMakeOrder(self, makeOrder):
        self.isMakeOrder = makeOrder

    def setTakeOrder(self, pickUpOrder):
        self.isTakeOrder = pickUpOrder

    def getActor(self):
        return OrdinaryClient(self.name)
