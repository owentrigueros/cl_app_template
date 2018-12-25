name = "cl_app_template"

from .ClAppTemplate import whatever
from .options import get_parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    ClAppTemplate.whatever(args.ARG1)
