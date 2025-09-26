# src/prototypus_ai/cli.py

import fire
import sys
import os

from .core.gemini_client import perform_conversion
# from .project.config import initialize_environment  # 設定があればここからインポート

class PrototypusAI:
    """
    Prototypus AI: The data transformation tool for the 21st century.
    """

    def __init__(self):
        # アプリケーション開始時の初期化処理（例：設定読み込み）
        # initialize_environment()
        pass

    def convert(self, input_path: str, output_format: str, prompt: str = None):
        """
        Converts a file from one format to another using Gemini AI.

        Args:
            input_path: The path to the input file to be converted.
            output_format: The desired output format (e.g., 'html', 'json', 'yaml').
            prompt: Optional. A custom prompt to guide the transformation.
        """
        if not os.path.exists(input_path):
            print(f"Error: The input file '{input_path}' was not found.", file=sys.stderr)
            sys.exit(1)

        print(f"[CLI] Starting conversion of '{input_path}' to '{output_format}'...")

        try:
            # coreモジュールのロジックを呼び出し、処理を委譲
            result = perform_conversion(input_path, output_format, prompt)

            print("\n--- Final Converted Content ---")
            print(result)
            print("-------------------------------")

        except Exception as e:
            print(f"An unexpected error occurred during conversion: {e}", file=sys.stderr)
            sys.exit(1)

    def hello(self):
        """A simple greeting."""
        print("Hello, world! (from cli.py)")

    def byebye(self, message: str):
        """
        A simple goodbye command.
        Args:
            message: The message to be displayed.
        """
        print(f"Welcome to Prototypus baibai! Here is your message: {message}")
        sys.exit(0)

def main():
    """
    Main entry point for the Prototypus AI CLI.
    """
    # ptai convert --input-path test_input.txt --output-format json --prompt "Summarize and convert this."

    # PrototypusAIクラスをコマンドラインインターフェースとして公開
    fire.Fire(PrototypusAI)

if __name__ == '__main__':
    # スクリプトが直接実行された場合に main を実行
    main()