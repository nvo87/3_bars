import argparse
from data_loaders import load_from_json


def get_biggest_bar(bars_list) -> dict:
    return max(bars_list, key=get_seats_count)


def get_smallest_bar(bars_list) -> dict:
    return min(bars_list, key=get_seats_count)


def get_closest_bar(bars_list, longitude, latitude) -> dict:
    return min(
        bars_list,
        key=lambda x: get_distance_to_bar(x, longitude, latitude)
    )


def input_coordinate(message='') -> float:
    try:
        return float(input(message))
    except ValueError:
        return None


def get_seats_count(bar: dict) -> int:
    return bar['properties']['Attributes']['SeatsCount']


def get_distance_to_bar(bar, your_longitude, your_latitude) -> float:
    bar_longitude = bar['geometry']['coordinates'][0]
    bar_latitude = bar['geometry']['coordinates'][1]
    return ((bar_longitude - your_longitude) ** 2
            + (bar_latitude - your_latitude) ** 2)


def get_bar_name(bar_dict):
    return bar_dict['properties']['Attributes']['Name']


def parse_args():
    parser = argparse.ArgumentParser(
        description='Script gets you the smallest, biggest and closest bar')
    parser.add_argument('file_path', help='path to json file with bars data. '
        'You may download it here: https://devman.org/fshare/1503831681/4/')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    bars_filepath = parse_args().file_path
    try:
        bars = load_from_json(bars_filepath)['features']
    except FileNotFoundError:
        exit('File not found or its name is wrong')
    if bars is None:
        exit('File is empty or has wrong structure')

    longitude = input_coordinate('Input your longitude:')
    latitude = input_coordinate('Input your latitude:')
    if not longitude and latitude:
        exit('Your input has to be a number')

    print('The biggest bar -', get_bar_name(get_biggest_bar(bars)))
    print('The smallest one -', get_bar_name(get_smallest_bar(bars)))
    print(
        'The closest one-',
        get_bar_name(get_closest_bar(bars, longitude, latitude))
    )