class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def get_cost(self):
        return self.size * 5 + len(self.toppings) * 2

    def get_description(self):
        return f"{self.size} дюймовая пицца с {', '.join(self.toppings)}"


class CheesePizza(Pizza):
    def __init__(self, size):
        super().__init__(size, ["сыр"])


class PepperoniPizza(Pizza):
    def __init__(self, size):
        super().__init__(size, ["пепперони", "сыр"])


class VeggiePizza(Pizza):
    def __init__(self, size):
        super().__init__(size, ["помидоры", "грибы", "перец", "сыр"])


class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type, size):
        if pizza_type == "cheese":
            return CheesePizza(size)
        elif pizza_type == "pepperoni":
            return PepperoniPizza(size)
        elif pizza_type == "veggie":
            return VeggiePizza(size)
        else:
            raise ValueError(f"Неподдерживаемый тип пиццы: {pizza_type}")


class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total_cost(self):
        return sum(pizza.get_cost() for pizza in self.pizzas)

    def get_description(self):
        return "\n".join(pizza.get_description() for pizza in self.pizzas)


class DiscountSystem:
    @staticmethod
    def calculate_discount(order):
        num_pizzas = len(order.pizzas)
        if num_pizzas >= 5:
            return 0.2  # 20% скидка для заказов с 5 и более пиццами
        elif num_pizzas >= 3:
            return 0.1  # 10% скидка для заказов с 3 или более пиццами
        else:
            return 0


def main():
    order = Order()

    while True:
        print("Выберите тип пиццы:")
        print("1. Сырная пицца")
        print("2. Пепперони пицца")
        print("3. Вегетарианская пицца")
        print("4. Завершить заказ")

        choice = input("Введите номер типа пиццы: ")

        if choice == "1":
            size = int(input("Введите размер пиццы (в дюймах): "))
            pizza = PizzaFactory.create_pizza("cheese", size)
            order.add_pizza(pizza)
        elif choice == "2":
            size = int(input("Введите размер пиццы (в дюймах): "))
            pizza = PizzaFactory.create_pizza("pepperoni", size)
            order.add_pizza(pizza)
        elif choice == "3":
            size = int(input("Введите размер пиццы (в дюймах): "))
            pizza = PizzaFactory.create_pizza("veggie", size)
            order.add_pizza(pizza)
        elif choice == "4":
            break
        else:
            print("Неправильный выбор, попробуйте снова.")

    discount = DiscountSystem.calculate_discount(order)
    total_cost = order.get_total_cost() * (1 - discount)

    print("---")
    print("Заказ:")
    print(order.get_description())
    print(f"Стоимость заказа: {total_cost}")

    with open("чек.txt", "w") as file:
        file.write("Заказ:\n")
        file.write(order.get_description())
        file.write(f"\nСтоимость заказа: {total_cost}")


if __name__ == "__main__":
    main()
