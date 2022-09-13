# # NOT PYTHONIC


# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_Price(self):
#         return self.__price

#     def set_price(self, prize):
#         if prize < 0:
#             raise ValueError("Price cannot be negetive")
#         self.price = prize


# cloud = Product(-50)


# PYTHONIC

# class Product:

#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.price

#     def set_price(self, prize):
#         if prize < 0:
#             raise ValueError("Price cannot be negetive")
#         self.price = prize

#     Price = property(get_price, set_price)


# cloud = Product(10)
# print(cloud.Price)
# cloud.Price = 50
# print(cloud.Price)


class Product:

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, prize):
        if prize < 0:
            raise ValueError("Price cannot be negetive")
        self.__price = prize

    # Price = property(get_price, set_price)


cloud = Product(10)
print(cloud.price)
cloud.price = 50
print(cloud.price)
