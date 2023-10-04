# import csv

# class WarehouseParcelDetail:
#     def __init__(self, parcel_number, parcel_weight, parcel_category):
#         self.parcel_number = parcel_number
#         self.parcel_weight = parcel_weight
#         self.parcel_category = parcel_category

#     def save_and_display_parcel_details(self, filename):
#         # Create a list to hold parcel details of the same category
#         same_category_details = []

#         # Read existing data from the CSV file, if any
#         try:
#             with open(filename, 'r', newline='') as file:
#                 csv_reader = csv.reader(file)
#                 next(csv_reader)  # Skip the header row
#                 for row in csv_reader:
#                     if row[2] == self.parcel_category:
#                         same_category_details.append(row[0])
#         except FileNotFoundError:
#             pass  # Ignore if the file doesn't exist yet

#         # Append the new parcel number to the same category details
#         same_category_details.append(str(self.parcel_number))

#         # Write the updated data to the CSV file
#         with open(filename, 'w', newline='') as file:
#             csv_writer = csv.writer(file)
#             csv_writer.writerow(['Parcel Number', 'Parcel Weight', 'Parcel Category'])  # Header
#             for number in same_category_details:
#                 csv_writer.writerow([number, self.parcel_weight, self.parcel_category])

#         # Display parcel numbers of the same category in a table
#         print(f"Parcel Category: {self.parcel_category}")
#         for number in same_category_details:
#             print(number)

# if __name__ == "__main__":
#     # Example usage:

#     # Create parcel detail objects
#     parcel1 = WarehouseParcelDetail(23456, 66234, 'Filters')
#     parcel2 = WarehouseParcelDetail(96355, 86643, 'Automobil_parts')
#     parcel3 = WarehouseParcelDetail(83722, 64326, 'Cargo_containeer')
#     parcel4 = WarehouseParcelDetail(66234, 98432, 'Filters')

#     # Save and display parcel details
#     parcel1.save_and_display_parcel_details('parcel_details.csv')
#     parcel2.save_and_display_parcel_details('parcel_details.csv')
#     parcel3.save_and_display_parcel_details('parcel_details.csv')
#     parcel4.save_and_display_parcel_details('parcel_details.csv')



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