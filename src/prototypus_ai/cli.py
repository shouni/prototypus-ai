import fire
import sys
import os

# サンプルとして、ダミーの変換関数をインポート
# 実際には、core.py や converters/ にあるロジックをインポートします
# from .core import process_conversion

class PrototypusAI:
    """
    Prototypus AI: The data transformation tool for the 21st century.
    """

    def convert(self, input_path: str, output_format: str, prompt: str = None):
        """
        Converts a file from one format to another using Gemini AI.

        Args:
            input_path: The path to the input file to be converted.
            output_format: The desired output format (e.g., 'html', 'json', 'yaml').
            prompt: Optional. A custom prompt to guide the transformation.
        """
        # ファイルの存在チェック
        if not os.path.exists(input_path):
            print(f"Error: The input file '{input_path}' was not found.", file=sys.stderr)
            sys.exit(1)

        # 変換ロジックを呼び出す
        print(f"Starting conversion of '{input_path}' to '{output_format}'...")
        print(f"Using prompt: '{prompt}'" if prompt else "Using default conversion rules.")

        # ダミーの変換処理
        # ここに実際の Gemini API 呼び出しと変換ロジックを実装します
        try:
            # result = process_conversion(input_path, output_format, prompt)
            result = f"Converted content for {input_path} to {output_format}."
            print("\n--- Converted Content ---")
            print(result)
            print("-------------------------")
        except Exception as e:
            print(f"An error occurred during conversion: {e}", file=sys.stderr)
            sys.exit(1)

def main():
    """
    Main entry point for the Prototypus AI CLI.
    """
    fire.Fire(PrototypusAI)

if __name__ == '__main__':
    main()