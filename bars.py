import json


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as file_object:
            return json.load(file_object)
    except FileNotFoundError:
        print('File bars.json not found or it has wrong name')
        exit()
    except json.decoder.JSONDecodeError:
        print('File has invalid json structure')
        exit()
    except Exception as err:
        print('Error is:', str(err))
        exit()


def get_biggest_bar(bars_list) -> dict:
    return max(bars_list, key=lambda x: get_seats_count(x))


def get_smallest_bar(bars_list) -> dict:
    return min(bars_list, key=lambda x: get_seats_count(x))


def get_closest_bar(bars_list, longitude, latitude) -> dict:
    return min(bars_list, key=lambda x: get_distance_to_bar(x, longitude, latitude))


def input_coordinate(message='') -> float:
    while True:
        try:
            return float(input(message))
        except ValueError:
            print('Your input has to be a number')


def get_seats_count(bar: dict) -> str:
    return bar['properties']['Attributes']['SeatsCount']


def get_distance_to_bar(bar, your_longitude, your_latitude) -> str:
    bar_longitude = bar['geometry']['coordinates'][0]
    bar_latitude = bar['geometry']['coordinates'][1]
    return (bar_longitude - your_longitude) ** 2 + (bar_latitude - your_latitude) ** 2


def print_bar_name(bar_dict, message=''):
    print(message, bar_dict['properties']['Attributes']['Name'])


if __name__ == '__main__':
    bars_filepath = 'bars.json'
    bars = load_data(bars_filepath)['features']

    longitude = input_coordinate('Input your longitude:')
    latitude = input_coordinate('Input your latitude:')

    print_bar_name(get_biggest_bar(bars), 'The biggest bar -')
    print_bar_name(get_smallest_bar(bars), 'The smallest one -')
    print_bar_name(get_closest_bar(bars, longitude, latitude), 'The closest one -')
