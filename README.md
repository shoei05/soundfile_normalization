[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1S9gfGZZ2NleEv6QgH51dxu2s95sOfgQ2?usp=sharing)

[解説記事](https://plaza.umin.ac.jp/shoei05/index.php/2024/05/26/2546/) / [GPTs](https://chatgpt.com/g/g-blH6IXYg6-soundfile-normalization )

# soundfile_normalization
音声ファイルの前処理: ノイズ除去と音量正規化を自動化するPythonコード

## 音声ファイルの前処理: ノイズ除去と音量正規化

このPythonコードは、音声ファイルからノイズを除去し、音量を正規化するためのツールです。音声認識やその他の音声処理タスクの精度を向上させるために、前処理として使用できます。

### 機能

* **ノイズ除去:** FFmpegの`afftdn`フィルターを使用して、音声ファイルからノイズを自動的に除去します。
* **音量正規化:** FFmpegの`loudnorm`フィルターを使用して、音声ファイルの音量を自動的に正規化します。
* **バッチ処理:** フォルダ内の複数の音声ファイルを一度に処理できます。
* **様々な入力形式のサポート:** WAV, MP3, MP4, M4A, MKV, WEBM などの一般的な音声および動画形式に対応しています。
* **Google Colab対応:** Google Colab環境で簡単に実行できます。

### ディレクトリ構造

```
soundfile_normalization/
├── soundfile_normalization.py   # メインのPythonスクリプト
├── input/                      # 処理したい音声データを格納するフォルダ
│   └── (音声データを入れる) 
├── output/                     # 処理後の音声データが格納されるフォルダ (自動生成)
│   └── (処理後の音声データ)
├── done_original/               # 処理が完了した元の音声データが格納されるフォルダ (自動生成)
│   └── (処理後の元データ)
├── README.md                   # このファイル
└── requirements.txt             # 必要なパッケージリスト
```

### 使用方法

#### Google Colab

- [Open with Colab](https://colab.research.google.com/drive/1S9gfGZZ2NleEv6QgH51dxu2s95sOfgQ2?usp=sharing)

1. 上記のGoogle Colabノートブックへのリンクをクリックします。
2. コードを自分のGoogle Driveにコピーします。
3. ノートブックの指示に従って、必要なライブラリをインストールし、音声ファイルをアップロードします。
4. コードを実行すると、処理された音声ファイルが自動的にダウンロードされます。

#### ローカル環境

1. **FFmpeg をインストールします。** 
   - インストール方法については、[公式ドキュメント](https://ffmpeg.org/download.html) を参照してください。
   - インストール後、FFmpeg がシステムの PATH 環境変数に含まれていることを確認してください。
2. **リポジトリのクローン** 
   ```bash
   git clone https://github.com/shoei05/soundfile_normalization.git
   ```
3. **クローンしたリポジトリのディレクトリに移動します。**
   ```bash
   cd soundfile_normalization
   ```
4. **仮想環境の作成 (推奨):**  クローンしたリポジトリのディレクトリに移動し、仮想環境を作成します (Python のバージョンやライブラリの依存関係を分離するために推奨されます)。

   ```bash
   cd replace_text
   python -m venv env_soundfile_normalization
   ```
5. **仮想環境の有効化:**

   * **Windows:**
     ```bash
     env_soundfile_normalization \Scripts\activate
     ```
   * **macOS/Linux:**
     ```bash
     source env_soundfile_normalization/bin/activate
     ```
6. **必要なライブラリをインストールします:** 
   ```bash
   pip install -r requirements.txt
   ```
7. **処理したい音声ファイルを `input` フォルダに配置します。**
8. **ターミナルで `python soundfile_normalization.py` コマンドを実行します。**
9. **処理された音声ファイルは `output` フォルダに保存されます。**

### パラメータ

* `noise_reduction_db`: ノイズ除去の強度をデシベル単位で指定します。デフォルトは10です。
* `max_workers`: 並列処理に使用するワーカー数を指定します。デフォルトは4です。

### 注意

* 適切なノイズ除去の強度は、音声データのノイズレベルや種類によって異なります。
* FFmpeg のインストールと設定については、公式ドキュメントを参照してください。

### ライセンス
このスクリプトは MIT ライセンスで公開されています。
このプロジェクトは、自由に使用、改変、再配布することができます。もし、コードを使用する場合は、元の作者への謝辞を含めていただければ幸いです。 

---
**謝辞:** 

例) このコードは、[shoei05](https://github.com/shoei05) によって作成されました。 

--- 
