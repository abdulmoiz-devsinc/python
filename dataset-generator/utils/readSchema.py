def read_schema_file(path: str) -> str:
    try:
        with open(path, "r") as file:
            return [line.strip() for line in file if line.strip()]

    except FileNotFoundError:
        raise FileNotFoundError(f"Schema file not found: {path}")

    except PermissionError:
        raise PermissionError(f"Permission denied while accessing: {path}")

    except Exception as e:
        raise RuntimeError(f"Failed to read schema file: {e}") from e
