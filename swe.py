import sys
import argparse

def main(argv):
    args_parser = argparse.ArgumentParser(
        description="Executes the chosen design with the Semantic World Engine (SWE)."
    )

    args_parser.add_argument(
        "design",
        type=str,
        help="Path to design file"
    )

    parsed_args = args_parser.parse_args(argv[1:])
    design = parsed_args.design

    try:
        with open(design) as f:
            pass
    except Exception as e:
        print(f"Invalid arguments: {str(e)}", file=sys.stderr)
        return -1

    print("Successfully loaded design file.")

if "__main__" == __name__:
    sys.exit(main(sys.argv))
