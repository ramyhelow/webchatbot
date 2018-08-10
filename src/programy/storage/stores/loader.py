"""
Copyright (c) 2016-2018 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import logging
import argparse

from programy.config.file.yaml_file import YamlConfigurationFile
from programy.clients.events.console.config import ConsoleConfiguration

class DataLoader(object):

    @staticmethod
    def create_arguments():
        parser = argparse.ArgumentParser(description='Program-Y Set SQL Loader')

        parser.add_argument('-f', '--file', help="Load a single file")
        parser.add_argument('-d', '--dir', help="Load all files in directory")
        parser.add_argument('-s', '--subdir', action='store_true', help="Include subdirectories in search")
        parser.add_argument('-c', '--config', help="Configuration file containing store details")
        parser.add_argument('-e', '--engine', help="Name of storage engine in configuration file")
        parser.add_argument('-a', '--removeall', action='store_true', help="Remove contents of store before upload")

        return parser


if __name__ == '__main__':

    loader = DataLoader()

    parser = DataLoader.create_arguments()

    args = parser.parse_args()

    print(args)
