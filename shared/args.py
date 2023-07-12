
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

def args_src_dst1_dst2_full_threads(description1,help1,help2,help3):
    parser = argparse.ArgumentParser(description=description1)
    parser.add_argument('src', metavar='src', type=str, help=help1)
    parser.add_argument('dst1', metavar='dst1', type=str, help=help2)
    parser.add_argument('dst2', metavar='dst2', type=str, help=help3)
    parser.add_argument('full', metavar='full', type=str, help=help3)
    parser.add_argument('threads', metavar='threads', type=int, help=help3)
    args = parser.parse_args()
    if(args.full=="True"):
        full=True
    else:
        full=False

    return args.src,args.dst1,args.dst2,full,args.threads

'''
    if not os.path.isdir(input_dir):
        parser.print_help()
        sys.exit(1)
'''