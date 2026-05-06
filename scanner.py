import os
from hasher import hash_file
from signatures import load_signatures, is_malicious
from quarantine import quarantine_file

def scan_directory(path):
    signatures = load_signatures()
    results = []

    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            result = scan_file(full_path, signatures)
            results.append(result)

    return results


def scan_file(filepath, signatures):
    try:
        file_hash = hash_file(filepath)

        if is_malicious(file_hash, signatures):
            quarantine_file(filepath)
            return f"[INFECTED] {filepath}"
        else:
            return f"[CLEAN] {filepath}"

    except Exception as e:
        return f"[ERROR] {filepath}: {e}"