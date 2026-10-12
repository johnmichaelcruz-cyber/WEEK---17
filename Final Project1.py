def get_initial_readings():
    """Return the initial temperature readings."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Check whether the text contains a valid whole number."""
    if len(text) == 0:
        return False

    start = 0

    if text[0] == "-":
        start = 1

    if start == len(text):
        return False

    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False

    return True


def display_menu():
    """Display the main menu."""
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(readings):
    """Display all stored temperature readings."""
    print("\nCURRENT READINGS")
    print("----------------")

    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def add_reading(readings, lowest, highest):
    """Validate and add a new temperature reading."""
    text = input("Enter new reading: ")

    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    else:
        reading = int(text)

        if reading < lowest or reading > highest:
            print(
                f"Invalid reading. Enter a value from "
                f"{lowest} to {highest}."
            )
        else:
            readings.append(reading)
            print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return the classification of one temperature reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def display_classifications(readings):
    """Display the classification of every reading."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        category = classify_reading(reading, 30, 35)
        print(f"{reading} °C -> {category}")


def compute_total(readings):
    """Calculate the total of all readings using a loop."""
    total = 0

    for reading in readings:
        total = total + reading

    return total


def compute_average(readings):
    """Calculate the average temperature."""
    total = compute_total(readings)
    return total / len(readings)


def find_minimum(readings):
    """Find the smallest temperature reading."""
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading

    return minimum


def find_maximum(readings):
    """Find the largest temperature reading."""
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading

    return maximum


def count_category(readings, category):
    """Count readings belonging to a specific category."""
    count = 0

    for reading in readings:
        result = classify_reading(reading, 30, 35)

        if result == category:
            count = count + 1

    return count


def determine_overall_status(warning_count, critical_count):
    """Return the overall monitoring status."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(readings):
    """Display numerical statistics and the overall status."""
    number = len(readings)
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, "NORMAL")
    warning_count = count_category(readings, "WARNING")
    critical_count = count_category(readings, "CRITICAL")

    normal_percentage = normal_count / number * 100
    warning_percentage = warning_count / number * 100
    critical_percentage = critical_count / number * 100

    status = determine_overall_status(
        warning_count, critical_count
    )

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings : {number}")
    print(f"Total of readings : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")

    print(
        f"\nNORMAL : {normal_count} "
        f"({normal_percentage:.2f}%)"
    )
    print(
        f"WARNING : {warning_count} "
        f"({warning_percentage:.2f}%)"
    )
    print(
        f"CRITICAL : {critical_count} "
        f"({critical_percentage:.2f}%)"
    )

    print(f"\nOverall Status: {status}")


def main():
    """Control the main program and repeat the menu."""
    readings = get_initial_readings()

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            display_readings(readings)

        elif choice == "2":
            add_reading(readings, 0, 100)

        elif choice == "3":
            display_classifications(readings)

        elif choice == "4":
            display_summary(readings)

        elif choice == "5":
            print(
                "Thank you for using the Device Monitoring System."
            )
            break

        else:
            print(
                "Invalid choice. Please enter a number from 1 to 5."
            )


main()