import sys

def main():
    print("Hello Wold! From Python: " + str(sys.version_info))
    if sys.version_info >= (3,6) and sys.version_info < (3,7):
        # Lets make this script fail for Python 3.6
        raise Exception('Python version 3.6.x is not supported!')
        
if __name__ == "__main__":
    main()
