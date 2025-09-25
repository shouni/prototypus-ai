# cli.py
import fire

class PrototypusAI:
    def __init__(self):
        pass

    def hello(self):
        print("Hello, world!")

    def  byebye(self):
        print("Byebye, world!")

def main():
    """
    Main entry point for the Prototypus AI CLI.
    """
    fire.Fire(PrototypusAI)

if __name__ == '__main__':
    main() # スクリプト実行時もmainを呼ぶ形にする