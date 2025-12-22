class Car:
    def __init__(self, make, model, trunk, engine_volume, year, fuel_efficiency):
        self.make = make
        self.model = model
        self.trunk = trunk
        self.engine_volume = engine_volume
        self.engine = engine_volume
        self.year = year
        self.fuel_efficiency = fuel_efficiency

    def __str__(self):
        return f"Автомобіль: {self.year} {self.make} {self.model}, двигун {self.engine_volume}л."

    def __repr__(self):
        return (f"Car(make='{self.make}', model='{self.model}', year={self.year}, "
                f"engine_volume={self.engine_volume}, fuel_efficiency={self.fuel_efficiency})")

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.make == other.make and self.model == other.model

    def calculate_fuel_consumption(self, distance_km):
        return (self.fuel_efficiency / 100) * distance_km

    def shift_gear(self, gear):
        print(f"Перемикаємо передачу на: {gear}")

    def info(self):
        print(f"Год: {self.year}, Объем двигателя: {self.engine}, Багажник: {self.trunk}")


class Sedan(Car):
    def info(self):
        print(f"Sedan - Год: {self.year}, Объем двигателя: {self.engine}, Багажник: {self.trunk}")


class Jeep(Car):
    def __init__(self, make, model, trunk, engine_volume, year, fuel_efficiency,
                 max_speed, num_doors, horsepower):
        super().__init__(make, model, trunk, engine_volume, year, fuel_efficiency)
        self.max_speed = max_speed
        self.num_doors = num_doors
        self.horsepower = horsepower

    def info(self):
        print(f"Jeep - Год: {self.year}, Объем двигателя: {self.engine}, Багажник: {self.trunk}, "
              f"Макс. скорость: {self.max_speed}, Дверей: {self.num_doors}, Лошадиные силы: {self.horsepower}")


if __name__ == '__main__':

    sedan1 = Sedan("Honda", "Accord", 550, 2.4, 2009, 8.5)
    jeep1 = Jeep("Jeep", "Renegade", 1300, 1.5, 2015, 10.5, 220, 4, 120)

    sedan1.info()
    jeep1.info()

    print(str(sedan1))
    print(repr(jeep1))

    sedan2 = Sedan("Honda", "Accord", 500, 2.0, 2017, 7.5)
    print(sedan1 == sedan2)

    distance = 200  # км
    fuel_needed = sedan1.calculate_fuel_consumption(distance)
    print(f"{sedan1.model} витратить {fuel_needed:} л пального на {distance} км.")

    sedan1.shift_gear('D')
    jeep1.shift_gear('R')
