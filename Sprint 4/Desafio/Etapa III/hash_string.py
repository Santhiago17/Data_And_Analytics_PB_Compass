import hashlib

def generate_hash(input_string):
    return hashlib.sha1(input_string.encode()).hexdigest()

if __name__ == "__main__":
    while True:
        input_string = input("Enter a string to hash: ")
        if input_string.strip().lower() == 'exit':
            break
        print("SHA-1 Hash:", generate_hash(input_string))