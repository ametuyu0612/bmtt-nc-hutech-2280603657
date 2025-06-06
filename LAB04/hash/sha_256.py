import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    # Bước trên chuyển dữ liệu thành bytes và cập nhập đối tượng hash
    return sha256_hash.hexdigest() # Trả về biểu diễn hex chuỗi hash

data_to_hash = input("Nhập dữ liệu cho SHA-256: ")
hash_value = calculate_sha256_hash(data_to_hash)
print("Giá trị băm SHA-256: ", hash_value)