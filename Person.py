__author__ = 'scorpion'


class Event:

    def __init__(self, date, type, cell_id, lac):
        self._date = date
        self._type = type
        self._cell_id = cell_id
        self._lac = lac

    def __le__(self, other):
        return self._date < other._date

    def __str__(self):
        return ",".join([self._date, self._type, self._cell_id, self._lac])

    def __repr__(self):
        return "'" + str(self) + "'"

    def get_cell_with_lac(self):
        return int(self._cell_id), int(self._lac)


class Person:

    def __init__(self, user_id):
        self._user_id = user_id
        self._events = []

    def add_event(self, row_event):
        event_component = row_event.split(",")

        # event_component[-1] == self._user_id
        if event_component[-1] != self._user_id:
            return False
        self._events.append(Event(*event_component[:-1]))
        return True


def main():
    pass

if __name__ == "__main__":
    main()
