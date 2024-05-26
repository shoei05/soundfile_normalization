[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1S9gfGZZ2NleEv6QgH51dxu2s95sOfgQ2?usp=sharing)

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

### 使用方法

#### Google Colab

- [Open with Colab](https://colab.research.google.com/drive/1S9gfGZZ2NleEv6QgH51dxu2s95sOfgQ2?usp=sharing)

1. 上記のGoogle Colabノートブックへのリンクをクリックします。
2. コードを自分のGoogle Driveにコピーします。
3. ノートブックの指示に従って、必要なライブラリをインストールし、音声ファイルをアップロードします。
4. コードを実行すると、処理された音声ファイルが自動的にダウンロードされます。

#### ローカル環境

1. Python 3 をインストールします。
2. 必要なライブラリをインストールします: `pip install pydub tqdm`
3. FFmpeg をインストールし、PATH 環境変数に追加します。
4. このリポジトリから `soundfile_normalization.py` ファイルをダウンロードします。
5. 処理したい音声ファイルを `input` フォルダに配置します。
6. ターミナルで `python sound_normalization.py` コマンドを実行します。
7. 処理された音声ファイルは `output` フォルダに保存されます。

### パラメータ

* `noise_reduction_db`: ノイズ除去の強度をデシベル単位で指定します。デフォルトは10です。
* `max_workers`: 並列処理に使用するワーカー数を指定します。デフォルトは4です。

### 注意

* 適切なノイズ除去の強度は、音声データのノイズレベルや種類によって異なります。
* FFmpeg のインストールと設定については、公式ドキュメントを参照してください。

### ライセンス

このプロジェクトは、自由に使用、改変、再配布することができます。コードを使用する場合は、元の作者への謝辞を含めていただければ幸いです。 

---
**謝辞:** 

例) このコードは、[shoei05](https://github.com/shoei05) によって作成されました。 

--- 
