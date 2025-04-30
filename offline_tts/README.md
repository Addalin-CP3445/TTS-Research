# 🗣️ Offline Arabic TTS Demo (Gradio)

This project is a Gradio-based demo for generating Arabic speech using multiple text-to-speech (TTS) engines:
- `TTS Arabic (nipponjo)`
- `HuggingFace VITS (SeyedAli Arabic Speech Synthesis)`

---

## 🛠️ Installation

### 2. Clone repo and Create a virtual environment (optional but recommended)

```bash
python -m venv tts_env
source tts_env/bin/activate   # On Windows use: tts_env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

```bash
python app.py
```

It will launch a local Gradio interface in your browser.

---

## 🧠 Models & Download Paths

### 🔹 TTS Arabic (nipponjo)

- This model is downloaded into:

```
<your-env-folder>\Lib\site-packages\tts_arabic\data
```

> This includes the FastPitch + HiFiGAN models used for synthesis.

---

### 🔹 HuggingFace VITS (SeyedAli/Arabic-Speech-synthesis)

- Downloaded into your local HuggingFace cache directory:

```
C:\Users\<your-username>\.cache\huggingface\hub\models--SeyedAli--Arabic-Speech-synthesis\snapshots
```

> This is automatically managed by the `transformers` library.

---

## 💬 Notes

- Ensure `ffmpeg` is installed and available in your system path (required by `pydub`).
- Tested with `Python 3.10+` and `torch >= 2.1`.


