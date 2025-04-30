import gradio as gr
import torch
import subprocess
import os
from transformers import VitsModel, AutoTokenizer
from tts_arabic import tts as arabic_tts
from pydub import AudioSegment

# Load HuggingFace model (only once)
vits_model = VitsModel.from_pretrained("SeyedAli/Arabic-Speech-synthesis")
vits_tokenizer = AutoTokenizer.from_pretrained("SeyedAli/Arabic-Speech-synthesis")

# HuggingFace TTS
def tts_huggingface(text):
    inputs = vits_tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        output = vits_model(**inputs).waveform

    # Convert tensor to numpy and scale to 16-bit PCM
    audio_np = output.squeeze().cpu().numpy()
    audio_int16 = (audio_np * 32767).astype("int16")

    path = "huggingface_output.wav"
    AudioSegment(
        audio_int16.tobytes(),
        frame_rate=vits_model.config.sampling_rate,
        sample_width=2,  # 16-bit = 2 bytes
        channels=1
    ).export(path, format="wav")

    return path

# tts_arabic library

def tts_arabic_custom(text, speaker, pace, denoise, volume, pitch_mul, pitch_add, model_id, vocoder_id, bits):
    wave = arabic_tts(
        text=text,
        speaker=speaker,
        pace=pace,
        denoise=denoise,
        volume=volume,
        pitch_mul=pitch_mul,
        pitch_add=pitch_add,
        model_id=model_id,
        vocoder_id=vocoder_id,
        play=False,
        save_to="arabic_tts_output.wav",
        bits_per_sample=bits
    )
    return "arabic_tts_output.wav"


# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## Offline Arabic TTS Demo")

    with gr.Row():
        with gr.Column(scale=2):
            engine = gr.Radio(label="Choose TTS Engine", choices=["TTS Arabic", "HuggingFace VITS"], value="TTS Arabic", interactive=True)
            input_text = gr.Textbox(label="Text to Synthesize", lines=3)

            with gr.Column(visible=True) as tts_arabic_settings:
                speaker = gr.Slider(0, 3, step=1, value=1, label="Speaker ID")
                pace = gr.Slider(0.5, 2.0, step=0.1, value=1.0, label="Pace")
                denoise = gr.Slider(0.0, 1.0, step=0.005, value=0.005, label="Denoise Strength")
                volume = gr.Slider(0.1, 1.0, step=0.1, value=0.9, label="Volume")
                pitch_mul = gr.Slider(0.5, 2.0, step=0.1, value=1.0, label="Pitch Multiplier")
                pitch_add = gr.Slider(-10, 10, step=1, value=0, label="Pitch Offset")
                model_id = gr.Dropdown(["fastpitch"], value="fastpitch", label="Model ID")
                vocoder_id = gr.Dropdown(["hifigan"], value="hifigan", label="Vocoder ID")
                bits = gr.Radio([8, 16, 32], value=32, label="Bits Per Sample")

            with gr.Column(visible=False) as f5_settings:
                ref_text = gr.Textbox(label="Reference Text", lines=2)
                ref_audio = gr.Audio(label="Reference Audio", type="filepath")

            generate_btn = gr.Button("Generate Audio")

        with gr.Column(scale=1):
            output_audio = gr.Audio(label="Synthesized Audio", type="filepath")

    def toggle_settings(engine):
        return {
            tts_arabic_settings: gr.update(visible=(engine == "TTS Arabic")),
            f5_settings: gr.update(visible=(engine == "F5-TTS"))
        }

    def generate(engine, input_text, ref_audio, ref_text, speaker, pace, denoise, volume, pitch_mul, pitch_add, model_id, vocoder_id, bits):
        if engine == "TTS Arabic":
            return tts_arabic_custom(input_text, speaker, pace, denoise, volume, pitch_mul, pitch_add, model_id, vocoder_id, bits)
        elif engine == "HuggingFace VITS":
            return tts_huggingface(input_text)

    engine.change(fn=toggle_settings, inputs=engine, outputs=[tts_arabic_settings, f5_settings])

    generate_btn.click(
        generate,
        inputs=[engine, input_text, ref_audio, ref_text, speaker, pace, denoise, volume, pitch_mul, pitch_add, model_id, vocoder_id, bits],
        outputs=[output_audio]
    )

demo.launch()
