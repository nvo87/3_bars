import argparse
import sys as _sys


class MyParser(argparse.ArgumentParser):
    def print_usage(self, file=None):
        if file is None:
            file = _sys.stdout
        self._print_message(self.format_usage(), file)
        print('You have to specify a filepath to bars.json. '
              'You may download it here: '
              'https://devman.org/fshare/1503831681/4/')