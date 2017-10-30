# Command-line Interfaces using argparse module

# 4 steps:
#   - create a parser
#   - specify/define positional and optional arguments
#   - parse arguments
#   - use arguments


# Problem: compute distance between two points in coordinate space
# inputs:
#       - (x, y) coordinates of the 2 points
#       - metric to use: {'cosine', 'euclidean'}; default='euclidean'
# output:
#       - distance
#
# other behavior:
#       - optionally normalize to bring points to unit scale
#       - different levels of printing (on-screen viewing vs. piping to another program)


import argparse


def normalize(p):
    pass


def euclidean(p1, p2, norm=False):
    return 10


def cosine(p1, p2):
    return 15


def process(args):
    p1 = args.p1
    p2 = args.p2
    metric = args.metric
    if metric == 'cosine':
        result = cosine(p1, p2)
    if metric == 'euclidean':
        result = euclidean(p1, p2, norm=args.normalize)

    ## Verbosity levels
    if args.verbosity >= 2:
        print("Running '{}'".format(__file__))
        print('{} distance between {} and {} is: {}'.format(metric, p1, p2, result))
    elif args.verbosity >=1:
        print('Distance({}, {}): {}'.format(p1, p2, result))
    else:
        print(result)



def main():
    # Create a parser:
    parser = argparse.ArgumentParser(description='Compute distance between two points in space.')

    # Add positional arguments
    parser.add_argument('p1',                   # positional argument name; (doubles as varname in code)
                        nargs=2,                # num of argument values expected for this arg
                        type=float,             # for type checking at interface level
                        help='x and y coordinates of 1st point')

    parser.add_argument('p2',
                        nargs=2,
                        type=float,
                        help='x and y coordinates of 2nd point')

    # Add optional arguments
    parser.add_argument('-m',                               # short form
                        '--metric',                         # long form
                        choices=['euclidean', 'cosine'],    # choose one; default='cosine'
                        default='euclidean',
                        help='distance metric to apply.')

    parser.add_argument('-n',
                        '--normalize',
                        action='store_true',      # if specified, var norm is set to True (see docs for other action classes)
                        help='normalize vectors before computing distance')

    parser.add_argument('-v',
                        action='count',             # stores count of flag usage: -v, -vv, -vvv etc.
                        dest='verbosity',           # varname for storing flag usage count
                        default=0,                  # set to zero count if missing.
                        help='Verbosity level. Repeat for greater verbosity.')

    args = parser.parse_args()
    print('####\nFor demonstration purposes only. You would never print this object:\n{}\n####\n'.format(args))
    process(args)


if __name__ == '__main__':
    # This block is run only if current script is directly executed; skipped if imported from another module
    main()



