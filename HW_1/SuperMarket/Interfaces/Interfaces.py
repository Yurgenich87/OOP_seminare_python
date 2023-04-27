from abc import abstractmethod
from HW_1.SuperMarket.Classes.Clients import Actor


class ActorBehaviour(Actor):
    @abstractmethod
    def setMakeOrder(self, makeOrder: bool):
        pass

    @abstractmethod
    def setTakeOrder(self, pickUpOrder: bool):
        pass

    @abstractmethod
    def isMakeOrder(self) -> bool:
        pass

    @abstractmethod
    def isTakeOrder(self) -> bool:
        pass

    @abstractmethod
    def getActor(self) -> Actor:
        pass


class MarketBehaviour(Actor):
    @abstractmethod
    def acceptToMarket(self, actor):
        pass

    @abstractmethod
    def releaseFromMarket(self, actors: List):
        pass

    @abstractmethod
    def update(self):
        pass


class QueueBehaviour(Actor):
    @abstractmethod
    def takeInQueue(self, actor):
        pass

    @abstractmethod
    def releaseFromQueue(self):
        pass

    @abstractmethod
    def takeOrder(self):
        pass

    @abstractmethod
    def giveOrder(self):
        pass
