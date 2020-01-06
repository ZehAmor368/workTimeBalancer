#!/usr/bin/python3

from WorkTime import WorkTime
from YamlHandler import YamlHandler
from Timer import Timer
from Timesheet import Timesheet
import sys


if len(sys.argv) < 2:
    print("Please enter an argument: start, stop, show")
    sys.exit()

cli_arguments = sys.argv[1:]

valid_arguments = ['start','stop','show']

if cli_arguments[0] not in valid_arguments:
    msg = "{} is not a valid argument. Please use:\n\n".format(cli_arguments[0])
    msg += " start\t-\tstarts WorkTimeBalancer for this day\n"
    msg += " stop\t-\tends WorkTimeBalancer for this day\n"
    msg += " show\t-\toutputs WorkTimeBalancers Timesheet"
    print(msg)
    sys.exit()

ts = Timesheet('Timesheet.yml')

if cli_arguments[0] == 'start':
    ts.startWork()
elif cli_arguments[0] == 'stop':
    ts.endWork()
elif cli_arguments[0] == 'show':
    print(ts)