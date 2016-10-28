import json
import math


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        data = json.load(fh)  # загружаем из файла данные в словарь data
        return  data


def get_biggest_bar(data):
    max_seats_bar = None
    max_seats = 0
    for bar in data:
        if bar["Cells"]["SeatsCount"] > max_seats :
            max_seats_bar = bar
            max_seats = bar["Cells"]["SeatsCount"]
    return max_seats_bar


def get_smallest_bar(data):
    bar = get_biggest_bar(data)
    min_seats = bar["Cells"]["SeatsCount"]
    min_seats_bar = None
    for bar in data:
        if bar["Cells"]["SeatsCount"] < min_seats:
            min_seats_bar = bar
            min_seats = bar["Cells"]["SeatsCount"]
    return min_seats_bar



def get_closest_bar(data, longitude, latitude):
    clossest_distance = 0
    clossest_bar = None
    for bar in data:
        y = bar["Cells"]["geoData"]["coordinates"][0] - longitude
        x = bar["Cells"]["geoData"]["coordinates"][1] - latitude
        if (math.sqrt((math.pow(y,2)+ math.pow(x,2))) > clossest_distance):
            clossest_distance = math.sqrt((math.pow(y,2)+ math.pow(x,2)))
            clossest_bar = bar
    for bar in data:
        y = bar["Cells"]["geoData"]["coordinates"][0] -longitude
        x = bar["Cells"]["geoData"]["coordinates"][1] - latitude
        if (math.sqrt((math.pow(y,2)+ math.pow(x,2))) < clossest_distance):
            clossest_distance = math.sqrt((math.pow(y,2)+ math.pow(x,2)))
            clossest_bar = bar

    return clossest_bar

if __name__ == '__main__':
   pass
