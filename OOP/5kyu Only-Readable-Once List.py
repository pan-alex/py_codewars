# Attention Agent.
#
# The White House is currently developing a mobile app that it can use to issue instructions to its undercover agents.
#
# Part of the functionality of this app is to have messages that can be read only once, and are then destroyed.
#
# As our best undercover developer, we need you to implement a SecureList class that will deliver this functionality.
#
# To complete this kata you need to be able to define a class that implements __getitem__(), __str__(), __repr__(), and possibly __len__().
#
# Good luck Agent.


class SecureList():
    def __init__(self, l):
        self.l = l.copy()

    def __getitem__(self, idx):
        to_print = self.l.copy()[idx]
        del self.l[idx]
        return to_print

    def __repr__(self):
        to_print = self.l.copy()
        self.l = []
        return str(to_print)

    def __str__(self):
        to_print = self.l.copy()
        self.l = []
        return str(to_print)

    def __len__(self):
        return len(self.l)

messages=SecureList([1,2,3,4])

## Examples:
# Behaviour different to the traditional list is outlined below:
#
#     Accessing an item at any index should delete the item at that index eg:
#
messages=SecureList([1,2,3,4])
messages[1]  # prints 2
print(messages)     # prints [1,3,4]
#
#     Printing the whole list should clear the whole list eg:
#
messages=SecureList([1,2,3,4])
print(messages)     # prints [1,2,3,4]
print(messages)     # prints []
#
#     Viewing the representation of the list should also clear the list eg:
#
messages=SecureList([1,2,3,4])
print("my messages are: %r."%messages)     # prints "my messages are: [1,2,3,4].
print(messages)     # prints []


base=[1,2,3,4]
a=SecureList(base)

a[0]
base[0]
a[0]
base[1]
len(a)   # 2
print("current List: %s"%a)
len(a)  # 0
a=SecureList(base)