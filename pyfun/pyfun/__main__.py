import sys
from .classmodule import MyClass
from .funcmodule import gen_gitignore
from .funcmodule import print_random0
from .funcmodule import print_timer0
from .funcmodule import gen_flask_hello_world
from .funcmodule import gen_flask_hello_world_heroku
from .funcmodule import print_flask_session
from .funcmodule import print_binary_search
from .funcmodule import print_threading
import pyfun

def help(cmd='all'):
    cmd_help = {}
    cmd_help['help'] = '$ pyfun help:'
    cmd_help['help'] += '\n\tpyfun help : show all commands'
    
    cmd_help['git'] = '$ pyfun git:'
    cmd_help['git'] += '\n\tpyfun git ignore : gen py gitignore'
    
    cmd_help['pycheat'] = '$ pyfun pycheat:'
    cmd_help['pycheat'] += '\n\tpyfun pycheat random : prints random num ex'
    cmd_help['pycheat'] += '\n\tpyfun pycheat timer : prints timer ex'
    
    cmd_help['flask'] = '$ pyfun flask:'
    cmd_help['flask'] += '\n\tpyfun flask hello_world : gen flask hello world proj'
    cmd_help['flask'] += '\n\tpyfun flask hello_world_heroku : gen flask hello world proj for heroku'
    cmd_help['flask'] += '\n\tpyfun flask session : flask session ex'
    
    cmd_help['algo'] = '$ pyfun algo:'
    cmd_help['algo'] += '\n\tpyfun algo binary_search : prints binary search code'

    cmd_help['concy'] = '$ pyfun concy:'
    cmd_help['concy'] += '\n\tpyfun concy threading : prints threading ex'


    if cmd == 'all':
        for command in cmd_help:
            print(cmd_help[command]+'\n')
    elif cmd_help.get(cmd, 0):
        print(cmd_help[cmd])
    else:
        print('help not availible for {}'.format(cmd))



def get_help():
    print('cmd not found\n$ pyfun help')

def handle_git(args):
    if len(args) == 0:
        help('git')
    elif len(args) == 1:
        if args[0] == 'ignore':
            gen_gitignore()
        else:
            help('git')   
    else:
        help('git')

def handle_pycheat(args):
    if len(args) == 0:
        help('pycheat')
    if len(args) == 1:
        if args[0] == 'random':
            print_random0()
        if args[0] == 'timer':
            print_timer0()
        else:
            help('pycheat')

def handle_flask(args):
    if len(args) == 0:
        help('flask')
    elif len(args) == 1:
        if args[0] == 'hello_world':
            gen_flask_hello_world()
        elif args[0] == 'hello_world_heroku':
            gen_flask_hello_world_heroku()
        elif args[0] == 'session':
            print_flask_session()
        else:
            help('flask')
    else:
        help('flask')

def handle_algo(args):
    if len(args) == 0:
        help('algo')
    elif len(args) == 1:
        if args[0] == 'binary_search':
            print_binary_search()
        else:
            help('algo')
    else:
        help('algo')

def handle_concy(args):
    if len(args) == 0:
        help('concy')
    elif len(args) == 1:
        if args[0] == 'threading':
            print_threading()
        else:
            help('concy')
    else:
        help('concy')

def handle_args(args):
    if len(args) == 0:
        help()
    elif len(args) >= 1:
        if args[0] == 'git':
            handle_git(args[1:])
        elif args[0] == 'pycheat':
            handle_pycheat(args[1:])
        elif args[0] == 'flask':
            handle_flask(args[1:])
        elif args[0] == 'algo':
            handle_algo(args[1:])
        elif args[0] == 'concy':
            handle_concy(args[1:])
        elif args[0] == 'help':
            help()
        else:
            get_help()
    else:
        print('aparenltly there are negative #args')


def main():
    args = sys.argv[1:]
    
    handle_args(args)

if __name__ == '__main__':
    main()