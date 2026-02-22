class Country:
    def __init__(self, name, pop):
        self.__name = name
        self.__population = pop

    def get_name(self):
        return self.__name

    def get_population(self):
        return self.__population

    def print_info(self):
        print(f"I {self.__name} bor det {self.__population} miljoner invånare")

se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)

se.print_info()
no.print_info()


