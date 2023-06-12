import wave
import pyroomacoustics as pa
import numpy as np


# CMU ARCTIC Corpusをカレントディレクトリにダウンロード
pa.datasets.CMUArcticCorpus(basedir="./CMU_ARCTIC", download=True, speaker=["aew", "axb"])

# 読み込むサンプルファイル
sample_wave_file = "./CMU_ARCTIC/cmu_us_aew_arctic/wav/arctic_a0001.wav"

# ファイルを読み込む
wav = wave.open(sample_wave_file)

# ファイルの情報を出力する
print("サンプリング周波数[Hz]: ", wav.getframerate())
print("サンプルサイズ[Byte]: ", wav.getsampwidth())
print("サンプル数: ", wav.getnframes())
print("チャンネル数: ", wav.getnchannels())

# PCM形式の波形データを読み込み
data = wav.readframes(wav.getnframes())

# dataを2バイトの数値列に変換
data = np.frombuffer(data, dtype=np.int16)

# waveファイルを閉じる
wav.close()
