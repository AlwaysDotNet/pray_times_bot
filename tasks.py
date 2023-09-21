from datetime import datetime

class Travel:
    def __init__(self, to:str, deport_date:str, back_date:str, money:float, name:str, surname:str, pass_ser:str, pass_num: int, visa, ticket:float, birth_date:str):
        self.to = to
        self.deport = deport_date
        self.back_date = back_date 
        self.money = money 
        self.name = name 
        self.surname = surname 
        self.seriya = pass_ser 
        self.num = pass_num 
        self.visa = visa 
        self.ticket = ticket 
        self.birth_date = birth_date 

    def days(self):
        depor = self.deport.split('-')
        year1 = int(depor[2]) * 365
        month1 = int(depor[1]) * 30
        day1 = int(depor[0])
        back = self.back_date.split('-')
        year2 = int(back[2]) * 365
        month2 = int(back[1]) * 30
        day2 = int(back[0])
        result = (year2 + month2 + day2) - (year1 + month1 + day1)
        return f"{self.name} {self.to}da {result} kun qolishadi."

    def age_check(self):
        cur = datetime.now().year
        year = self.birth_date.split('-')
        age = cur - int(year[2])
        if age >= 16:
            return f"Sayohatga {self.name}ning yoshlari yetadi"
        else:
            return f"Afsuski, sayohatga {self.name}ning yoshlari yetmaydi"

    def money_check(self):
        if self.money > self.ticket:
            return f"{self.to}ga borgani {self.name}ni puli yetadi"
        else:
            return f"Afsuski, {self.to}ga borgani {self.name}ni puli yetmaydi"
        

if __name__ == "__main__":
    to = input("Travelling to: ")
    deport = input("Deport date(format: dd-mm-yyyy): ")
    back = input("Coming back in(format: dd-mm-yyyy): ")
    money = float(input("Your budget: "))
    name = input("Name: ")
    surname = input("Surname: ")
    pass_seriya = input("Passport seriya: ")
    pass_raqam = int(input("Passport digits: "))
    visa = input("Input Visa: 1-yes/0-no: ")
    ticket = float(input("How much does the ticket cost: "))
    b_date = input("Your birth date(format: dd-mm-yyyy): ")
    result = Travel(to, deport, back, money,name, surname, pass_seriya, pass_raqam, visa, ticket, b_date)
    print(result.days())
    print(result.money_check())
    print(result.age_check())

    
