class person:
    count = 0
    
    def __init__(self, name, birth, phone_number) -> None:
        person.count += 1
        self.name = name
        self.birth = birth
        self.phone_number = phone_number
        
    def dislpay(self):
        print(f"Name: {self.name}")
        print(f"Birth: {self.birth}")
        print(f"Phone number: {self.phone_number}")
        print(self.count)
        

# name = input("Nhập tên: ")
# birth = input("Nhập ngày sinh: ")
# phone_number = input("Nhập số điện thoại: ")

P1 = person("Long", "22/11", "012123")
P1.dislpay()
P2 = person("Quynh", "22/11", "012123")
P2.dislpay()
P3 = person("Phung", "22/11", "012123")
P3.dislpay()
