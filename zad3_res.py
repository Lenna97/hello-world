# domasna zadaca 1
# domasna zadaca 2
# domasna zadaca 2+ : Da se isprintaat site atributi za zadaden objekt od employee_list.


# zadaca 1
# Da se napravat 2 instanci od klasata Company i 3 instanci od klasata Employee.

from typing import Self


class Company:
    def __init__(self, name):
        self.name = name

class Employee:    
    def __init__(self, name, position, salary, company):
        self.name = name
        self.position = position
        self.salary = salary
        self.company = company
        self.annual_leave = 25
        self.special_circumstances_leave = 5 
        self.maternity_leave = 100 
        self.sick_days_leave = 5
    #Zadaca 3
    def days_off(self, leave_type):
        if leave_type == "annual":
            return self.annual_leave
        elif leave_type == "special_circumstances":
            return self.special_circumstances_leave
        elif leave_type == "maternity":
            return self.maternity_leave
        elif leave_type == "sick_days":
            return self.sick_days_leave
        else:
            return "Invalid leave type"
    #zadaca 4
    def promotion(self, salary_increase_percent):
        self.salary += self.salary * (salary_increase_percent / 100)
        return self.salary

# Instanci od klasata Company
company1 = Company("Company1")
company2 = Company("Company2")

# Instanci od klasata Employee
employee1 = Employee("Employee1", "Manager", 80000, company1)
employee2 = Employee("Employee2", "Engineer", 60000, company1)
employee3 = Employee("Employee3", "Designer", 80000, company2)

print("Employee1 Company: ", employee1.company.name)
print("Employee2 Company: ", employee2.company.name)
print("Employee3 Company: ", employee3.company.name)

# zadaca 2
# Da se napravi sporedba za prosecnite salary costs za sekoja kompanija.
employees = [employee1, employee2, employee3]

def average_salary(company):
        total_salary = 0
        employee_count = 0

        for employee in employees:
            if employee.company == company:
                total_salary += employee.salary
                employee_count += 1

        if employee_count == 0:
            return 0

        return total_salary / employee_count
print("Average Salary for Company1: ", average_salary(company1))
print("Average Salary for Company2: ", average_salary(company2))

# zadaca 3
# Da se napise metod days_off so koj employee ke ima pravo da bara denovi odmor.
# Pritoa imame annual leave, special circumstances leave, maternity leave, sick days leave.

print(f"Annual days off za employee1: {employee1.days_off("annual")}") 
print(f"Special circumstances days off za employee1: {employee1.days_off("special_circumstances")}") 
print(f"Maternity days off za employee1: {employee1.days_off("maternity")}") 
print(f"Sick days days off za employee1: {employee1.days_off("sick_days")}") 
# zadaca 4
# Da se napise metod promotion so koj employee ke moze da bide unapreden.

print(f"Promotion za employee1, novata plata e: {employee1.promotion(10)}") 

# zadaca 5
# Da se napravi klasa Produkt.
# Da se dodadat zadolzitelni atriibuti pri kreiranje na instanca od Produkt: naziv, seriski_broj, cena, tip
# i opcionalen atribut kolicina.
class Product:
    def __init__(self, name, serial_number, price, product_type, quantity=1):
        self.name = name
        self.serial_number = serial_number
        self.price = price
        self.product_type = product_type
        self.quantity = quantity

    def get_product_details(self):
        return f"Ime na produkt: {self.name}, Seriski broj: {self.serial_number}, Cena: {self.price}, Tip: {self.product_type}, Kolicina: {self.quantity}"

product1 = Product("Macbook Pro", "SN123456", 1200, "Laptop")
product2 = Product("Dell", "SN234567", 900, "Desktop", 3)

print(product1.get_product_details()) 
print(product2.get_product_details())

# zadaca 6
# Da se napravi klasa Prodavnica.
# Instancata od prodavnicata, mora da ima: ime, seriski_broj.
# Da se kreira metod dodaj_produkt, koj kje dodava produkti vo prodavnicata,
# so toa sto mora da se proveri dali e od tip Produkt.
class Shop:
    def __init__(self, name, serial_number):
        self.name = name
        self.serial_number = serial_number
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            print("Nevaliden tip na produkt.")

    def __str__(self):
        return f"Ime na prodavnica: {self.name}, Seriski broj: {self.serial_number}"


    def get_store_details(self):
        return self.__str__()

    def get_product_list(self):
        return [product.get_product_details() for product in self.products]




shop1 = Shop("Best Buy", "SS123456")
shop1.add_product(product1)
shop1.add_product(product2)

print(shop1.get_store_details()) 
print(shop1.get_product_list())   


# zadaca 7
# Da se kreira klasa Kupuvac.
# Sekoj Kupuvac mora da ima: ime, prezime, dostapni_paricni_sredstva.
class Customer:
    def __init__(self, name, surname, available_cash):
        self.name = name
        self.surname = surname
        self.available_cash = available_cash

    def __str__(self):
        return f"Ime na kupuvac: {self.name}, Prezime: {self.surname}, Dostapni paricni sredstva: {self.available_cash}"

    def get_customer_details(self):
        return self.__str__()
    def buy_product(self, product):
        if product.price <= self.available_cash:
            self.available_cash -= product.price
            product.quantity -= 1
            return True
        else:
            return False

customer1 = Customer("John", "Doe", 1200)
print(customer1.get_customer_details()) 
print(f"{customer1.name} {customer1.surname} kupuva {product1.name} so cena {product1.price}: {customer1.buy_product(product1)}") 
print(customer1.get_customer_details()) 


# zadaca 8
# Da se kreiraat __str__ metodi za klasite.
# Da se kreira metod pecati_produkti na klasata Prodavnica koj sto kje gi printa site dostapni produkti.


# zadaca 9
#  Da se kreiraat 5 produkti.
# Da se kreiraat 2 prodavnici.
# Da se dodadat produkti vo prodavnicite.
# Da se kreiraat kupuvaci.
# Da se napravi scenario, kupuvacot da kupi produkt od prodavnica. Vo slucaj ako go nema produktot,
# da proba da go kupi produktot od drugata prodavnica.
# Pri kupuvanje na produkt od prodavnica, treba da se izbrise istoit od listata na produkti. Za ova da se koristi
# privaten metod __brisi_produkt.
# Da se vnimava na dostapnite sredstva na kupuvacot.
