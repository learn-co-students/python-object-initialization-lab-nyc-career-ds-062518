class Driver:

    def __init__(self, first, last, favorite_hobby = 'driving'):
        self._first = first
        self._last = last
        self.favorite_hobby = favorite_hobby

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

#favorite_hobby decorators
    @property
    def favorite_hobby(self):
        return self._favorite_hobby

    @favorite_hobby.setter
    def favorite_hobby(self, favorite_hobby):
        self._favorite_hobby = favorite_hobby

    @favorite_hobby.deleter
    def favorite_hobby(self):
        del self._favorite_hobby
