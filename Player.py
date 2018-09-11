class GamePlayer():
    def __init__(self,name,point):
        self._name=name
        self._point=point

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('value must be an str!')
        self._name = value

    @property
    def point(self):
        return self._point
    @point.setter
    def point(self, value):
        if not isinstance(value, int):
            raise ValueError('value must be an int!')
        self._point = value
