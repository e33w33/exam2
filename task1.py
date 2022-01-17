class Country:
    def __init__(self, name, president, population):
        self.name = name
        self.president = president
        self.population = population

    def __str__(self):
        return f'President of {self.name} is {self.president}, population in this country is {self.population}'


class Kyrgyzstan(Country):
    def borders(self):
        have_borders = True
        print('Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China')


class Russia(Country):
    def currency(self):
        print('National currency is Rubles')


kgz = Kyrgyzstan('Kyrgyzstan', 'Sadyr Japarov', '6.5m')
print(kgz)
kgz.borders()
print('______________________________________________')
rus = Russia('Russia', 'Vladimir Putin', '144.1m')
print(rus)
rus.currency()
