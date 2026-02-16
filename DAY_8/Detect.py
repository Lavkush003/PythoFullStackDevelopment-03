
def detect_file_type(file_path):
    with open(file_path, "rb") as file:
        header = file.read(8)   # read first 8 bytes

    # Known magic numbers
    if header.startswith(b"%PDF"):
        return "PDF file"
    elif header.startswith(b"\x89PNG"):
        return "PNG image"
    elif header.startswith(b"\xFF\xD8\xFF"):
        return "JPEG image"
    elif header.startswith(b"PK\x03\x04"):
        return "ZIP archive"
    elif header.startswith(b"MZ"):
        return "Windows EXE file"
    else:
        return "Unknown file type"


file_path = input("Enter file path: ")
result = detect_file_type(file_path)
print("Detected:", result)
