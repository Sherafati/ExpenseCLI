from backend import *
from docopt import docopt
import tabulate
usage = """

Usage:
  cli.py --init
  cli.py --show [<category>]
  cli.py --add <amount> <title> [<message>]



"""

arguments = docopt(usage)


if arguments['--init']:
    init()
    print("database created!")

if arguments['<amount>'] and arguments['--add']:
    try:
        newamnt = float(arguments['<amount>'])
    except:
        print(usage)
    else:
        add(newamnt, arguments['<title>'], arguments['<message>'])
        print("Added!")

if arguments['--show']:
    amnt, result = show(arguments['<category>'])
    print("total expense is: ", amnt)
    print(tabulate.tabulate(result))