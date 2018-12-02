class Message:
    _end = '\033[0m'
    _header = '\033[95m'
    _okblue = '\033[94m'
    _okgreen = '\033[92m'
    _warning = '\033[93m'
    _fail = '\033[91m'
    _bold = '\033[1m'
    _underline = '\033[4m'

    def print_color(color, message):
        print(f'{color}{message}' + Message._end)
