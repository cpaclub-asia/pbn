import os
import sys
import argparse
from shared.file_processor import process_files

def main():
    parser = argparse.ArgumentParser(description='HTML File Processor')
    parser.add_argument('input_dir', metavar='input_dir', type=str, help='Path to the input directory')
    parser.add_argument('output_dir', metavar='output_dir', type=str, help='Path to the output directory')
    parser.add_argument('assets_dir', metavar='assets_dir', type=str, help='Path to the output directory')
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    assets_dir = args.assets_dir

    if not os.path.isdir(input_dir):
        parser.print_help()
        sys.exit(1)

    # Создание output_dir, если он не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    process_files(input_dir, output_dir,assets_dir)

if __name__ == '__main__':
    main()
