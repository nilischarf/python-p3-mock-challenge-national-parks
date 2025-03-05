class NationalPark:

    all_parks = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Park must be a string of at least 3 characters.")
        if hasattr(self, '_name'):
            raise AttributeError("Cannot change NationalPark name after instantiation")
        self._name = name
        NationalPark.all_parks.append(self)

    @property
    def name(self):
        return self._name

    def trips(self):
        return [trip for trip in Trip.all_trips if trip.national_park == self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        if not self.trips():
            return None
        visitor_count = {}
        for trip in self.trips():
            visitor_count[trip.visitor] = visitor_count.get(trip.visitor, 0) + 1
        return max(visitor_count, key=visitor_count.get)

    @classmethod
    def most_visited(cls):
        if not cls.all_parks:
            return None
        return max(cls.all_parks, key=lambda park: park.total_visits(), default=None)


class Visitor:

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (1 <= len(new_name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = new_name

    def trips(self):
        return [trip for trip in Trip.all_trips if trip.visitor == self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        if not isinstance(park, NationalPark):
            raise TypeError("Argument must be an instance of NationalPark")
        return sum(1 for trip in self.trips() if trip.national_park == park)


class Trip:

    all_trips = []

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise TypeError("Visitor must be an instance of Visitor class.")
        if not isinstance(national_park, NationalPark):
            raise TypeError("NationalPark must be an instance of NationalPark class.")
        self._visitor = visitor
        self._national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all_trips.append(self)

    @property
    def visitor(self):
        return self._visitor

    @property
    def national_park(self):
        return self._national_park

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise ValueError("Start date must be a string at least 7 characters long.")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise ValueError("End date must be a string at least 7 characters long.")
        self._end_date = value