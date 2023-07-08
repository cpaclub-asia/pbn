
import argparse

def args_src_dst(description1,help1,help2):
    parser = argparse.ArgumentParser(description=description1)
    parser.add_argument('src', metavar='src', type=str, help=help1)
    parser.add_argument('dst', metavar='dst', type=str, help=help2)
    args = parser.parse_args()

    return args.src,args.dst

    if not os.path.isdir(input_dir):
        parser.print_help()
        sys.exit(1)