class Employee:
    """
    Klasa za vraboteni.
    """
    def __init__(self, first_name:str, last_name:str, email:str, position:str, company:str, salary=None):
        """
        Inicijalizirame objekt od klasata Employee.

        :param first_name: str, ime
        :param last_name: str, prezime
        :param email: str, email
        :param position: str, pozicija vo kompanijata
        :param company: str, kompanija
        :param salary: int, plata
        :param leave_date: str, datum 

        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.position = position
        self.company = company
        self.salary = salary
        self.leave_date = None

    def leave_company(self, leave_date:str):
        
        self.leave_date = leave_date



class Company:
    """
    Klasa za kompanija.
    """
    def __init__(self, name:str, company_id:int, address=None):
        """
        Inicijalizirame objekt od klasata Company.

        :param name: str, ime na kompanijata
        :parm company_id: int, unikaten broj na kompanija 
        :param address: str, adresa
        """
        self.name = name
        self.company_id = company_id
        self.address = address
    
    def hire(self, employee:Employee, position:str, salary:int):
        print(f'{self.name} go vrabotuva {employee.first_name}')
        employee.position = position
        employee.salary = salary

    def offer(self, employee:Employee,position:str, offer_respond:bool):
        self.offer_respond = offer_respond
        employee.position = position

        print(f'{self.name} prkja ponuda za rabota do {employee.first_name} za rabotnata pozicija {position}')




semos_mk = Company("Semos Makedonija", 1234)
semos_srb = Company("Semos Srbija", 5678)

ime1 = Employee("Ime1", "Prezime1", "ime1@ime1.com", "developer", "semos_mk")
ime2 = Employee("Ime2", "Prezime2", "ime2@ime2.com", "devops", "semos_srb")

semos_mk.offer(ime1, 'developer', True)

semos_srb.offer(ime2, 'support' , False)


if semos_mk.offer_respond:
    semos_mk.hire(ime1, ime1.position, 10000000)
    print(ime1.position, ime1.salary)
else:
    print(f"{ime1.first_name} ne go prifakja ponudata!")
#ime1.leave_company('06.12.2023')

if ime1.leave_date:
    print(f'{ime1.first_name} {ime1.last_name} go napusti firmata na {ime1.leave_date}.')
else:
    print(f'{ime1.first_name} {ime1.last_name} seuste e vraboten vo {semos_mk.name}.')


if semos_srb.offer_respond:
    semos_srb.hire(ime2, ime2.position, 10000000)
    print(ime2.position, ime2.salary)
else:
    print(f"{ime2.first_name} ne go prifakja ponudata!")
ime2.leave_company('06.12.2023')

if semos_srb.offer_respond:
    if ime2.leave_date:
        print(f'{ime2.first_name} {ime2.last_name} go napusti firmata na {ime2.leave_date}.')
    else:
        print(f'{ime2.first_name} {ime2.last_name} seuste e vraboten vo {semos_srb.name}.')
