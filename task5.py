const_hour = 40

class Employee:
    def __init__(self, name, pin, hour) -> None:
        self.name = name
        self.pin = pin
        self.hour = hour

    def calc_salary(self):
        pass

    def total_salary(self):
        pass

    def calc_performance(self):
        return (self.hour * 100) / const_hour


class Manager(Employee):
    def __init__(self, name, pin, hour, salary) -> None:
        super().__init__(name, pin, hour)
        self.salary = salary

    def calc_salary(self):
        return self.salary


class Secretary(Employee):
    def __init__(self, name, pin, hour, salary) -> None:
        super().__init__(name, pin, hour)
        self.salary = salary

    def calc_salary(self):
        return self.salary


class Seller(Employee):
    def __init__(self, name, pin, hour, sell_count, salary) -> None:
        super().__init__(name, pin, hour)
        self.sell_count = sell_count
        self.salary = salary

    def calc_salary(self):
        return self.salary + (self.sell_count*50)


class Workshop_worker(Employee):
    def __init__(self, name, pin, hour) -> None:
        super().__init__(name, pin, hour)

    def calc_salary(self):
        self.salary = self.hour * 100
        return self.salary


class Secretary_substitute(Employee):
    def __init__(self, name, pin, hour) -> None:
        super().__init__(name, pin, hour)

    def calc_salary(self):
        self.salary = self.hour * 100
        return self.salary


manager = Manager(
    "Барсбек Канаткулов",
    1,
    18,
    45000
)
secretary = Secretary(
    "Алымкул Тилекбаев",
    2,
    38,
    20000
)
sales_person = Seller(
    "Айпери Шалымбекова",
    3,
    38,
    20,
    20000
)
ww1 = Workshop_worker(
    "Бакыт Рустамов",
    4,
    25
)
ww2 = Workshop_worker(
    "Алтынай Ширинбаева",
    5,
    40
)
sub = Secretary_substitute(
    "Жанар Рыскулов",
    6,
    33
)
personal = [
    manager,
    secretary,
    sales_person,
    ww1,
    ww2,
    sub
    ]


def spend_comp_money():
    total_money = sum([
        person.calc_salary() for person in personal
        ])
    return f"Общий заработок персонала - {total_money}"


def print_info():
    total = spend_comp_money()
    for person in personal:
        print(
            f"ID - {person.pin}, Name - {person.name} Salary - {person.salary} Performance - {person.calc_performance()}",
            end="\n"
        )
    return total


print_info()
