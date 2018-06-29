class Passenger:

    def __init__(self, first, last, email, rides_taken=0):
        self._first = first
        self._last = last
        self._email = email
        self._rides_taken = rides_taken

#first_name_decorators
    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first):
        self._first = first

    @first.deleter
    def first(self):
        del self._first

#last_name_decorators
    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last):
        self._last = last

    @last.deleter
    def last(self):
        del self._last

#email decorators
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @email.deleter
    def email(self):
        del self._email

#rides_taken decorators

    @property
    def rides_taken(self):
        return self._rides_taken

    @rides_taken.setter
    def rides_taken(self, rides_taken):
        self._rides_taken = rides_taken

    @rides_taken.deleter
    def rides_taken(self):
        del self._rides_taken
