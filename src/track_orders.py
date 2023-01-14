class TrackOrders:

    def __init__(self):
        self.estoque = list()

    def __len__(self):
        return len(self.estoque)

    def add_new_order(self, customer, order, day):
        self.estoque.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        most_requested = dict()
        for order in self.estoque:
            if order[0] == customer:
                if order[1] in most_requested:
                    most_requested[order[1]] += 1
                else:
                    most_requested[order[1]] = 1
        return max(most_requested, key=most_requested.get)

    def get_never_ordered_per_customer(self, customer):
        disher = set()
        requests = set()
        for order in self.estoque:
            disher.add(order[1])
            if order[0] == customer:
                requests.add(order[1])
        return disher - requests

    def get_days_never_visited_per_customer(self, customer):
        days = set()
        visited_days = set()
        for order in self.estoque:
            days.add(order[2])
            if order[0] == customer:
                visited_days.add(order[2])
        return days - visited_days

    def get_busiest_day(self):
        day = dict()
        for order in self.estoque:
            if order[2] in day:
                day[order[2]] += 1
            else:
                day[order[2]] = 1
        return max(day, key=day.get)

    def get_least_busy_day(self):
        day = dict()
        for order in self.estoque:
            if order[2] not in day:
                day[order[2]] = 1
            else:
                day[order[2]] += 1
        return min(day, key=day.get)
