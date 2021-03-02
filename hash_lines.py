import hashlib
import threading

# Parameters to change
# ---------------------------------------------------------------
file = "test.txt"
encoding = "ansi"
# ---------------------------------------------------------------


def md5(file):
    count = 0
    f1 = open(file, "r", encoding=encoding)
    f2 = open(file + "_output_md5.txt", "w", encoding=encoding)
    for line in f1:
        count += 1
        striped = line.replace(*"\n", "")
        hash_object = hashlib.md5(striped.encode(encoding))
        hex_dig = hash_object.hexdigest()
        f2.write(hex_dig + "\t=>\t" + striped + '\n')
    f1.close()
    f2.close()
    print(f'{count} Processed lines => md5')


def sha1(file):
    count = 0
    f1 = open(file, "r", encoding=encoding)
    f2 = open(file + "_output_sha1.txt", "w", encoding=encoding)
    for line in f1:
        count += 1
        striped = line.replace(*"\n", "")
        hash_object = hashlib.sha1(striped.encode(encoding))
        hex_dig = hash_object.hexdigest()
        f2.write(hex_dig + "\t=>\t" + striped + '\n')
    f1.close()
    f2.close()
    print(f'{count} Processed lines => sha1')


def sha256(file):
    count = 0
    f1 = open(file, "r", encoding=encoding)
    f2 = open(file + "_output_sha256.txt", "w", encoding=encoding)
    for line in f1:
        count += 1
        striped = line.replace(*"\n", "")
        hash_object = hashlib.sha256(striped.encode(encoding))
        hex_dig = hash_object.hexdigest()
        f2.write(hex_dig + "\t=>\t" + striped + '\n')
    f1.close()
    f2.close()
    print(f'{count} Processed lines => sha256')


def sha512(file):
    count = 0
    f1 = open(file, "r", encoding=encoding)
    f2 = open(file + "_output_sha512.txt", "w", encoding=encoding)
    for line in f1:
        count += 1
        striped = line.replace(*"\n", "")
        hash_object = hashlib.sha512(striped.encode(encoding))
        hex_dig = hash_object.hexdigest()
        f2.write(hex_dig + "\t=>\t" + striped + '\n')
    f1.close()
    f2.close()


def main():
    # Threads
    print(f'Starting all 4 threads...\n')
    th1 = threading.Thread(target=md5, args=(file,))
    th2 = threading.Thread(target=sha1, args=(file,))
    th3 = threading.Thread(target=sha256, args=(file,))
    th4 = threading.Thread(target=sha512, args=(file,))

    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()

    print(f'\nAll threads closed succesfully')


if __name__ == '__main__':
    main()
