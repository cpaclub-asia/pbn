
import argparse

def args_src_dst(description1,help1,help2):
    parser = argparse.ArgumentParser(description=description1)
    parser.add_argument('src', metavar='src', type=str, help=help1)
    parser.add_argument('dst', metavar='dst', type=str, help=help2)
    args = parser.parse_args()

    return args.src,args.dst


def args_src_dst1_dst2(description1,help1,help2,help3):
    parser = argparse.ArgumentParser(description=description1)
    parser.add_argument('src', metavar='src', type=str, help=help1)
    parser.add_argument('dst1', metavar='dst1', type=str, help=help2)
    parser.add_argument('dst2', metavar='dst2', type=str, help=help3)
    args = parser.parse_args()

    return args.src,args.dst1,args.dst2


'''
    if not os.path.isdir(input_dir):
        parser.print_help()
        sys.exit(1)
'''