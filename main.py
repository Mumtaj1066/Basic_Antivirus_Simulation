from scanner import scan_directory
from config import SCAN_PATH

def main():
    print("Starting antivirus scan...")
    results = scan_directory(SCAN_PATH)

    print("\nScan complete.")
    for r in results:
        print(r)

if __name__ == "__main__":
    main()