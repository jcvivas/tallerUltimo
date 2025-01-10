import os

def check_for_null_bytes(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.feature')):
                filepath = os.path.join(root, file)
                with open(filepath, 'rb') as f:
                    content = f.read()
                    if b'\x00' in content:
                        print(f"Null byte found in file: {filepath}")

if __name__ == "__main__":
    check_for_null_bytes(".")

