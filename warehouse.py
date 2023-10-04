import os
import csv
class WarehouseParcelDetail:
    VALID_CATEGORIES = ["filters", "automobil_parts", "cargo_containeer"]

    def __init__(self, parcel_number, parcel_weight, parcel_category):
        if not self._validate_parcel_number(parcel_number):
            raise ValueError("Parcel number must be a 5-digit number.")
        if parcel_category.lower() not in self.VALID_CATEGORIES:
            raise ValueError("Parcel category must be one of: filters, automobil_parts, cargo_containeer")

        self.parcel_number = parcel_number
        self.parcel_weight = parcel_weight
        self.parcel_category = parcel_category.lower()

    def _validate_parcel_number(self, parcel_number):
        return len(str(parcel_number)) == 5 and str(parcel_number).isdigit()

    def save_parcel_details(self):
        if not os.path.exists('parcel_details.csv'):
            with open('parcel_details.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Parcel Number", "Parcel Weight", "Parcel Category"])

        with open('parcel_details.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.parcel_number, self.parcel_weight, self.parcel_category])

    @staticmethod
    def display_parcel_details_by_category(category):
        if not os.path.exists('parcel_details.csv'):
            print("CSV file 'parcel_details.csv' does not exist.")
            return []

        parcel_numbers = []
        with open('parcel_details.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  
            for row in reader:
                if row[2] == category:
                    parcel_numbers.append(row[0])

        return parcel_numbers
categories = {"1":"filters","2":"automobil_parts","3":"cargo_containeer"}
n = int(input("Input No. of Records : "))
for i in range(n):
    parcel_number = int(input("Enter Parcel Number : "))
    parcel_weight = int(input("Enter Parcel Weight : "))
    print("___________Categories_________")
    print("'1':'filters'\n'2':'automobil_parts'\n'3':'cargo_containeer'")
    cargo_container = input("Enter Parcel Category Number : ")

    parcel = WarehouseParcelDetail(parcel_number,parcel_weight,categories[cargo_container])

    parcel.save_parcel_details()