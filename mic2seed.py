import sounddevice as sd
import numpy as np
import hashlib
import binascii
import time
import os


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def record_audio(duration):
    print('Grabbing entropy from the air...')
    fs = 44100  # Sampling frequency
    seconds = duration  # Duration in seconds
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    return recording, fs


def calculate_sha256(data):
    sha256_hash = hashlib.sha256(data)
    return sha256_hash.hexdigest()


def sha256(input_data):
    return hashlib.sha256(input_data).digest()


def sha256_to_binary_string(hash_result):
    binary_string = ""
    for byte in hash_result:
        # Convert each byte to its binary representation and pad with zeros to ensure it's 8 bits long
        binary_string += format(byte, '08b')
    return binary_string


def binToHexa(n):
    bnum = int(n)
    temp = 0
    mul = 1
    # counter to check group of 4
    count = 1
    # char array to store hexadecimal number
    hexaDeciNum = ['0'] * 100
    # counter for hexadecimal number array
    i = 0
    while bnum != 0:
        rem = bnum % 10
        temp = temp + (rem * mul)
        # check if group of 4 completed
        if count % 4 == 0:
            # check if temp < 10
            if temp < 10:
                hexaDeciNum[i] = chr(temp + 48)
            else:
                hexaDeciNum[i] = chr(temp + 55)
            mul = 1
            temp = 0
            count = 1
            i = i + 1
        # group of 4 is not completed
        else:
            mul = mul * 2
            count = count + 1
        bnum = int(bnum / 10)
    # check if at end the group of 4 is not completed
    if count != 1:
        hexaDeciNum[i] = chr(temp + 48)
    # check at end the group of 4 is completed
    if count == 1:
        i = i - 1
    return hexaDeciNum[i]


def bytes_to_binary_string(byte_data):
    binary_string = ''.join(format(byte, '08b') for byte in byte_data)
    return binary_string


def binary_string_to_mnemonic(binary_string, word_list_file):
    bytes = 32
    tmp_bin = binary_string
    # convert string with 0 and 1 to hex and to binary
    bin_list = []
    start = 0
    part = 4
    while start < len(tmp_bin):  # Splitting string in 4 digits parts
        bin_list.append(tmp_bin[start: start + part])
        start += part
    # convert list with four 0 and 1 digits to list with hexadecimal letters
    hex_list = []
    for bn in bin_list:
        hex_list.append(binToHexa(bn))
    hex_ent = ''.join(hex_list)  # creates hexadecimal string of entropy
    tmp_bin = binascii.unhexlify(hex_ent)  # binary of entropy
    tmp_hex = binascii.hexlify(tmp_bin)  # hexadecimal of entropy
    str_hash = hashlib.sha256(tmp_bin).hexdigest()  # hashing binary of entropy
    # Converting hash to binary
    int_hash = int(str_hash, base=16)
    bin_hash = str(bin(int_hash))[2:]
    # Adding checksum to entropy
    checksum = bin(int(str_hash, 16))[2:].zfill(256)[: bytes * 8 // 32]
    print(color.YELLOW + 'Checksum: ' + color.END + f'{checksum}')
    binary_seed = (bin(int(tmp_hex, 16))[2:].zfill(bytes * 8) + checksum)
    print(f'binary_seed: {binary_seed}')
    # Split the binary string into chunks of 11 bits each
    chunks = [binary_seed[i:i+11] for i in range(0, len(binary_string), 11)]
    # Open wordlist file, using english since other languages do not have sense
    with open(word_list_file, 'r') as f:
        word_list = [word.strip() for word in f.readlines()]
    # Map each chunk to its corresponding index in the word list
    indexes = [int(chunk, 2) for chunk in chunks]
    # Generate the mnemonic by retrieving words from the word list
    mnemonic = ' '.join(word_list[index] for index in indexes)
    return mnemonic

# START
# Changes working directory
os.chdir('/opt/Tools/WalletGen/Mic2Seed')
print(color.GREEN + 'This tool creates a BIP39 mnemonic seed getting entropy from your microphone' + color.END)
# Alert, check mike
print(color.RED + 'Note that this tool may have undesired results with not properly working hardware. Check your hardware before continuing' + color.END)
print(color.YELLOW + 'You could use the MicCheck tool or try to record something with the gnome-recorder' + color.END)
print(color.RED + 'Note that this tool may have undesired results with not properly working hardware. Check your hardware before continuing' + color.END)
input('Press enter to continue...')
duration = 30  # Duration in seconds
recording, fs = record_audio(duration)

if recording is None or fs is None:
    exit(color.RED + 'No recording available, check your hardware\nEXITING\n' + color.END)

audio_bytes = recording.tobytes()
#print('audio bytes: ' + str(audio_bytes))
hashed_data = sha256(audio_bytes)
binary_string = sha256_to_binary_string(hashed_data)
print("Binary string:", binary_string)

word_list_file = "Wordlists/b39en"  # Replace this with the path to your BIP39 word list file

# Generate the BIP39 mnemonic directly from the binary string
mnemonic = binary_string_to_mnemonic(binary_string, word_list_file)

print('==========')
print(color.DARKCYAN + mnemonic + color.END)
print('==========')
print(color.BLUE + 'Made by the AnuBitux Team!' + color.END)
print('==========')
