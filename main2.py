import pandas
from abc import ABC, abstractmethod
# ABC is Abstract Base Class

df = pandas.read_csv("hotels.csv", dtype={"id": str})


# Synatactic Sugar = Simplified Syntax
notTrue = "Hello" == "Hi"
# a.k.a "hello".__eq__("Hi")
# 1 + 2
# 1 .__add__(2)
print(notTrue)

#Attributes can be
   # variables (instance vs class)
   # methods (instance vs class)

# Property is a method that behaves like a variable


class Hotel:
    # class variables created within the class level
    # shared across each instance
    watermark = "The Real Estate Company"

    # Instance method
    def __init__(self, hotel_id):
        # instance variables coded inside the method
        # only available within the instance
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    # Instance method
    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)

    # Instance method
    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

     # Class method
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass

class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
                Thank you for your Reservation!
                Booking details are below
                Name: {self.the_customer_name}
                Hotel name: {self.hotel.name}
        """
        return content

    def generate_spa(self):
        content = f"""
                Thank you for your SPA Reservation!
                Here are your SPA Booking data:
                Name: {self.customer_name}
                Hotel name: {self.hotel.name}
        """
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2


# Example of inheritance whith overriding method
class DigitalTicket(Ticket):
    def generate(self):
        print("Child Class")


print(Hotel.get_hotel_count(data=df))

hotel1 = Hotel(hotel_id=188)
print(Hotel.get_hotel_count(data=df))

# example of property
ticket = ReservationTicket(customer_name="john smith ", hotel_object=hotel1)
print(ticket.the_customer_name)
print(ticket.generate())

# Example of static method inside a class
print(ReservationTicket.convert(10))

ticket = DigitalTicket(customer_name="JOHN SMITH", hotel_object=hotel1)
ticket.generate()

