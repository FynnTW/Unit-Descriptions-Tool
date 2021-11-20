from itertools import starmap
import os
import re
import traceback
from typing import Text
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Input
import time


def LEDIndicator(key=None, radius=30):
    return sg.Graph(canvas_size=(radius, radius),
             graph_bottom_left=(-radius, -radius),
             graph_top_right=(radius, radius),
             tooltip="If red, existing unit descriptions are recognized to likely exist, press remove descriptions first!",
             pad=(0, 0), key=key)

def SetLED(window, key, color):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 12, fill_color=color, line_color=color)

sg.set_options(background_color='#002740',
        text_element_background_color='#002740',
        element_background_color='#002740',
        scrollbar_color='#780000',
        input_elements_background_color='#454242',
        button_color=('white','#454242'),
        text_color='#ffffff',
        element_text_color='#ffffff',
        input_text_color='#ffffff')

#Getting current path program is ran from
currentpath = os.getcwd()
modpath = currentpath

optionscfgfilename = currentpath + "\\unit_stats_tool.cfg"

try:
    optionscfg = open(optionscfgfilename, "r")
    for line in optionscfg:
        if re.search(r'^modpath =.\"(\S.*)\"', line) is not None:
            modpath = re.findall(r'^modpath =.\"(\S.*)\"', line)[0]   
        elif re.search(r'^movespeed_text =', line) is not None:
            movespeed_text = re.findall(r'^movespeed_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^freeupkeep_text =', line) is not None:
            freeupkeep_text = re.findall(r'^freeupkeep_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^uniqueunit_text =', line) is not None:
            uniqueunit_text = re.findall(r'^uniqueunit_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^generalunit_text =', line) is not None:
            generalunit_text = re.findall(r'^generalunit_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^accuracy1_text =', line) is not None:
            accuracy1_text = re.findall(r'^accuracy1_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^accuracy1_min =', line) is not None:
            accuracy1_min = float(re.findall(r'^accuracy1_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy1_max =', line) is not None:
            accuracy1_max = float(re.findall(r'^accuracy1_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy2_text =', line) is not None:
            accuracy2_text = re.findall(r'^accuracy2_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^accuracy2_min =', line) is not None:
            accuracy2_min = float(re.findall(r'^accuracy2_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy2_max =', line) is not None:
            accuracy2_max = float(re.findall(r'^accuracy2_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy3_text =', line) is not None:
            accuracy3_text = re.findall(r'^accuracy3_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^accuracy3_min =', line) is not None:
            accuracy3_min = float(re.findall(r'^accuracy3_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy3_max =', line) is not None:
            accuracy3_max = float(re.findall(r'^accuracy3_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy4_text =', line) is not None:
            accuracy4_text = re.findall(r'^accuracy4_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^accuracy4_min =', line) is not None:
            accuracy4_min = float(re.findall(r'^accuracy4_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy4_max =', line) is not None:
            accuracy4_max = float(re.findall(r'^accuracy4_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy5_text =', line) is not None:
            accuracy5_text = re.findall(r'^accuracy5_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^accuracy5_min =', line) is not None:
            accuracy5_min = float(re.findall(r'^accuracy5_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy5_max =', line) is not None:
            accuracy5_max = float(re.findall(r'^accuracy5_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy6_text =', line) is not None:
            accuracy6_text = re.findall(r'^accuracy6_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^accuracy6_min =', line) is not None:
            accuracy6_min = float(re.findall(r'^accuracy6_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^accuracy6_max =', line) is not None:
            accuracy6_max = float(re.findall(r'^accuracy6_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^range_text =', line) is not None:
            range_text = re.findall(r'^range_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^ammo_text =', line) is not None:
            ammo_text = re.findall(r'^ammo_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^gunpowder_text =', line) is not None:
            gunpowder_text = re.findall(r'^gunpowder_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^aprange_text =', line) is not None:
            aprange_text = re.findall(r'^aprange_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^apsec_text =', line) is not None:
            apsec_text = re.findall(r'^apsec_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^secatt_text =', line) is not None:
            secatt_text = re.findall(r'^secatt_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^scrub_text =', line) is not None:
            scrub_text = re.findall(r'^scrub_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^sand_text =', line) is not None:
            sand_text = re.findall(r'^sand_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^forest_text =', line) is not None:
            forest_text = re.findall(r'^forest_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^snow_text =', line) is not None:
            snow_text = re.findall(r'^snow_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^morale_text =', line) is not None:
            morale_text = re.findall(r'^morale_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^morale1_text =', line) is not None:
            morale1_text = re.findall(r'^morale1_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^morale1_min =', line) is not None:
            morale1_min = int(re.findall(r'^morale1_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale1_max =', line) is not None:
            morale1_max = int(re.findall(r'^morale1_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale2_text =', line) is not None:
            morale2_text = re.findall(r'^morale2_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^morale2_min =', line) is not None:
            morale2_min = int(re.findall(r'^morale2_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale2_max =', line) is not None:
            morale2_max = int(re.findall(r'^morale2_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale3_text =', line) is not None:
            morale3_text = re.findall(r'^morale3_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^morale3_min =', line) is not None:
            morale3_min = int(re.findall(r'^morale3_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale3_max =', line) is not None:
            morale3_max = int(re.findall(r'^morale3_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale4_text =', line) is not None:
            morale4_text = re.findall(r'^morale4_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^morale4_min =', line) is not None:
            morale4_min = int(re.findall(r'^morale4_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale4_max =', line) is not None:
            morale4_max = int(re.findall(r'^morale4_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale5_text =', line) is not None:
            morale5_text = re.findall(r'^morale5_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^morale5_min =', line) is not None:
            morale5_min = int(re.findall(r'^morale5_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale5_max =', line) is not None:
            morale5_max = int(re.findall(r'^morale5_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale6_text =', line) is not None:
            morale6_text = re.findall(r'^morale6_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^morale6_min =', line) is not None:
            morale6_min = int(re.findall(r'^morale6_min =.\"(\S.*)\"', line)[0])
        elif re.search(r'^morale6_max =', line) is not None:
            morale6_max = int(re.findall(r'^morale6_max =.\"(\S.*)\"', line)[0])
        elif re.search(r'^lockmorale_text =', line) is not None:
            lockmorale_text = re.findall(r'^lockmorale_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^moraleres_text =', line) is not None:
            moraleres_text = re.findall(r'^moraleres_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^moralelow_text =', line) is not None:
            moralelow_text = re.findall(r'^moralelow_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^moralenormal_text =', line) is not None:
            moralenormal_text = re.findall(r'^moralenormal_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^moraledisciplined_text =', line) is not None:
            moraledisciplined_text = re.findall(r'^moraledisciplined_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^moraleimpetuous_text =', line) is not None:
            moraleimpetuous_text = re.findall(r'^moraleimpetuous_text =.\"(\S.*)\"', line)[0]
        elif re.search(r'^moraleberserker_text =', line) is not None:
            moraleberserker_text = re.findall(r'^moraleberserker_text =.\"(\S.*)\"', line)[0]
    optionscfg.close()
except:
    sg.popup('Do you have a file called unit_stats_tool.cfg in the same folder as the program?', title='Error')
    
#GUI setup (PySimpleGUI)
layout =                [   [sg.Text('Select path to mod: ')],
                            [sg.Input(default_text=modpath, size=(100, 1), key='modpath'), sg.FolderBrowse(), sg.Button('Set', border_width=(3), button_color='#455642', tooltip="Press after selecting a folder or typing a path to confirm, select the modfolder of the mod you want to use")],
                            [sg.Text('Movement speed text: ', size=(17, 1)), sg.Input(default_text=movespeed_text, k = 'movespeedtext'), sg.Checkbox('Enable? ', k = 'enablemovespeed', default=True)],
                            [sg.Text('free_upkeep_unit text: ', size=(17, 1)), sg.Input(default_text=freeupkeep_text, k = 'freeupkeeptext'), sg.Checkbox('Enable? ', k = 'enablefreeupkeep', default=True), sg.Text('unique_unit text: ', size=(17, 1)), sg.Input(default_text=uniqueunit_text, k = 'uniqueunittext'), sg.Checkbox('Enable? ', k = 'enableuniqueunit', default=True), sg.Text('general_unit text: ', size=(17, 1)), sg.Input(default_text=generalunit_text, k = 'generalunittext'), sg.Checkbox('Enable? ', k = 'enablegeneralunit', default=True)],
                            [sg.Text('Range text: '), sg.Input(default_text=range_text, k = 'rangetext', size=(20, 1)), sg.Checkbox('Enable? ', k = 'enablerange', default=True), sg.Text('Ammo text: '), sg.Input(default_text=ammo_text, k = 'ammotext', size=(20, 1)), sg.Checkbox('Enable? ', k = 'enableammo', default=True)],
                            [sg.Text('Accuracy Ranges (low to high): '), sg.Checkbox('Enable? ', k = 'enableaccuracy', default=True), sg.Checkbox('Enable siege accuracy vs buildings? ', k = 'enableaccuracybuildings', default=True), sg.Checkbox('Enable siege accuracy vs towers? ', k = 'enableaccuracytowers', default=True)], 
                            [sg.Input(default_text=accuracy1_text, k = 'accuracy1text'), sg.Input(default_text=accuracy1_min, k = 'accuracy1min', size=(8, 1)), sg.Input(default_text=accuracy1_max, k = 'accuracy1max', size=(8, 1))],
                            [sg.Input(default_text=accuracy2_text, k = 'accuracy2text'), sg.Input(default_text=accuracy2_min, k = 'accuracy2min', size=(8, 1)), sg.Input(default_text=accuracy2_max, k = 'accuracy2max', size=(8, 1))],
                            [sg.Input(default_text=accuracy3_text, k = 'accuracy3text'), sg.Input(default_text=accuracy3_min, k = 'accuracy3min', size=(8, 1)), sg.Input(default_text=accuracy3_max, k = 'accuracy3max', size=(8, 1))],
                            [sg.Input(default_text=accuracy4_text, k = 'accuracy4text'), sg.Input(default_text=accuracy4_min, k = 'accuracy4min', size=(8, 1)), sg.Input(default_text=accuracy4_max, k = 'accuracy4max', size=(8, 1))],
                            [sg.Input(default_text=accuracy5_text, k = 'accuracy5text'), sg.Input(default_text=accuracy5_min, k = 'accuracy5min', size=(8, 1)), sg.Input(default_text=accuracy5_max, k = 'accuracy5max', size=(8, 1))],
                            [sg.Input(default_text=accuracy6_text, k = 'accuracy6text'), sg.Input(default_text=accuracy6_min, k = 'accuracy6min', size=(8, 1)), sg.Input(default_text=accuracy6_max, k = 'accuracy6max', size=(8, 1))],
                            [sg.Text(" ")],
                            [sg.Text('AP Projectiles text: ', size=(17, 1)), sg.Input(default_text=aprange_text, k = 'aprangetext'), sg.Checkbox('Enable? ', k = 'enableaprange', default=True), sg.Text('missile_gunpowder text: ', size=(17, 1)), sg.Input(default_text=gunpowder_text, k = 'gunpowdertext'), sg.Checkbox('Enable? ', k = 'enablegunpowder', default=True)],
                            [sg.Text('AP Secondary text: ', size=(17, 1)), sg.Input(default_text=apsec_text, k = 'apsectext'), sg.Checkbox('Enable? ', k = 'enableapsec', default=True)],
                            [sg.Text('Secondary Attack text: ', size=(17, 1)), sg.Input(default_text=secatt_text, k = 'secatttext'), sg.Checkbox('Enable? ', k = 'enablesecatt', default=True)],
                            [sg.Text(" ")],
                            [sg.Text('Terrain Bonuses '), sg.Checkbox('Enable? ', k = 'enableterrain', default=True)],
                            [sg.Text('stat_ground scrub: '), sg.Input(default_text=scrub_text, k = 'scrubtext'), sg.Text('stat_ground sand: '), sg.Input(default_text=sand_text, k = 'sandtext')],
                            [sg.Text('stat_ground forest: '), sg.Input(default_text=forest_text, k = 'foresttext'), sg.Text('stat_ground snow: '), sg.Input(default_text=snow_text, k = 'snowtext')],
                            [sg.Text(" ")],
                            [sg.Text('Morale Ranges: '), sg.Input(default_text=morale_text, k = 'moraletext'), sg.Checkbox('Enable? ', k = 'enablemorale', default=True), sg.Checkbox('Show Morale as number', k = 'enablemoralenr', default=False)],
                            [sg.Input(default_text=morale1_text, k = 'morale1text'), sg.Input(default_text=morale1_min, k = 'morale1min', size=(8, 1)), sg.Input(default_text=morale1_max, k = 'morale1max', size=(8, 1))],
                            [sg.Input(default_text=morale2_text, k = 'morale2text'), sg.Input(default_text=morale2_min, k = 'morale2min', size=(8, 1)), sg.Input(default_text=morale2_max, k = 'morale2max', size=(8, 1))],
                            [sg.Input(default_text=morale3_text, k = 'morale3text'), sg.Input(default_text=morale3_min, k = 'morale3min', size=(8, 1)), sg.Input(default_text=morale3_max, k = 'morale3max', size=(8, 1))],
                            [sg.Input(default_text=morale4_text, k = 'morale4text'), sg.Input(default_text=morale4_min, k = 'morale4min', size=(8, 1)), sg.Input(default_text=morale4_max, k = 'morale4max', size=(8, 1))],
                            [sg.Input(default_text=morale5_text, k = 'morale5text'), sg.Input(default_text=morale5_min, k = 'morale5min', size=(8, 1)), sg.Input(default_text=morale5_max, k = 'morale5max', size=(8, 1))],
                            [sg.Input(default_text=morale6_text, k = 'morale6text'), sg.Input(default_text=morale6_min, k = 'morale6min', size=(8, 1)), sg.Input(default_text=morale6_max, k = 'morale6max', size=(8, 1))],
                            [sg.Text('lock_morale text: ', size=(14, 1)), sg.Input(default_text=lockmorale_text, k = 'lockmoraletext'), sg.Checkbox('Enable? ', k = 'enablelockmorale', default=True), sg.Checkbox('Dont show morale if locked ', k = 'disableiflocked', default=True)],
                            [sg.Text('Morale Responses: ', size=(14, 1)), sg.Input(default_text=moraleres_text, k = 'moralerestext'), sg.Checkbox('Enable? ', k = 'enablemoraleres', default=True)],
                            [sg.Text('low: ', size=(14, 1)), sg.Input(default_text=moralelow_text, k = 'moralelowtext'), sg.Text('normal: ', size=(14, 1)), sg.Input(default_text=moralenormal_text, k = 'moralenormaltext')],
                            [sg.Text('disciplined: ', size=(14, 1)), sg.Input(default_text=moraledisciplined_text, k = 'moraledisciplinedtext'), sg.Text('impetuous: ', size=(14, 1)), sg.Input(default_text=moraleimpetuous_text, k = 'moraleimpetuoustext'), sg.Text('berserker: ', size=(14, 1)), sg.Input(default_text=moraleberserker_text, k = 'moraleberserkertext')],
                            [sg.Button('Remove Descriptions', border_width=(3), tooltip="Works to remove descriptions added by the tool, always press if there already are descriptions on top of your export_units file!"), LEDIndicator('descr_found'), sg.Button('Start', border_width=(3), button_color='#455642'), sg.Button('Save Options to cfg', border_width=(3), button_color='#455642'), sg.Button('Quit', border_width=(3), button_color='#780000')],
                            [sg.Output(size=(200, 22), key='-output-')]
                            ]
                            
#GUI loading
window = sg.Window('Medieval 2 Unit Descriptions Tool', layout, finalize=True, resizable=True)
window.maximize()
cleaned = 0
started = 0
path_set = 0

try:
    eduname = modpath + "\\data\\export_descr_unit.txt"
    dprojectilename = modpath + "\\data\\descr_projectile.txt"
    euname = modpath + "\\data\\text\\export_units.txt"
    outputfilename = modpath + "\\data\\text\\export_units_new.txt"
    inputfilename = modpath + "\\data\\text\\export_units_cleaned.txt"
    file_eu = open(euname, encoding='utf16')
    descount = 0
    path_set = 1
    for line in file_eu:
        if re.search(r'_descr\}.+?(Range:).+\\n\\n', line) is not None or re.search(r'_descr\}.+?(Accuracy:).+\\n\\n', line) is not None or re.search(r'_descr\}.+?(Morale:).+\\n\\n', line) is not None:
            descount += 1
    SetLED(window, 'descr_found', 'red' if descount > 5 else 'green')
    file_eu.seek(0)

    encodings = ['utf8', 'cp1252', 'cp1250']

    for i in encodings:
        try:
            file_edu = open(eduname, encoding=i)
            file_edu.readlines()
            file_edu.seek(0)
            break
        except UnicodeDecodeError:
            continue

    for i in encodings:
        try:
            file_dprojectile = open(dprojectilename, encoding=i)
            file_dprojectile.readlines()
            file_dprojectile.seek(0)
            break
        except UnicodeDecodeError:
            continue
except:
    path_set = 0

def eu_replacer(unit, move_speed, free_upkeep, unique_unit, general_unit, accuracy, accuracy_buildings, accuracy_towers, range, ammo, range_ap, gunpowder, ap_sec, sec_att, scrub, sand, forest, snow, morale, morale_res, lock_morale, siege):
    inputfile = open(inputfilename, 'r', encoding="utf16")
    outputfile = open(outputfilename, 'w', encoding="utf16")
    inputfile.seek(0)
    outputfile.seek(0)
    for line in inputfile.readlines():
        if re.search(r'\{(.+)_descr\}', line) is not None:
            eu_unit = re.findall(r'\{(.+)_descr\}', line)[0]
            if unit.strip() == eu_unit:
                if enable_lockmorale == True and lock_morale == 1:
                    lockmorale_descr = str((lockmorale_text + r"\\n"))
                else:
                    lockmorale_descr = ""
                if enable_morale == True:
                    if disable_if_locked is True and lock_morale == 1:
                        morale_descr = ""
                    else:
                        if enable_moralenr == False:
                            if int(morale) >= morale1_min and int(morale) <= morale1_max:
                                morale_descr = str((morale_text + morale1_text + r"\\n"))
                            elif int(morale) >= morale2_min and int(morale) <= morale2_max:
                                morale_descr = str((morale_text + morale2_text + r"\\n"))
                            elif int(morale) >= morale3_min and int(morale) <= morale3_max:
                                morale_descr = str((morale_text + morale3_text + r"\\n"))
                            elif int(morale) >= morale4_min and int(morale) <= morale4_max:
                                morale_descr = str((morale_text + morale4_text + r"\\n"))
                            elif int(morale) >= morale5_min and int(morale) <= morale5_max:
                                morale_descr = str((morale_text + morale5_text + r"\\n"))
                            elif int(morale) >= morale6_min and int(morale) <= morale6_max:
                                morale_descr = str((morale_text + morale6_text + r"\\n"))
                            else:
                                morale_descr = ""
                        if enable_moralenr is True:
                            morale_descr = str(morale_text + str(morale) + r"\\n") 
                else:
                    morale_descr = ""
                if enable_moraleres == True:
                    if disable_if_locked is True and lock_morale == 1:
                        morale_res_descr = ""
                    else:
                        if morale_res == "low":
                            morale_res_descr = str((moraleres_text + moralelow_text + r"\\n"))
                        elif morale_res == "normal":
                            morale_res_descr = str((moraleres_text + moralenormal_text + r"\\n"))
                        elif morale_res == "disciplined":
                            morale_res_descr = str((moraleres_text + moraledisciplined_text + r"\\n"))
                        elif morale_res == "impetuous":
                            morale_res_descr = str((moraleres_text + moraleimpetuous_text + r"\\n"))
                        elif morale_res == "berserker":
                            morale_res_descr = str((moraleres_text + moraleberserker_text + r"\\n"))
                        else:
                            morale_res_descr = ""
                else:
                    morale_res_descr = ""
                if enable_movespeed == True:
                    movespeed_descr = str(movespeed_text + str(int(float(move_speed)*100)) + "%" + r"\\n")
                else:
                    movespeed_descr = ""
                if enable_freeupkeep == True and free_upkeep == 1:
                    freeupkeep_descr = str(freeupkeep_text + r"\\n")
                else:
                    freeupkeep_descr = ""
                if enable_uniqueunit == True and unique_unit == 1:
                    uniqueunit_descr = str(uniqueunit_text + r"\\n")
                else:
                    uniqueunit_descr = ""
                if enable_generalunit == True and general_unit == 1:
                    generalunit_descr = str(generalunit_text + r"\\n")
                else:
                    generalunit_descr = ""
                if enable_secatt == True and sec_att > 0:
                    sec_att_descr = str(secatt_text + str(sec_att) + r"\\n")
                else:
                    sec_att_descr = ""
                #accuracy_buildings_descr = ""
                #accuracy_towers_descr = ""
                if enable_accuracy == True:
                    if accuracy > 0:
                        if accuracy > accuracy1_min and accuracy <= accuracy1_max:
                            if siege == 0:
                                accuracy_descr = str("Accuracy: " + str(accuracy1_text) + r"\\n")
                            elif siege == 1:
                                accuracy_descr = str("Accuracy versus units: " + str(accuracy1_text) + r"\\n")
                        elif accuracy > accuracy2_min and accuracy <= accuracy2_max:
                            if siege == 0:
                                accuracy_descr = str("Accuracy: " + str(accuracy2_text) + r"\\n")
                            elif siege == 1:
                                accuracy_descr = str("Accuracy versus units: " + str(accuracy2_text) + r"\\n")
                        elif accuracy > accuracy3_min and accuracy <= accuracy3_max:
                            if siege == 0:
                                accuracy_descr = str("Accuracy: " + str(accuracy3_text) + r"\\n")
                            elif siege == 1:
                                accuracy_descr = str("Accuracy versus units: " + str(accuracy3_text) + r"\\n")
                        elif accuracy > accuracy4_min and accuracy <= accuracy4_max:
                            if siege == 0:
                                accuracy_descr = str("Accuracy: " + str(accuracy4_text) + r"\\n")
                            elif siege == 1:
                                accuracy_descr = str("Accuracy versus units: " + str(accuracy4_text) + r"\\n")
                        elif accuracy > accuracy5_min and accuracy <= accuracy5_max:
                            if siege == 0:
                                accuracy_descr = str("Accuracy: " + str(accuracy5_text) + r"\\n")
                            elif siege == 1:
                                accuracy_descr = str("Accuracy versus units: " + str(accuracy5_text) + r"\\n")
                        elif accuracy > accuracy6_min and accuracy <= accuracy6_max:
                            if siege == 0:
                                accuracy_descr = str("Accuracy: " + str(accuracy6_text) + r"\\n")
                            elif siege == 1:
                                accuracy_descr = str("Accuracy versus units: " + str(accuracy6_text) + r"\\n")
                        else:
                            accuracy_descr = ""
                    else:
                        accuracy_descr = ""
                    if siege == 1:
                        if accuracy_buildings > 0 and enable_accuracy_buildings == 1:
                            if accuracy_buildings > accuracy1_min and accuracy_buildings <= accuracy1_max:
                                accuracy_buildings_descr = str("Accuracy versus buildings: " + str(accuracy1_text) + r"\\n")
                            elif accuracy_buildings > accuracy2_min and accuracy_buildings <= accuracy2_max:
                                accuracy_buildings_descr = str("Accuracy versus buildings: " + str(accuracy2_text) + r"\\n")
                            elif accuracy_buildings > accuracy3_min and accuracy_buildings <= accuracy3_max:
                                accuracy_buildings_descr = str("Accuracy versus buildings: " + str(accuracy3_text) + r"\\n")
                            elif accuracy_buildings > accuracy4_min and accuracy_buildings <= accuracy4_max:
                                accuracy_buildings_descr = str("Accuracy versus buildings: " + str(accuracy4_text) + r"\\n")
                            elif accuracy_buildings > accuracy5_min and accuracy_buildings <= accuracy5_max:
                                accuracy_buildings_descr = str("Accuracy versus buildings: " + str(accuracy5_text) + r"\\n")
                            elif accuracy_buildings > accuracy6_min and accuracy_buildings <= accuracy6_max:
                                accuracy_buildings_descr = str("Accuracy versus buildings: " + str(accuracy6_text) + r"\\n")
                            else:
                                accuracy_buildings_descr = ""
                        else:
                            accuracy_buildings_descr = ""
                        if accuracy_towers > 0 and enable_accuracy_towers == 1:
                            if accuracy_towers > accuracy1_min and accuracy_towers <= accuracy1_max:
                                accuracy_towers_descr = str("Accuracy versus towers: " + str(accuracy1_text) + r"\\n")
                            elif accuracy_towers > accuracy2_min and accuracy_towers <= accuracy2_max:
                                accuracy_towers_descr = str("Accuracy versus towers: " + str(accuracy2_text) + r"\\n")
                            elif accuracy_towers > accuracy3_min and accuracy_towers <= accuracy3_max:
                                accuracy_towers_descr = str("Accuracy versus towers: " + str(accuracy3_text) + r"\\n")
                            elif accuracy_towers > accuracy4_min and accuracy_towers <= accuracy4_max:
                                accuracy_towers_descr = str("Accuracy versus towers: " + str(accuracy4_text) + r"\\n")
                            elif accuracy_towers > accuracy5_min and accuracy_towers <= accuracy5_max:
                                accuracy_towers_descr = str("Accuracy versus towers: " + str(accuracy5_text) + r"\\n")
                            elif accuracy_towers > accuracy6_min and accuracy_towers <= accuracy6_max:
                                accuracy_towers_descr = str("Accuracy versus towers: " + str(accuracy6_text) + r"\\n")
                            else:
                                accuracy_towers_descr = ""
                        else:
                            accuracy_towers_descr = ""
                    else:
                        accuracy_buildings_descr = ""
                        accuracy_towers_descr = ""
                else:
                    accuracy_descr = ""
                    accuracy_buildings_descr = ""
                    accuracy_towers_descr = ""
                if enable_range == True and range > 0:
                    range_descr = str(range_text + str(range) + " meters" + r"\\n")
                else:
                    range_descr = ""
                if enable_ammo == True and ammo > 0:
                    ammo_descr = str(ammo_text + str(ammo) + r"\\n")
                else:
                    ammo_descr = ""
                if enable_aprange == True and range_ap == 1:
                    rangeap_descr = str(aprange_text + r"\\n")
                else:
                    rangeap_descr = ""
                if enable_gunpowder == True and gunpowder == 1:
                    gunpowder_descr = str(gunpowder_text + r"\\n")
                else:
                    gunpowder_descr = ""
                if enable_apsec == True and ap_sec == 1:
                    apsec_descr = str(apsec_text + r"\\n")
                else:
                    apsec_descr = ""
                if enable_terrain == 1:
                    terrain_bonus_descr = ""
                    bonuslist = []
                    if scrub > 0:
                        bonuslist.append(scrub_text)
                    if sand > 0:
                        bonuslist.append(sand_text)
                    if forest > 0:
                        bonuslist.append(forest_text)
                    if snow > 0:
                        bonuslist.append(snow_text)
                    i = 0
                    for bonus in bonuslist:
                        try:
                            if i == 0:
                                terrain_bonus_descr = "Terrain bonus: " + bonuslist[i]
                            elif i > 0:
                                terrain_bonus_descr = terrain_bonus_descr + ", " + bonuslist[i]
                            i += 1
                        except:
                            continue  
                    if len(bonuslist) > 0:
                        terrain_bonus_descr = (terrain_bonus_descr + r"\\n")
                    else:
                        terrain_bonus_descr = ""
                    terrain_malus_descr = ""
                    maluslist = []
                    if scrub < 0:
                        maluslist.append(scrub_text)
                    if sand < 0:
                        maluslist.append(sand_text)
                    if forest < 0:
                        maluslist.append(forest_text)
                    if snow < 0:
                        maluslist.append(snow_text)
                    i = 0
                    for malus in maluslist:
                        try:
                            if i == 0:
                                terrain_malus_descr = "Terrain malus: " + maluslist[i]
                            elif i > 0:
                                terrain_malus_descr = terrain_malus_descr + ", " + maluslist[i]
                            i += 1
                        except:
                            continue
                    if len(maluslist) > 0:
                        terrain_malus_descr = (terrain_malus_descr + r"\\n")
                    else:
                        terrain_malus_descr = ""
                else:
                    terrain_bonus_descr = ""
                    terrain_malus_descr = ""
                changedline = "_descr}" + str(lockmorale_descr) + str(morale_descr) + str(morale_res_descr) + str(movespeed_descr) + str(freeupkeep_descr) + str(uniqueunit_descr) + str(generalunit_descr) + str(sec_att_descr) + str(apsec_descr) + str(accuracy_descr) + str(accuracy_buildings_descr) + str(accuracy_towers_descr) + str(range_descr) + str(ammo_descr) + str(rangeap_descr) + str(gunpowder_descr) + str(terrain_bonus_descr) + str(terrain_malus_descr) + (r"\\n")
                print(changedline)
                regexsub = re.sub(r'_descr\}', changedline, line)
                #print(regexsub)
                outputfile.write(regexsub)
            else:
                outputfile.write(line)
        else:
            outputfile.write(line)
    inputfile.close()      
    outputfile.close()      
    inputfile = open(inputfilename, 'w', encoding="utf16")
    outputfile = open(outputfilename, 'r', encoding="utf16")
    for line in outputfile:
        inputfile.write(line)
                
try:
    while True: 

        # ---------------Needed to use input from GUI----------------------------------

        event, values = window.read()

        if event == 'Set':
            if (values['modpath']) != "":
                modpath = values['modpath']

            eduname = modpath + "\\data\\export_descr_unit.txt"
            dprojectilename = modpath + "\\data\\descr_projectile.txt"
            euname = modpath + "\\data\\text\\export_units.txt"
            outputfilename = modpath + "\\data\\text\\export_units_new.txt"
            inputfilename = modpath + "\\data\\text\\export_units_cleaned.txt"
            file_eu = open(euname, encoding='utf16')
            descount = 0
            path_set = 1
            for line in file_eu:
                if re.search(r'_descr\}.+?(Range:).+\\n\\n', line) is not None or re.search(r'_descr\}.+?(Accuracy:).+\\n\\n', line) is not None or re.search(r'_descr\}.+?(Morale:).+\\n\\n', line) is not None:
                    descount += 1
            SetLED(window, 'descr_found', 'red' if descount > 5 else 'green')
            file_eu.seek(0)

            encodings = ['utf8', 'cp1252', 'cp1250']

            for i in encodings:
                try:
                    file_edu = open(eduname, encoding=i)
                    file_edu.readlines()
                    file_edu.seek(0)
                    break
                except UnicodeDecodeError:
                    continue

            for i in encodings:
                try:
                    file_dprojectile = open(dprojectilename, encoding=i)
                    file_dprojectile.readlines()
                    file_dprojectile.seek(0)
                    break
                except UnicodeDecodeError:
                    continue

        if event == 'Remove Descriptions':
            if path_set == 1:
                cleaned = 1
                inputfile = open(inputfilename, "w", encoding='utf16')
                if started == 1:
                    file_eu = open(euname, encoding='utf16')
                for line in file_eu.readlines():
                    if re.search(r'_descr\}(.+?\\n\\n)', line) is not None:
                        changedline = re.sub(r'_descr\}(.+?\\n\\n)', '_descr}', line)
                        inputfile.write(changedline)
                    else:
                        inputfile.write(line)
                inputfile.close()
                file_eu.close
                SetLED(window, 'descr_found', 'green')
            else:
                sg.popup('Confirm path first! (Press Set button)', title='Error')

        if event == 'Save Options to cfg':
            try:
                optionscfg = open(optionscfgfilename, "w")
                optionscfg.write("modpath = \"" + values['modpath'] + "\"" + "\n")
                optionscfg.write("movespeed_text = \"" + values['movespeedtext'] + "\"" + "\n")
                optionscfg.write("freeupkeep_text = \"" + values['freeupkeeptext'] + "\"" + "\n")
                optionscfg.write("uniqueunit_text = \"" + values['uniqueunittext'] + "\"" + "\n")
                optionscfg.write("generalunit_text = \"" + values['generalunittext'] + "\"" + "\n")
                optionscfg.write("accuracy1_text = \"" + values['accuracy1text'] + "\"" + "\n")
                optionscfg.write("accuracy1_min = \"" + values['accuracy1min'] + "\"" + "\n")
                optionscfg.write("accuracy1_max = \"" + values['accuracy1max'] + "\"" + "\n")
                optionscfg.write("accuracy2_text = \"" + values['accuracy2text'] + "\"" + "\n")
                optionscfg.write("accuracy2_min = \"" + values['accuracy2min'] + "\"" + "\n")
                optionscfg.write("accuracy2_max = \"" + values['accuracy2max'] + "\"" + "\n")
                optionscfg.write("accuracy3_text = \"" + values['accuracy3text'] + "\"" + "\n")
                optionscfg.write("accuracy3_min = \"" + values['accuracy3min'] + "\"" + "\n")
                optionscfg.write("accuracy3_max = \"" + values['accuracy3max'] + "\"" + "\n")
                optionscfg.write("accuracy4_text = \"" + values['accuracy4text'] + "\"" + "\n")
                optionscfg.write("accuracy4_min = \"" + values['accuracy4min'] + "\"" + "\n")
                optionscfg.write("accuracy4_max = \"" + values['accuracy4max'] + "\"" + "\n")
                optionscfg.write("accuracy5_text = \"" + values['accuracy5text'] + "\"" + "\n")
                optionscfg.write("accuracy5_min = \"" + values['accuracy5min'] + "\"" + "\n")
                optionscfg.write("accuracy5_max = \"" + values['accuracy5max'] + "\"" + "\n")
                optionscfg.write("accuracy6_text = \"" + values['accuracy6text'] + "\"" + "\n")
                optionscfg.write("accuracy6_min = \"" + values['accuracy6min'] + "\"" + "\n")
                optionscfg.write("accuracy6_max = \"" + values['accuracy6max'] + "\"" + "\n")
                optionscfg.write("range_text = \"" + values['rangetext'] + "\"" + "\n")
                optionscfg.write("ammo_text = \"" + values['ammotext'] + "\"" + "\n")
                optionscfg.write("aprange_text = \"" + values['aprangetext'] + "\"" + "\n")
                optionscfg.write("gunpowder_text = \"" + values['gunpowdertext'] + "\"" + "\n")
                optionscfg.write("apsec_text = \"" + values['apsectext'] + "\"" + "\n")
                optionscfg.write("secatt_text = \"" + values['secatttext'] + "\"" + "\n")
                optionscfg.write("scrub_text = \"" + values['scrubtext'] + "\"" + "\n")
                optionscfg.write("sand_text = \"" + values['sandtext'] + "\"" + "\n")
                optionscfg.write("forest_text = \"" + values['foresttext'] + "\"" + "\n")
                optionscfg.write("snow_text = \"" + values['snowtext'] + "\"" + "\n")
                optionscfg.write("morale_text = \"" + values['moraletext'] + "\"" + "\n")
                optionscfg.write("morale1_text = \"" + values['morale1text'] + "\"" + "\n")
                optionscfg.write("morale1_min = \"" + values['morale1min'] + "\"" + "\n")
                optionscfg.write("morale1_max = \"" + values['morale1max'] + "\"" + "\n")
                optionscfg.write("morale2_text = \"" + values['morale2text'] + "\"" + "\n")
                optionscfg.write("morale2_min = \"" + values['morale2min'] + "\"" + "\n")
                optionscfg.write("morale2_max = \"" + values['morale2max'] + "\"" + "\n")
                optionscfg.write("morale3_text = \"" + values['morale3text'] + "\"" + "\n")
                optionscfg.write("morale3_min = \"" + values['morale3min'] + "\"" + "\n")
                optionscfg.write("morale3_max = \"" + values['morale3max'] + "\"" + "\n")
                optionscfg.write("morale4_text = \"" + values['morale4text'] + "\"" + "\n")
                optionscfg.write("morale4_min = \"" + values['morale4min'] + "\"" + "\n")
                optionscfg.write("morale4_max = \"" + values['morale4max'] + "\"" + "\n")
                optionscfg.write("morale5_text = \"" + values['morale5text'] + "\"" + "\n")
                optionscfg.write("morale5_min = \"" + values['morale5min'] + "\"" + "\n")
                optionscfg.write("morale5_max = \"" + values['morale5max'] + "\"" + "\n")
                optionscfg.write("morale6_text = \"" + values['morale6text'] + "\"" + "\n")
                optionscfg.write("morale6_min = \"" + values['morale6min'] + "\"" + "\n")
                optionscfg.write("morale6_max = \"" + values['morale6max'] + "\"" + "\n")
                optionscfg.write("lockmorale_text = \"" + values['lockmoraletext'] + "\"" + "\n")
                optionscfg.write("moraleres_text = \"" + values['moralerestext'] + "\"" + "\n")
                optionscfg.write("moralelow_text = \"" + values['moralelowtext'] + "\"" + "\n")
                optionscfg.write("moralenormal_text = \"" + values['moralenormaltext'] + "\"" + "\n")
                optionscfg.write("moraledisciplined_text = \"" + values['moraledisciplinedtext'] + "\"" + "\n")
                optionscfg.write("moraleimpetuous_text = \"" + values['moraleimpetuoustext'] + "\"" + "\n")
                optionscfg.write("moraleberserker_text = \"" + values['moraleberserkertext'] + "\"" + "\n")
                optionscfg.close()
            except:
                sg.popup('Do you have a file called unit_stats_tool.cfg in the same folder as the program?', title='Error')
                continue

        # -------------------------Quit button-------------------------------------------
        if event == sg.WIN_CLOSED or event == 'Quit':
            if started == 1:
                os.remove(modpath + "\\data\\text\\export_units_cleaned.txt")
            break
        
        
        if event == 'Start':
            if path_set == 1:
                started = 1
                if cleaned == 0:
                    inputfile = open(inputfilename, "w", encoding='utf16')
                    for line in file_eu.readlines():
                        inputfile.write(line)
                    inputfile.close()
                movespeed_text = str(values['movespeedtext'])
                enable_movespeed = bool(values['enablemovespeed'])
                freeupkeep_text = str(values['freeupkeeptext'])
                enable_freeupkeep = values['enablefreeupkeep']
                uniqueunit_text = str(values['uniqueunittext'])
                enable_uniqueunit = values['enableuniqueunit']
                generalunit_text = str(values['generalunittext'])
                enable_generalunit = values['enablegeneralunit']
                enable_accuracy = values['enableaccuracy']
                enable_accuracy_buildings = values['enableaccuracybuildings']
                enable_accuracy_towers = values['enableaccuracytowers']
                accuracy1_text = str(values['accuracy1text'])
                accuracy1_min = float(values['accuracy1min'])
                accuracy1_max = float(values['accuracy1max'])
                accuracy2_text = str(values['accuracy2text'])
                accuracy2_min = float(values['accuracy2min'])
                accuracy2_max = float(values['accuracy2max'])
                accuracy3_text = str(values['accuracy3text'])
                accuracy3_min = float(values['accuracy3min'])
                accuracy3_max = float(values['accuracy3max'])
                accuracy4_text = str(values['accuracy4text'])
                accuracy4_min = float(values['accuracy4min'])
                accuracy4_max = float(values['accuracy4max'])
                accuracy5_text = str(values['accuracy5text'])
                accuracy5_min = float(values['accuracy5min'])
                accuracy5_max = float(values['accuracy5max'])
                accuracy6_text = str(values['accuracy6text'])
                accuracy6_min = float(values['accuracy6min'])
                accuracy6_max = float(values['accuracy6max'])
                range_text = str(values['rangetext'])
                enable_range = values['enablerange']
                ammo_text = str(values['ammotext'])
                enable_ammo = values['enableammo']
                aprange_text = str(values['aprangetext'])
                enable_aprange = values['enableaprange']
                gunpowder_text = str(values['gunpowdertext'])
                enable_gunpowder = values['enablegunpowder']
                apsec_text = str(values['apsectext'])
                enable_apsec = values['enableapsec']
                secatt_text = str(values['secatttext'])
                enable_secatt = values['enablesecatt']
                enable_terrain = values['enableterrain']
                scrub_text = str(values['scrubtext'])
                sand_text = str(values['sandtext'])
                forest_text = str(values['foresttext'])
                snow_text = str(values['snowtext'])
                morale_text = str(values['moraletext'])
                enable_morale = values['enablemorale']
                enable_moralenr = values['enablemoralenr']
                morale1_text = str(values['morale1text'])
                morale1_min = int(values['morale1min'])
                morale1_max = int(values['morale1max'])
                morale2_text = str(values['morale2text'])
                morale2_min = int(values['morale2min'])
                morale2_max = int(values['morale2max'])
                morale3_text = str(values['morale3text'])
                morale3_min = int(values['morale3min'])
                morale3_max = int(values['morale3max'])
                morale4_text = str(values['morale4text'])
                morale4_min = int(values['morale4min'])
                morale4_max = int(values['morale4max'])
                morale5_text = str(values['morale5text'])
                morale5_min = int(values['morale5min'])
                morale5_max = int(values['morale5max'])
                morale6_text = str(values['morale6text'])
                morale6_min = int(values['morale6min'])
                morale6_max = int(values['morale6max'])
                lockmorale_text =str(values['lockmoraletext'])
                enable_lockmorale = values['enablelockmorale']
                disable_if_locked = values['disableiflocked']
                enable_moraleres = values['enablemoraleres']
                moraleres_text = str(values['moralerestext'])
                moralelow_text = str(values['moralelowtext'])
                moralenormal_text = str(values['moralenormaltext'])
                moraledisciplined_text = str(values['moraledisciplinedtext'])
                moraleimpetuous_text = str(values['moraleimpetuoustext'])
                moraleberserker_text = str(values['moraleberserkertext'])
                edu_missile_unit = 0
                has_secondary = 0
                unit_found = 0
                for line in file_edu:
                    if re.search(r'^;', line) is not None:
                        continue
                    if re.search(r';', line) is not None:
                        line = line.split(';')[0]
                    if re.search(r'^dictionary\s', line) is not None:
                        #print("\n")
                        selected_unit_edu = re.findall(r'dictionary\s+(\S+)\s', line)[0]
                        move_speed_edu = 1.00
                        edu_projectile = "no"
                        free_upkeep_edu = 0
                        unique_unit_edu = 0
                        general_unit_edu = 0
                        has_secondary = 0
                        edu_missile_unit = 0
                        missile_ap_edu = 0
                        gunpowder_edu = 0
                        secondary_attack_edu = 0
                        secondary_ap_edu = 0
                        stat_scrub = 0
                        stat_sand = 0
                        stat_forest = 0
                        stat_snow = 0
                        morale_edu = 0
                        projectile_accuracy = 0.00
                        projectile_accuracy_buildings = 0.00
                        projectile_accuracy_towers = 0.00
                        edu_range = 0
                        edu_ammo = 0
                        morale_response_edu = ""
                        locked_morale = 0
                        unit_found = 1
                        siege_unit = 0
                        print(selected_unit_edu)
                    elif re.search(r'^category\s', line) is not None:
                        unit_category = re.findall(r'category\s+(\S+)\s', line)[0]
                    elif re.search(r'^move_speed_mod\s', line) is not None:
                        move_speed_edu = str(re.findall(r'move_speed_mod\s+(\S+)\s', line)[0])
                        print("Movement speed:",  move_speed_edu)
                    elif re.search(r'^attributes\s', line) is not None: 
                        if re.search(r'free_upkeep_unit', line) is not None:
                            free_upkeep_edu = 1
                            print("free_upkeep_edu")
                        if re.search(r'unique_unit', line) is not None:
                            unique_unit_edu = 1
                            print("unique_unit_edu")
                        if re.search(r'general_unit', line) is not None:
                            general_unit_edu = 1
                            print("general_unit_edu")
                    elif re.search(r'^stat_pri\s', line) is not None:
                        if unit_category == 'siege':
                            has_secondary = 1
                            secondary_attack_edu = re.findall(r'stat_pri\s+(\S.*?),', line)[0]
                        elif re.findall(r'^stat_pri\s+(\S.*?)\s', line)[0] != "no":
                            if re.findall(r'stat_pri\s.+?,.+?,.(\S.*?),', line)[0] != 'no' and unit_category != 'siege':
                                edu_missile_unit = 1
                                projectile_accuracy = 0.00
                                edu_projectile = re.findall(r'stat_pri\s.+?,.+?,.(\S.*?),', line)[0]
                                print("Projectile:",  edu_projectile)
                                projectile_found = 0
                                projectile_regex = r'^projectile\s+' + edu_projectile + r'\s'
                                file_dprojectile.seek(0)
                                for pline in file_dprojectile:
                                    if re.search(r'^;', pline) is not None:
                                        continue
                                    if re.search(r';', pline) is not None:
                                        pline = pline.split(';')[0]
                                    if re.search(r'^projectile\s', pline) is not None and re.search(projectile_regex, pline) is not None:
                                        projectile_found = 1
                                    if re.search(r'^accuracy_vs_units\s', pline) is not None and projectile_found == 1:
                                        projectile_accuracy = re.findall(r'accuracy_vs_units\s+(\S+)\s', pline)[0] 
                                        projectile_found = 0
                                        print("Accuracy:", projectile_accuracy)
                                edu_range = re.findall(r'stat_pri\s.+?,.+?,.+?,.(\S.*?),', line)[0]
                                print("Range:", edu_range)
                                edu_ammo = re.findall(r'stat_pri\s.+?,.+?,.+?,.+?,.(\S.*?),', line)[0]
                                print("Ammo:", edu_ammo)
                                if re.search(r'missile_gunpowder', line) is not None:
                                    print("missile_gunpowder")
                                    gunpowder_edu = 1
                    if re.search(r'^stat_pri_attr\s', line) is not None and re.search(r'^stat_pri_attr\s+.*ap', line) is not None:
                        if has_secondary == 1 and unit_category == 'siege':
                            secondary_ap_edu = 1
                            print("AP in melee")
                        elif edu_missile_unit == 1:
                            missile_ap_edu = 1
                            print("AP Projectiles")
                    if re.search(r'^stat_sec\s', line) is not None: 
                        if re.findall(r'stat_sec\s.+?,.+?,.(\S.*?),', line)[0] != 'no' and unit_category == 'siege':
                            projectile_accuracy = 0.00
                            edu_projectile = re.findall(r'stat_sec\s.+?,.+?,.(\S.*?),', line)[0]
                            print("Projectile:",  edu_projectile)
                            projectile_found = 0
                            projectile_regex = r'^projectile\s+' + edu_projectile + r'\s'
                            file_dprojectile.seek(0)
                            for pline in file_dprojectile:
                                if re.search(r'^;', pline) is not None:
                                    continue
                                if re.search(r';', pline) is not None:
                                    pline = pline.split(';')[0]
                                if re.search(r'^projectile\s', pline) is not None and re.search(projectile_regex, pline) is not None:
                                    projectile_found = 1
                                elif re.search(r'^accuracy_vs_units\s', pline) is not None and projectile_found == 1:
                                    projectile_accuracy = re.findall(r'accuracy_vs_units\s+(\S+)\s', pline)[0] 
                                    print("Accuracy:", projectile_accuracy)
                                elif re.search(r'^accuracy_vs_buildings\s', pline) is not None and projectile_found == 1:
                                    projectile_accuracy_buildings = re.findall(r'accuracy_vs_buildings\s+(\S+)\s', pline)[0] 
                                    print("Accuracy vs buildings:", projectile_accuracy_buildings)
                                elif re.search(r'^accuracy_vs_towers\s', pline) is not None and projectile_found == 1:
                                    projectile_accuracy_towers = re.findall(r'accuracy_vs_towers\s+(\S+)\s', pline)[0] 
                                    print("Accuracy vs towers:", projectile_accuracy_towers)
                                elif re.search(r'^projectile\s', pline) is not None and re.search(projectile_regex, pline) is None:
                                    projectile_found = 0
                            edu_range = re.findall(r'stat_sec\s.+?,.+?,.+?,.(\S.*?),', line)[0]
                            print("Range:", edu_range)
                            edu_ammo = re.findall(r'stat_sec\s.+?,.+?,.+?,.+?,.(\S.*?),', line)[0]
                            print("Ammo:", edu_ammo)
                        elif re.findall(r'stat_sec\s.+?,.+?,.+?,.+?,.+?,.(\S.*?),', line)[0] != 'no' and unit_category != 'siege':
                            has_secondary = 1
                            if edu_missile_unit == 0:
                                secondary_attack_edu = re.findall(r'stat_sec\s+(\S.*?),', line)[0]
                                print("Secondary Attack:", secondary_attack_edu)
                    elif re.search(r'^stat_sec_attr\s', line) is not None and re.search(r'^stat_sec_attr\s+.*ap', line) is not None and has_secondary == 1 and unit_category != 'siege':
                        secondary_ap_edu = 1
                        print("AP in melee")
                    elif re.search(r'^stat_sec_armour\s', line) is not None and int(re.findall(r'stat_sec_armour\s+(\S.*?),', line)[0]) > 0:
                        secondary_ap_edu = 0
                        secondary_attack_edu = 0
                        has_secondary = 0
                    elif re.search(r'stat_ground\s', line) is not None:
                        stat_scrub = re.findall(r'stat_ground\s+(.+?),', line)[0]
                        stat_sand = re.findall(r'stat_ground\s+.+?,.(\S+),', line)[0]
                        stat_forest = re.findall(r'stat_ground\s+.+?,.+?,.(\S+),', line)[0]
                        stat_snow = re.findall(r'stat_ground\s+.+?,.+?,.+?,.(\S+)\s', line)[0]
                        print("scrub bonus", stat_scrub)
                        print("sand bonus", stat_sand)
                        print("forest bonus", stat_forest)
                        print("snow bonus", stat_snow)
                    elif re.search(r'stat_mental\s', line) is not None:
                        morale_edu = re.findall(r'stat_mental\s+(.+?),', line)[0]
                        morale_response_edu = re.findall(r'stat_mental\s+.+?,.(\S+?),', line)[0]
                        print("Morale:", morale_edu)
                        print("Morale Response:", morale_response_edu)
                        if re.search(r'lock_morale\s', line) is not None:
                            locked_morale = 1
                            print("Can't be broken")
                        if unit_found == 1 and unit_category != 'ship':
                            if unit_category == 'siege':
                                siege_unit = 1
                            try:
                                eu_replacer(str(selected_unit_edu), str(move_speed_edu), int(free_upkeep_edu), int(unique_unit_edu), int(general_unit_edu), float(projectile_accuracy), float(projectile_accuracy_buildings), float(projectile_accuracy_towers), int(edu_range), int(edu_ammo), int(missile_ap_edu), int(gunpowder_edu), int(secondary_ap_edu), int(secondary_attack_edu), int(stat_scrub), int(stat_sand), int(stat_forest), int(stat_snow), int(morale_edu), str(morale_response_edu), int(locked_morale), int(siege_unit))
                            except:
                                continue
                inputfile.close()
                file_eu.close()
                i = 1
                renamed = 0
                while renamed == 0:
                    try:
                        os.rename(modpath + "\\data\\text\\export_units.txt", modpath + "\\data\\text\\export_units_backup" + str(i) + ".txt")
                        renamed = 1
                    except:
                        i += 1
                os.rename(modpath + "\\data\\text\\export_units_new.txt", modpath + "\\data\\text\\export_units.txt")
                SetLED(window, 'descr_found', 'red')
            else:
                sg.popup('Confirm path first! (Press Set button)', title='Error')    

except Exception as e:
    tb = traceback.format_exc()
    sg.Print(f'An error happened.  Here is the info:', e, tb)
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)
 