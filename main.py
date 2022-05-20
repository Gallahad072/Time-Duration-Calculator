from ast import While


def main(start=False, end=False):
    print("\nPlease enter a time in 24 hour clock format, e.g 0010, 2305, 1517\n")

    while True:
        start = start if start else input("Start Time: ")
        if start.isdigit():
            start = start.zfill(4)
            start_hrs, start_mins = int(start[:2]), int(start[2:])
            if start_hrs < 24 and start_mins < 60:
                break
            else:
                print("\nEnter a valid time\n")
        else:
            print("\nEnter only digits\n")

    while True:
        end = end if end else input("End Time: ")
        if end.isdigit():
            end = end.zfill(4)
            end_hrs, end_mins = int(end[:2]), int(end[2:])
            if end_hrs < 24 and end_mins < 60:
                if int(end) > int(start):
                    break
                else:
                    print("\nEnter a time later than start\n")
            else:
                print("\nEnter a valid time\n")
        else:
            print("\nEnter only digits\n")

    start_hrs_total = start_hrs + start_mins / 60
    end_hrs_total = end_hrs + end_mins / 60
    hrs = round(end_hrs_total - start_hrs_total, 2)

    start_mins_total = start_hrs * 60 + start_mins
    end_mins_total = end_hrs * 60 + end_mins
    mins = end_mins_total - start_mins_total

    hrs_mins = f"{str(mins//60)}:{str(mins%60).zfill(2)}"
    message = (
        f"\nDuration:\n{hrs_mins} hours and minutes\n{hrs} hours\n{mins} minutes\n"
    )

    return hrs_mins, hrs, mins, message


if __name__ == "__main__":
    while True:
        vals = main()
        print(vals[-1])
