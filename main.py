# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def combat(my_wep,enemy_wep,my_ships,enemy_ships):
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    industry = 262
    manu_start = 5
    manu_end   = 15

    science_required = 1152 - 120 +1008-434 + 864-102
    science_required = 1584 - 61
    science_start = 60
    science_end   = 125

    attack_wep = 12
    def_wep = 11

    ships_per_hour = round(industry * (manu_start - 1 + 5) / 24, 2) ## starting manutech - 1 calc
    for manutech in range(manu_start, manu_end):
        increase = round(industry * (manutech + 5) / 24,2)/ships_per_hour * 100
        increase = round(increase,1)
        ships_per_hour = round(industry * (manutech + 5) / 24,2)
        print('Manu Tech: ' + str(manutech) + ' ships per hour = ' + str( ships_per_hour) + '      increase % = ' + str(increase))

    round_time = 999 # just to start to compare to
    for science in range(science_start,science_end):
        time = science_required/science

        if math.ceil(time) < round_time:
            print('Science: ' + str(science) +  ' Hours taken = ' + str(time) )

        round_time = math.ceil(time) # sets new round time to compare to next run

    print('def wep = ' + str(def_wep) + ' ' + 'attack wep = ' + str(attack_wep) + ' ' + str(round((def_wep + 1) / attack_wep * 100, 2)))

    # for i in range(10,14):
    #     for j in range(10,14):
    #         print('def wep = '+ str(i) + ' ' + 'attack wep = '+ str(j) + ' def % advantage' + str(round((i+1)/j*100,2)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# could use this as basis for combat
#https://github.com/tseddon84/neptune_pride/blob/master/battle_checker/battle_check.py