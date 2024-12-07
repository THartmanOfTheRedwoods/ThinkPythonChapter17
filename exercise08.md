# What's Wrong w/ This Code

```python
class Kangaroo:
    """A Kangaroo is a marsupial."""
    
    def __init__(self, name, contents=[]):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        self.contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.contents.append(item)
```

* When you do the following:

```python
kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')

kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)

print(roo)
```

* Both print statements print out, erronously the pouch:

```text
Kanga has pouch contents:
    'wallet'
    'car keys'
    <__main__.Kangaroo object at 0x7f44f9b4e500>
    
 Roo has pouch contents:
    'wallet'
    'car keys'
    <__main__.Kangaroo object at 0x7f44f9b4e500>
```

* Here's why!
    * The optional `contents=[]` parameter in the `__init__` method defines the empty list object for `contents` when the method is defined. Thus, any call to `__init__` without the contents of a list provided, will point the Kangaroo object at the same list object erroneously. Thus, when you add the contents to kanga's pouch, your only added to 1 contents object, but it is shared by both the kanga and roo objects.