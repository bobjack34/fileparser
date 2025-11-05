from .parser import parse
import sys 

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m fileparser <filename>")
        print("test print")
        sys.exit(1)
    
    filename = sys.argv[1]
    try:
        info = parse(filename)
        print(f"File name: {info.name}")
        print(f"Suffix: {info.suffix}")
        print(f"Type: {info.type}")
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)