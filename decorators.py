def file_open_err(func):
    def wrapper_opening_file_errors(self, fname) -> None:
        try:
            func(self, fname)
        except FileNotFoundError:
            # This can be logged if need be
            print("ERR: Given file not found!")
            quit(1)
    return wrapper_opening_file_errors
