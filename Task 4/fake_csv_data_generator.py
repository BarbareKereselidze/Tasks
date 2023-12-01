import csv
import random
from random import randint
from faker import Faker
from datetime import datetime
import os


class GenerateFakeCsv:
    def __init__(self):
        self.fake = Faker()
        self.fake_data = []
        self.row_amount = randint(100, 1000)

    def generate_fake_user(self):
        header = ["name", "birthdate", "email", "address", "phone_number"]
        self.fake_data.append(header)

        for _ in range(self.row_amount):
            name = self.fake.name()
            birthdate = self.fake.date_of_birth(minimum_age=18, maximum_age=80)
            email = self.fake.email()
            address = self.fake.address()
            new_address = address.replace("\n", " ")
            phone_number = self.fake.phone_number()

            self.fake_data.append([name, birthdate, email, new_address, phone_number])

        return self.fake_data

    def generate_fake_job(self):
        header = ["name", "job", "company", "salary", "credit_card_number", "credit_card_expire"]
        self.fake_data.append(header)

        for _ in range(self.row_amount):
            name = self.fake.name()
            job = self.fake.job()
            company = self.fake.company()
            salary = randint(1000, 10000)
            credit_card_number = self.fake.credit_card_number()
            credit_card_expire = self.fake.credit_card_expire()

            self.fake_data.append([name, job, company, salary, credit_card_number, credit_card_expire])

        return self.fake_data

    def generate_csv(self, csv_directory_path):
        timestamp = datetime.now().timestamp()
        filename = f"{csv_directory_path}/fake_data_{timestamp}.csv"

        functions_list = [self.generate_fake_user(), self.generate_fake_job()]
        fake_csv = random.choice(functions_list)

        while True:
            try:
                with open(filename, 'w', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerows(fake_csv)

                print(f"Fake data has been generated and saved to '{filename}'.")

                break

            except FileNotFoundError:
                os.makedirs(csv_directory_path, exist_ok=True)


generator = GenerateFakeCsv()
generator.generate_csv("csv_files")



