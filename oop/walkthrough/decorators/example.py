def log_message(func):
    def wrapper(*args):
        print("Arguments to wrapper function...", args)
        print("Performing execution...")
        return func(*args)
    return wrapper
        
@log_message
def create_list_of_ints(n: int):
    return [i for i in range(0, n)]

@log_message
def concatenate_two_strings(string1: str, string2: str):
    return string1 + string2


if __name__ == "__main__":

    print("Calculating list of ints...")
    print(create_list_of_ints(10))

    print()
    print("Concatenating two strings...")
    print(concatenate_two_strings("Hello, ", "world."))