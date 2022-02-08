BRIDGE_FEE = 15
TAG_PRICE = 30


class BridgeNoMoney(Exception):
    def __init__(self, name, message='has no money to pass the bridge'):
        self.message = message
        self.name = name
        self.custom_message = f'{name} {message}'

    def __str__(self):
        return self.custom_message


class Person:
    def __init__(self, name, money, tag=False):
        self.name = name
        self.money = money
        self.tag = tag

    @property
    def get_balance(self):
        return self.money

    @property
    def get_tag(self):
        return self.tag


def fare(func):
    def inner(person):
        if person.get_balance >= BRIDGE_FEE and person.get_tag:
            person.money -= BRIDGE_FEE
        elif person.get_balance >= BRIDGE_FEE and not person.get_tag:
            if person.get_balance >= BRIDGE_FEE + TAG_PRICE:
                person.money -= BRIDGE_FEE + TAG_PRICE
                person.tag = True
            else:
                raise BridgeNoMoney(person.name)
        else:
            raise BridgeNoMoney(person.name)
        return func(person)

    return inner


@fare
def bridge(person):
    print(f'{person.name} passed the bridge with enough money. Current balance: {person.get_balance}. Tag: {person.get_tag}')


if __name__ == '__main__':
    anna = Person(name='Anna', money=50, tag=True)
    bridge(anna)
