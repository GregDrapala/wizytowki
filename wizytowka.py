from faker import Faker
fake = Faker()

class BaseContact():
      def __init__(self, firstname, lastname, phone_number, email):
            self.firstname = firstname
            self.lastname = lastname
            self.phone_number = phone_number
            self.email = email
      
      def contact(self):
            print('wybieram numer {} i dzwonie do {} {}'.format(self.phone_number, self.firstname, self. lastname))


class BusinessContact(BaseContact):
      def __init__(self, firstname, lastname, phone_number, email, company, post, work_phone_number):
            BaseContact.__init__(self, firstname, lastname, phone_number, email)
            self.company = company
            self.post = post
            self.work_phone_number = work_phone_number
            
    
      def contact(self):
            print('wybieram numer {} i dzwonie do {} {}'.format(self.work_phone_number, self.firstname, self. lastname))            


adam_nowak = BaseContact(
      firstname='Adam',
      lastname='Nowak',
      email='an@op.pl',
      phone_number='602602602')


jan_nowak = BusinessContact(
      firstname='Jan',
      lastname='Nowak',
      phone_number='600342023',
      email='JanN@op.pl',
      company='Aldi',
      post='manager',
      work_phone_number='700342253')

adam_nowak.contact()

jan_nowak.contact()


def label_length(self):
      return len(self.firstname + self.lastname)



def create_contacts(business_contact: bool, number_of_contacts: int):
      names = []
      fake = Faker()
      for i in range(number_of_contacts):
            if(business_contact):
                  names.append(BusinessContact(firstname=fake.first_name(), lastname=fake.last_name(), company=fake.company(), post=fake.job(), email=fake.email(),work_phone_number=fake.phone_number(), phone_number=fake.phone_number())) 
            else:      
                  names.append(BaseContact(firstname=fake.first_name(), lastname=fake.last_name(), email=fake.email(), phone_number=fake.phone_number()))
      return names

namelist=create_contacts(business_contact=True, number_of_contacts=4)

for name in namelist:
      print('{} {} {} {}'.format(name.firstname, name.lastname, name.company, name.email))
      print(label_length(name))