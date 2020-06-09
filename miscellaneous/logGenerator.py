#!/usr/bin/env python3

import os
import random

months = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
]

msgs = [
    'The ticket was modified while updating ',
    'Permission denied while closing ticket ',
    'Timeout while retrieving information ',
    'Connection to DB failed ',
    'Commented on ticket ',
    'Closed ticket ',
    "Ticket doesn't exist ",
    'Tried to add information to closed ticket ',
    'Created ticket '
]

usrs = [
    'mdouglas',
    'noel',
    'breee',
    'ac',
    'blossom',
    'rr.robinson',
    'mcintosh',
    'jackowens',
    'oren',
    'xlg',
    'ahmed.miller',
    'bpacheco',
    'enim.non',
    'flavia',
    'sri',
    'nonummy',
    'britanni',
    'montanap',
    'mai.hendrix',
    'kirknixon'
]

system = 'ubuntu.local'
category = 'ticky'
types =  ['INFO', 'ERROR']

with open ('logfile.log', 'a') as file:
    
    for i in range(20):    
        month = months[random.randint(0,11)]
        date = str(random.randint(10,28))
        time = str(random.randint(10,23)) + ':' + str(random.randint(10,59)) + ':' + str(random.randint(10,59))
        type_ = types[random.randint(0,1)]
        msg = msgs[random.randint(0, 8)]
        usr = usrs[random.randint(0, 19)]
        tckt_Num = "#" + str(random.randint(1000, 9999))
        if type_ == 'INFO':
            file.write(("{} {} {} {} {}: {} {}[{}] ({})").format(month, date, time, system, category, type_, msg, tckt_Num, usr))
        else:
            file.write(("{} {} {} {} {}: {} {}({})").format(month, date, time, system, category, type_, msg, usr))
           
        file.write("\n")
