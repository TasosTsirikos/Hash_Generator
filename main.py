import hashlib

def generate_hash(data, algorithm):
    hash_object = hashlib.new(algorithm)
    hash_object.update(data.encode('utf-8'))
    return hash_object.hexdigest()

def main():
    data = input("Enter the data to hash: ")
    algorithm = input("Enter the encryption algorithm (e.g., MD5, SHA1, SHA256): ")
    hash_value = generate_hash(data, algorithm)
    print(f"The hash value of '{data}' using {algorithm} is: {hash_value}")

if __name__ == "__main__":
    main()
