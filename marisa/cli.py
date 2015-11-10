import datetime
from argparse import ArgumentParser
from laser_jab_manager import LaserJobManager


def parse_cli():
    parser = ArgumentParser(description='Tool for managing laser job recording')

    parser.add_argument(
        'user',
        metavar='USER',
        action='store',
        type=str,
        help='Name of current user')

    subparsers = parser.add_subparsers(help='operation to be performed')

    submit_job_parser = subparsers.add_parser('submit')
    submit_job_parser.set_defaults(which='submit')

    submit_job_parser.add_argument(
        '-t', '--time',
        action='store',
        type=str,
        required=True,
        help='Duration (HH:MM:MM, MM:SS, or SSSS)')

    submit_job_parser.add_argument(
        '-d', '--description',
        action='store',
        type=str,
        help='Optional description of job')

    query_job_parser = subparsers.add_parser('query')
    query_job_parser.set_defaults(which='query')

    #TODO: query stuff

    return parser.parse_args()


def time_str_to_seconds(time_str):
    tc = time_str.split(':')
    h = m = s = 0
    if len(tc) == 3:
        h = int(tc[0])
        m = int(tc[1])
        s = int(tc[2])
    elif len(tc) == 2:
        m = int(tc[0])
        s = int(tc[1])
    else:
        s = int(time_str)

    return datetime.timedelta(hours=h,minutes=m,seconds=s).total_seconds()


def run():
    props = parse_cli();
    lm = LaserJobManager(props.user)

    if props.which == 'submit':
        time = time_str_to_seconds(props.time)
        if not lm.submit_job(time, props.description):
            sys.exit(1)

    if props.which == 'query':
        #TODO: query stuff
        raise NotImplementedError('nope.avi')
