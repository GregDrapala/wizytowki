from faker import Faker
fake = Faker()
class Business_Card():
    def __init__(self, firstname, lastname, company, post, email,):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.post = post
        self.email = email
       
        #Variables
        self.namelength = 0

class base_contact(Business_Card):
   def __init__(self, private_phone_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.private_phone_number = private_phone_number
def contact_private(self):
    print('wybieram numer {}, i dzwonie do {} {}'.format(self.private_phone_number, self.firstname, self. lastname))
        
class business_contact(Business_Card):
   def __init__(self, work_phone_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.work_phone_number = work_phone_number
def contact_work(self):
    print('wybieram numer {}, i dzwonie do {} {}'.format(self.work_phone_number, self.firstname, self. lastname))


def __str__(self):
       return f'{self.firstname} {self.lastname} {self.email}'
    
jan_nowak = Business_Card(firstname='Jan', lastname='Nowak', company='Aldi', post='manager', email='JanN@op.pl', private_phone_number='600342023', work_phone_number='700342253')

@property
def namelength(self):
        return self.namelength
@namelength.setter
def namelength(self):
        self.namelength = len(self.firstname + ' ' + self.lastname)


def create_contacts():
    names = []
    fake = Faker()
    for i in range(5):
        names.append(Business_Card(firstname=fake.first_name(), lastname=fake.last_name(), company=fake.company(), post=fake.job(), email=fake.email()))
    return names


namelist = create_contacts()

for name in namelist:
    print('{} {} {} {}'.format(name.firstname, name.lastname, name.company, name.email))
    print(name.namelength)


