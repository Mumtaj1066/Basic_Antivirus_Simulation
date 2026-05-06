import json

SIGNATURE_FILE = "data/signatures.json"

def load_signatures():
    try:
        with open(SIGNATURE_FILE, "r") as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()


def is_malicious(file_hash, signatures):
    return file_hash in signatures