# Prototypus AI (Python): The Data Transformation Tool

[![Python Version](https://img.shields.io/badge/Python-3.12+-blue?logo=python)](https://www.python.org/) 
[![CLI Framework](https://img.shields.io/badge/CLI-python--fire-red?logo=pypi)](https://github.com/google/python-fire) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### 🚀 概要 (About)

`Prototypus AI` は、**Python** と **`python-fire`** ライブラリを使用して構築されたコマンドラインツール（CLI）です。主に、**Gemini API** を活用して様々な入力ファイルを読み込み、ユーザーの指定したプロンプトと出力形式に基づいて、AIによるデータ変換や整形を実行するために設計されています。

このプロジェクトは、Pythonにおける**標準的なパッケージ構造（`src/` 構成）とCLI設計パターン**を習得するために作成されました。

### 🛠️ 技術スタック (Tech Stack)

  * **メイン言語:** **Python 3.12+**
  * **CLI フレームワーク:** **`python-fire`** (クラス/メソッドを自動でCLIコマンドに変換)
  * **API クライアント:** **`google-generativeai`** (Gemini API SDK)
  * **設定管理:** **`python-dotenv`** (環境変数の読み込み)

-----

### 📦 インストールとセットアップ (Installation & Setup)

#### 1\. 前提条件

  * Git
  * Python 3.12 以上

#### 2\. 環境変数の設定

Gemini APIを利用するには、APIキーが必要です。プロジェクトルートに **`.env`** ファイルを作成し、キーを設定してください。

```bash
# .env ファイルの内容
GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

#### 3\. 開発環境のセットアップ

プロジェクトルートで以下のコマンドを実行し、仮想環境を作成し、開発モードでインストールします。

```bash
# 仮想環境を作成・有効化
python -m venv .venv
source .venv/bin/activate

# 開発モードでインストール
pip install -e .

# インストールされたコマンドの確認
ptai hello
```

-----

### 🚀 使用方法 (Usage)

インストールが完了すると、`ptai` コマンドでアプリケーションを実行できます。

#### 1\. データ変換 (`convert`)

このコマンドは、指定されたファイルを読み込み、AIに変換を依頼します。

```bash
# 実行例
ptai convert \
    --input-path data/input.csv \
    --output-format yaml \
    --prompt "Identify the top 5 entries and output them as a clean YAML list."
```

#### 2\. コマンドの詳細

| コマンド | 説明 | 引数 |
| :--- | :--- | :--- |
| `ptai convert` | ファイルをAI変換します。 | `--input-path`, `--output-format` (必須), `--prompt` (オプション) |
| `ptai hello` | CLIが動作していることを確認します。 | なし |
| `ptai -- --help` | **`ptai`** コマンド全体のヘルプを表示します。 | なし |

-----

### 📚 学習ポイント (Learning Notes)

このプロジェクトを通じて、以下の主要なPython開発スキルを習得しました。

  * **パッケージの分離**: **`src/`** ディレクトリを使用し、ライブラリコード (`prototypus_ai`) とリポジトリを分離するモダンなパッケージ構造。
  * **エントリポイント**: **`pyproject.toml`** を使用して `ptai` コマンドを **`prototypus_ai.cli:main`** に紐づける方法。
  * **関心の分離 (SoC)**:
      * **`cli.py`**: ユーザー入力の解析とエラーチェックのみを担当。
      * **`core/`**: 外部API呼び出しや複雑なビジネスロジックのみを担当。
      * **`project/`**: 設定値（APIキーなど）の読み込みのみを担当。
  * **CLIライブラリ**: `python-fire` を使用して、Pythonのクラスをわずかなコードで機能的なCLIに変換する効率的な方法。

-----

### 📜 ライセンス (License)

このプロジェクトは **MIT License** の下で公開されています。詳細については [`LICENSE`](https://www.google.com/search?q=LICENSE) ファイルを参照してください。
