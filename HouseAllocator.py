import config as cfg

def initialize_boarding_house():
    for cls in cfg.classes:
        for food_pref in cfg.food_preferences:
            boarding_house = cls.upper() + food_pref.upper()
            cfg.boarding_house_allocation[boarding_house] = list()
    cfg.boarding_house_allocation[cfg.NOT_ALLOCATED] = list()

def get_each_hostel_capacity():
    try:
        total_capacity = int(input("Please Insert Total Boarding Capacity: "))
        if total_capacity>=0 and total_capacity%4 == 0:
            return int(total_capacity/4)
        else:
            print("Please provide initial capacity in multiplication of 4 and a positive number")
            return get_each_hostel_capacity()
    except Exception as e:
        print("Please provide capacity in integer")
        return get_each_hostel_capacity()


def validate_and_queue_registration_data(registration_data):
    student_data = registration_data.split()
    if len(student_data) != 4:
        print("Number of arguments for registration is not correct, "
              "Please give input in mentioned format - reg roll_number class food_preference")
        return
    if student_data[0].lower() != 'reg':
        print("Registration command is wrong please use (reg or Reg) for registration")
        return
    try:
        if int(student_data[1]) > 9999 or int(student_data[1]) < 1:
            print("Roll number should be in range of 1 to 9999 and integer value only")
            return
    except Exception as e:
        print("Roll number is not Integer type, Roll number should be in range of 1 to 9999")
        return
    if student_data[2].lower() not in cfg.classes:
        print("Class Name should be A or B (case insensitive)")
        return

    if student_data[3].lower() not in cfg.food_preferences:
        print("Food preferences should be V or NV (case insensitive)")
        return

    if student_data[1] not in cfg.roll_number_list:
        cfg.registration_queue.append(student_data)
        cfg.roll_number_list.append(student_data[1])
    else:
        print("Student is already registered")


def get_input():
    print("Follow given format for student registration (reg roll_number class food_preference)")
    # use space as a separator between attributes
    registration_data = input("Please Insert New Student Record: ")
    while registration_data not in  ['fin', 'exit']:
        validate_and_queue_registration_data(registration_data)
        registration_data = input("Please Insert New Student Record: ")


def check_availability(boarding_house_capacity, boarding_house):
    if boarding_house_capacity == 0:
        return False
    if len(cfg.boarding_house_allocation.get(boarding_house)) < boarding_house_capacity:
        return True
    else:
        return False


def get_boarding_house_name(student_record):
    return student_record[2].upper() + student_record[3].upper()


def assign_boarding_house(boarding_house_capacity):
    for student_record in cfg.registration_queue:
        boarding_house = get_boarding_house_name(student_record)
        if check_availability(boarding_house_capacity, boarding_house):
            allocation_list = cfg.boarding_house_allocation.get(boarding_house)
            allocation_list.append(int(student_record[1]))
            cfg.boarding_house_allocation[boarding_house] = allocation_list

        else:
            allocation_list = cfg.boarding_house_allocation.get(cfg.NOT_ALLOCATED)
            allocation_list.append(int(student_record[1]))
            cfg.boarding_house_allocation[cfg.NOT_ALLOCATED] = allocation_list

# for printing boarding allocation details
def show_boarding_allocation():
    print("\nBoarding House Allocations : -")
    for boarding_house, students_list in cfg.boarding_house_allocation.items():
        print(boarding_house,":",students_list)

# entry point for boarding house allocation
def main():
    boarding_house_capacity = get_each_hostel_capacity()
    get_input()
    initialize_boarding_house()
    assign_boarding_house(boarding_house_capacity)
    show_boarding_allocation()


if __name__ == "__main__":
    main()
