class UsefulStuff:
    def __init__(self, name):
        print(name, 'is used to make life easier!')


class Watch(UsefulStuff):
    def __init__(self, watch_name):
        print(watch_name, "is small and convenient")
        #super().__init__(watch_name)


class Phone(UsefulStuff):
    def __init__(self, phone_name):
        print(phone_name, "makes a call")
        #super().__init__(phone_name)

    def make_call(self):
        print('ring-ring')


class SmartWatch(Watch, Phone):
    def __init__(self):
        print('Smartwatch is great!')
        super().__init__('Smartwatch')


# mug = UsefulStuff('mug')
# watch = Watch('Omega')
# phone = Phone('iPhone')
sw = SmartWatch()