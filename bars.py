import json
import io


def load_data(filepath):
    with io.open(filepath, encoding='utf-8') as f_obj:
        return json.load(f_obj)


def get_biggest_bar(bars_list):
    return max(bars_list, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars_list):
    return min(bars_list, key=lambda x: x['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars_list, longitude, latitude):
    return min(bars_list, key=lambda x: (x['geometry']['coordinates'][0] - longitude) ** 2 - \
                                        (x['geometry']['coordinates'][1] - latitude) ** 2)


if __name__ == '__main__':
    bars_filepath = 'bars.json'
    bars = load_data(bars_filepath)
    bars_list = bars['features']

    longitude = float(input('Input your longitude:'))
    latitude = float(input('Input your latitude:'))

    print('The biggest bar -', get_biggest_bar(bars_list)['properties']['Attributes']['Name'])
    print('The smallest one -', get_smallest_bar(bars_list)['properties']['Attributes']['Name'])
    print('The closest one -', get_closest_bar(bars_list, longitude, latitude)['properties']['Attributes']['Name'])
