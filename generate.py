import csv
from faker import Faker
import random
class Writer:
    file_num = 1
    num_rows = 10000
    status_types = ['I', 'P', 'S', 'N']
    columns = ['IAV', 'First Name', 'Last Name', 'Middle Name', 'Status', 'DOB', 'Phone', 'Email', 'Company ID', 'State', 'Case Created Date', 'Last Update Date']

    def __init__(self, faker):
        self.faker = faker
        for _ in range(36):
            self.status_types.append('A')

    #Note that names may not make gender sense
    def generateCSVFile(self):
        fake = self.faker
        with open('output_' + str(self.file_num) + '.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            if self.file_num == 4:
                 writer.writerow(["A-Number"] + ["First Name"] + ["Last Name"] + ["Middle Name"] + ["DOB"] + ["Status"] + ["Phone"] + ["Email"] + ["State"] + ["Created Date"] + ["Updated Last"])
            else:
                writer.writerow(["A-Number"] + ["First Name"] + ["Last Name"] + ["Middle Name"] + ["DOB"] + ["Status"] + ["Phone"] + ["Email"] + ["Company"] + ["State"] + ["Created Date"] + ["Updated Last"])
            for i in range(self.num_rows):
                a_num = 'A' + str(random.randrange(10000000, 999999999))
                first_name = fake.first_name()
                last_name = fake.last_name()
                middle_name = fake.first_name() if self.file_num < 3 else '' if random.randint(0, 100) % 3 == 0 else fake.first_name()
                dob = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=115)
                status = self.status_types[random.randint(0,39)]
                phone = random.randrange(1000000000, 9999999999) if self.file_num < 3 else fake.phone_number()
                email = fake.email()
                company = fake.company()
                state = fake.state_abbr()
                create_date = fake.date_of_birth(tzinfo=None, minimum_age=0, maximum_age=5)
                update_date = fake.date_between(create_date, "today")
                if self.file_num < 4:
                    writer.writerow([a_num] + [first_name] + [last_name] + [middle_name] + [dob] + [status] + [phone] + [email] + [company] + [state] + [create_date] + [update_date])
                else:
                    #Removed Company Field
                    if random.randint(1, 100) == 1:
                        writer.writerow([None] + [None] + [None] + [None] + [None] + [None] + [None] + [None] + [None] + [None] + [None])
                    else:
                        writer.writerow([a_num] + [first_name] + [last_name] + [middle_name] + [dob] + [status] + [phone] + [email] + [state] + [create_date] + [update_date])
        self.file_num += 1

fake = Faker()
writer = Writer(fake)
writer.generateCSVFile()
writer.generateCSVFile()
writer.generateCSVFile()
writer.generateCSVFile()
