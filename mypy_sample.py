def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read().encode("utf-8")
