import os
from pydub import AudioSegment
from pydub.effects import normalize
from tqdm import tqdm
import logging
from concurrent.futures import ThreadPoolExecutor
import shutil
import tempfile
import uuid

# ログの設定
logging.basicConfig(filename='preprocessing.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def replace_spaces(filename):
    return filename.replace(" ", "_")

def preprocess_audio(input_path, output_path, noise_reduction_db, done_folder):
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")

        temp_dir = tempfile.gettempdir()
        temp_id = str(uuid.uuid4())
        temp_wav = os.path.join(temp_dir, f"temp_{temp_id}.wav")
        temp_denoised = os.path.join(temp_dir, f"temp_denoised_{temp_id}.wav")

        _, extension = os.path.splitext(input_path)
        extension = extension.lower()

        # オーディオファイルを読み込んで一時的にwav形式で保存
        audio = AudioSegment.from_file(input_path, format=extension.lstrip('.'))
        audio.export(temp_wav, format="wav")

        # ノイズ除去
        denoise_command = f"ffmpeg -i {temp_wav} -af 'afftdn=nr={noise_reduction_db}' {temp_denoised} -y"
        if os.system(denoise_command) != 0:
            raise RuntimeError(f"Error executing ffmpeg command: {denoise_command}")

        # ノイズ除去後の音声を読み込み
        audio = AudioSegment.from_wav(temp_denoised)

        # サンプリングレートの変換
        audio = audio.set_frame_rate(16000)

        # 音声の正規化
        normalized_audio = normalize(audio)

        # 正規化された音声を読み込んでmp3形式で保存
        normalized_audio.export(output_path, format="mp3")

        # 処理したファイルをdoneフォルダに移動
        shutil.move(input_path, os.path.join(done_folder, replace_spaces(os.path.basename(input_path))))

        logging.info(f"Preprocessed {input_path}")

    except Exception as e:
        logging.error(f"Error processing {input_path}: {str(e)}")
        raise

    finally:
        # 一時ファイルを削除
        for temp_file in [temp_wav, temp_denoised]:
            if os.path.exists(temp_file):
                os.remove(temp_file)

def process_files(input_folder, output_folder, noise_reduction_db, max_workers, done_folder):
    audio_files = [f for f in os.listdir(input_folder) if f.lower().endswith((".wav", ".mp3", ".mp4", ".m4a", ".mkv", ".webm"))]
    total_files = len(audio_files)

    progress_bar = tqdm(total=total_files, unit='file')

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for filename in audio_files:
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(replace_spaces(filename))[0]}.mp3")
            futures.append(executor.submit(preprocess_audio, input_path, output_path, noise_reduction_db, done_folder))

        for future in futures:
            try:
                future.result()
                progress_bar.update()
            except Exception as e:
                logging.error(f"Error in parallel processing: {str(e)}")

    progress_bar.close()

if __name__ == "__main__":
    input_folder = './p_input'
    output_folder = './input'
    done_folder = './p_done'
    noise_reduction_db = 10
    max_workers = 4

    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(done_folder, exist_ok=True)

    process_files(input_folder, output_folder, noise_reduction_db, max_workers, done_folder)
