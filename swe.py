import sys
import argparse
from engine.Design import Design

def main(argv):
    args_parser = argparse.ArgumentParser(
        description="Executes the chosen design with the Semantic World Engine (SWE)."
    )

    args_parser.add_argument(
        "design_path",
        type=str,
        help="Path to design file"
    )

    parsed_args = args_parser.parse_args(argv[1:])
    design_path = parsed_args.design_path

    try:
        with open(design_path) as f:
            pass
    except Exception as e:
        print(f"Invalid arguments: {str(e)}", file=sys.stderr)
        return -1

    Design(design_path)

if "__main__" == __name__:
    sys.exit(main(sys.argv))
