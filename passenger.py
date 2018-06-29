class Passenger:
    def __init__(self, first, last, email, rides_taken = 0):
        self._rides_taken = rides_taken
        self._first = first
        self._last = last
        self._email = email

    @property
    def first(self):
        return self._first
    @first.setter
    def first(self, name):
        self._first = name
    @first.deleter
    def first(self):
        del self._first

    @property
    def last(self):
        return self._last
    @last.setter
    def last(self, name):
        self._last = name
    @last.deleter
    def last(self):
        del self._last

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, name):
        self._email = name
    @email.deleter
    def email(self):
        del self._email

    @property
    def rides_taken(self):
        return self._rides_taken
    @rides_taken.setter
    def rides_taken(self, name):
        self._rides_taken = name
    @rides_taken.deleter
    def rides_taken(self):
        del self._rides_taken
