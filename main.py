# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def combat(my_wep,enemy_wep,my_ships,enemy_ships):
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    industry = 241
    manu_start = 5
    manu_end   = 15
    science_required = 1440-14-83-83
    science_required = 1152 - 32
    science_start = 60
    science_end   = 125

    ships_per_hour = round(industry * (manu_start - 1 + 5) / 24, 2) ## starting manutech - 1 calc
    for manutech in range(manu_start, manu_end):
        increase = round(industry * (manutech + 5) / 24,2)/ships_per_hour * 100
        increase = round(increase,1)
        print('Manu Tech: ' + str(manutech) + ' ships per hour = ' + str( ships_per_hour) + '      increase % = ' + str(increase))
        ships_per_hour = round(industry * (manutech + 5) / 24,2)

    round_time = 999 # just to start to compare to
    for science in range(science_start,science_end):
        time = science_required/science

        if math.ceil(time) < round_time:
            print('Science: ' + str(science) +  ' Hours taken = ' + str(time) )

        round_time = math.ceil(time) # sets new round time to compare to next run



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
