import sys

def parse_args(args, arg_pattern):
    parsed_args = {}
    current_flag = None
    for arg in args[1:]:
        if arg.startswith('-'):
            current_flag = arg[1:]
            if current_flag not in arg_pattern:
                return f"Error: Unknown flag '{current_flag}'"
            if arg_pattern[current_flag] == "bool":
                parsed_args[current_flag] = True
            else:
                parsed_args[current_flag] = []
        else:
            if current_flag:
                if arg_pattern[current_flag] == "int":
                    try:
                        parsed_args[current_flag].append(int(arg))
                    except ValueError:
                        return f"Error: Value '{arg}' for flag '{current_flag}' must be an integer"
                elif arg_pattern[current_flag] == "str":
                    parsed_args[current_flag] = arg
                elif arg_pattern[current_flag] == "list":
                    parsed_args[current_flag].append(arg)
                else:
                    return f"Error: Unknown value type '{arg_pattern[current_flag]}' for flag '{current_flag}'"
            else:
                return f"Error: Value '{arg}' does not belong to any flag"

    # Fill default values for any missing flags
    for flag, value_type in arg_pattern.items():
        if flag not in parsed_args:
            if value_type == "bool":
                parsed_args[flag] = False
            elif value_type == "int":
                parsed_args[flag] = 0
            elif value_type == "str":
                parsed_args[flag] = ""
            elif value_type == "list":
                parsed_args[flag] = []
            else:
                return f"Error: Unknown value type '{value_type}' for flag '{flag}'"

    # Convert single-value flags from lists to scalars
    for flag, value in parsed_args.items():
        if isinstance(value, list) and len(value) == 1:
            parsed_args[flag] = value[0]

    return parsed_args

if __name__ == "__main__":
    arg_pattern = {
        "l": "bool",
        "p": "int",
        "d": "str",
        "g": "list",
    }
    args = sys.argv
    parsed_args = parse_args(args, arg_pattern)
    if isinstance(parsed_args, dict):
        print("Parsed arguments:")
        for flag, value in parsed_args.items():
            print(f"{flag}: {value}")
    else:
        print(parsed_args)
