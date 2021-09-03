# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    industry = 119
    science_required = 1152 - 34
    science_start = 51
    science_end   = 75

    for manutech in range(0, 10):
        print('Manu Tech: ' + str(manutech) + ' ships per hour = ' + str( industry * (manutech + 5) / 24) )

    round_time = 999 # just to start to compare to
    for science in range(science_start,science_end):
        time = science_required/science

        if math.ceil(time) < round_time:
            print('Science: ' + str(science) +  ' Hours taken = ' + str(time) )

        round_time = math.ceil(time) # sets new round time to compare to next run



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
