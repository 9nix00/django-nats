# -*- coding: utf-8 -*-
import os
import argparse
from django_nats import version
from cliez import conf
from cliez.base.component import Component
from cliez.parser import parse

conf.COMPONENT_ROOT = os.path.dirname(__file__)


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=Component.load_description('django_nats/manual/main.txt'),
        epilog='You can submit issues at: https://www.github.com/<project-address>',
    )
    parser.add_argument('--version', action='version', version='%(prog)s v{}'.format(version))
    parse(parser)
    pass


if __name__ == "__main__":
    main()
    pass

