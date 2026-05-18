def log_action(func):
    def wrapper(*args, **kwargs):
        print("Action logged")
        return func(*args, **kwargs)
    return wrapper