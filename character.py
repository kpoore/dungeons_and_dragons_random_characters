#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
A program to create D&D characters withrandomly selected race, gender, 
class/multi-class, and stats.

Created on Thu Feb  2 11:07:21 2017

@author: keith
"""
import random

        
def generate_race():
    possible_races = {'Human':[[0, 66/400.], [0.47, 0.47, 0.06], [18, 100],
                               [56, 76], [110, 206]],
                    'Dwarf':[[66/400., 2*66/400.], [0.47, 0.47, 0.06],
                             [50, 350], [48, 56], [115, 260]],
                    'Elf':[[2*66/400., 3*66/400.], [0.47, 0.47, 0.06],
                           [100, 750], [53, 73], [75, 147]],
                    'Halfling':[[3*66/400., 4*66/400.], [0.44, 0.50, 0.06],
                                [20, 160], [31, 39], [35, 40]],
                    'Gnome':[[0.66, 0.66+23/600.], [0.5, 0.44, 0.06], 
                             [40, 475], [35, 43], [35, 40]],
                    'Dragonborn':[[0.66+23/600., 0.66+2*23/600.],
                                  [0.33, 0.33, 0.34], [15, 80], [66, 82],
                                  [175, 320]],
                    'Half-elf':[[0.66+2*23/600., 0.66+3*23/600.],
                                [0.47, 0.47, 0.06], [20, 200], [57, 73],
                                [110, 206]],
                    'Half-orc':[[0.66+3*23/600., 0.66+4*23/600.],
                                [0.47, 0.47, 0.06], [14, 75], [58, 78],
                                [140, 285]],
                    'Tiefling':[[0.66+4*23/600., 0.66+5*23/600.],
                                [0.33, 0.33, 0.34], [18, 100],
                               [56, 76], [110, 200]],
                    'Aasimar':[[0.66+5*23/600., 0.66+6*23/600.],
                               [0.33, 0.33, 0.34], [18, 160], [56, 76],
                               [110, 206]],
                    'Triton':[[0.89, 0.89+11/600.], 
                              [0.47, 0.47, 0.06], [15, 200], [55, 65],
                              [80, 150]],
                    'Firbolg':[[0.89+11/600., 0.89+2*11/600.],
                               [0.25, 0.25, 0.5], [30, 500], [84, 96],
                               [240, 300]],
                    'Goliath':[[0.89+2*11/600., 0.89+3*11/600.],
                               [0.33, 0.33, 0.34], [18, 100], [84, 96],
                               [280, 340]],
                    'Kenku':[[0.89+3*11/600., 0.89+4*11/600.],
                             [0.33, 0.33, 0.34], [12, 60], [55, 65],
                             [90, 120]],
                    'Lizardfolk':[[0.89+4*11/600., 0.89+5*11/600.],
                                  [0.10, 0.10, 0.80], [14, 60], [60, 74],
                                  [130, 250]],
                    'Tabaxi':[[0.89+5*11/600., 1.],
                              [0.20, 0.20, 0.60], [18, 100], [60, 74],
                              [80, 150]]}
    rand_num = random.random()
    for key in possible_races:
        if possible_races[key][0][0] <= rand_num <= possible_races[key][0][1]:
            race = possible_races[key]
            race_name = key
    return race_name, race[1], race[2], race[3], race[4]
   
    
def set_age(age_prob):
    return random.randint(age_prob[0], age_prob[1])
    
    
def set_height(height_prob):
    return random.randint(height_prob[0], height_prob[1])
    

def set_weight(weight_prob):
    return random.randint(weight_prob[0], weight_prob[1])


def set_gender(gender_prob):
    rand_num = random.random()
    if 0.0 <= rand_num <= gender_prob[0]:
        return 'male'
    elif gender_prob[0] <= rand_num <= gender_prob[0] + gender_prob[1]:
        return 'female'
    else:
        return 'neutral'


#def set_class():
#
#
#    return char_class        

if __name__ == '__main__':
    race_name, p_gender, p_age, p_height, p_weight = generate_race()
    char_race = race_name
    char_age = set_age(p_age)
    char_weight = set_age(p_weight)
    char_height = set_height(p_height)
    char_gender = set_gender(p_gender)
    
    print "Your character is a {} year old {}. Your character is {}, weighing {} and is {} inches tall".format(
            char_age, char_race, char_gender, char_weight, char_height)