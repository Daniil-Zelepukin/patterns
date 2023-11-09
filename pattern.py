#Singleton (одиночка)

class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  

print ("---------------------")

#Observer (наблюдатель)

class Observable:
    def __init__(self):
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def notify_observers(self, message):
        for observer in self.observers:
            observer(message)


def observer(message):
    print(f"Received message: {message}")

observable = Observable()
observable.add_observer(observer)
observable.notify_observers("Hello!")

print ("---------------------")

#Strategy (стратегия)

class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using credit card")


class PayPalPaymentStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")


class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_payment(self, amount):
        self.strategy.pay(amount)


if __name__ == "__main__":
    payment_context = PaymentContext(CreditCardPaymentStrategy())
    payment_context.execute_payment(100)

    payment_context.strategy = PayPalPaymentStrategy()
    payment_context.execute_payment(50)

print ("---------------------")

#Adapter (адаптер)

class Adaptee:  
    def specific_request(self):
        return "Specific request"

class Target: 
    def request(self):
        return "General request"

class Adapter(Target):  
    def __init__(self, adaptee):
        self.adaptee = adaptee
    
    def request(self):
        return f"Adapter: {self.adaptee.specific_request()}"


adaptee = Adaptee()
adapter = Adapter(adaptee)
result = adapter.request()
print(result)  