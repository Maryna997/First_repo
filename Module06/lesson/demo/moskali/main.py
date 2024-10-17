from moskali.constants import MENU
from moskali.exceptions import NotInRange
from pathlib import Path
from faker import Faker 


FILENAME = Path(__file__).parent / "losses.txt"

def add_new_record(name, amount):
    with open(FILENAME, "a") as f:
        fake = Faker()
        current_date = fake.date_between("-1y").strftime("%m%d%Y")
        record = f"{current_date: >15}{name: ^40}{amount: ^10}\n"
        f.write(record)

def show_statistics():
    with open(FILENAME, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line, end="")

def main():
    print(MENU)
    while True: 
        try:
            choice = int(input("Make your choice please >>>"))
            if choice < 1 or choice > 4:
                raise NotInRange("Please select from 1-4")
        except ValueError:
            print("Please write choice as a number")
            continue
        except NotInRange as e:
            print(e)
            continue
        except:
            print("Whoops, try again")
            continue


        match choice:
            case 1:
                print("PLease enter dta in the following format <name>:<amount>")
                record = input(">>>")
                name, amount = record.strip().split(":")
                add_new_record(name, amount)
            case 2:
                print("Please see data below")
                show_statistics()
            case 3: 
                print(MENU)
            case 4:
                print("You did great job today!")
                break




if __name__ == "__main__":
    main()