import argparse
import csv


def analyze(input_csv, output_csv):
    input_fd = open(input_csv, 'r')
    input_data = csv.reader(input_fd)
    for row in input_data:
        # TODO
        # Main logic
        pass
    # TODO
    # Output file generation

    # TODO
    # Storing data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manages files and paths.')
    parser.add_argument('-i', '--input', action='store', nargs='?',
                        default='input.csv', help='Input csv file')
    parser.add_argument('-o', '--output', action='store', nargs='?',
                        default='output.csv', help='Output csv file')
    args = parser.parse_args()

    analyze(args.input, args.output)
