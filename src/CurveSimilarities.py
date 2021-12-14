import numpy as np
import pandas as pd
import Frechet

if __name__ == "__main__":

    # open file
    file_object = open(r"D:\MicrosoftVisualStudio\myprojects\Frechet_distance\test_files\loc3_each_timestamp.csv", encoding='UTF-8')
    try:
        file_content = file_object.readlines() # not very huge file, use readlines() to speed up
    finally:
        file_object.close()
    # curve_a
    splitor = ','
    curve_a = []
    for each in file_content:
        curve_a.append((float(each.split(splitor)[0]), float(each.split(splitor)[1])))


    # open file
    file_object = open(r"D:\MicrosoftVisualStudio\myprojects\Frechet_distance\test_files\loc4_each_timestamp.csv", encoding='UTF-8')
    try:
        file_content = file_object.readlines() # not very huge file, use readlines() to speed up
    finally:
        file_object.close()
    # curve_b
    splitor = ','
    curve_b = []
    for each in file_content:
        curve_b.append((float(each.split(splitor)[0]), float(each.split(splitor)[1])))

    # calculate Frechet distance
    print(Frechet.frechet_distance(curve_a,curve_b)) 