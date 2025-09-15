def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    source = parts[1]
    target = parts[2]

    try:
        with open(source) as source_file, open(target, "w") as target_file:
            target_file.write(source_file.read())
    except FileNotFoundError:
        ...
