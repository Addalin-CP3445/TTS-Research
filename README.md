
# 🔍 TTS & STT Research Summary

This repository documents my initial research and experimentation with Text-to-Speech (TTS) and Speech-to-Text (STT) tools. Below is an overview of the platforms explored and key observations from the process.

---

## 🗣️ TTS Tools Explored

- [**Coqui-TTS**](https://github.com/coqui-ai/TTS): An on-premise, open-source framework. However, some models like XTTS are licensed under CPML and not entirely open for commercial use.  
- [**AiVOOV**](https://aivoov.com/): API-based service; no on-premise deployment available.  
- [**ElevenLabs**](https://elevenlabs.io/docs/quickstart): API-based; not available for on-premise use.  

---

## 🧾 STT Tools Explored

- [**OpenAI Whisper**](https://github.com/openai/whisper): On-premise, MIT-licensed, and highly effective for multilingual transcription.  
- [**Voice AI**](https://www.neuralspace.ai/voiceai): API-only service; not available for local deployment.  
  > ⚠️ **Note**: Voice AI by Neuralspace is in the process of shutting down.  
- [**ElevenLabs**](https://elevenlabs.io/docs/quickstart): Also API-based and not deployable on-premise.  

---

## 📚 Open-Source Research

- [**ESPnet**](https://github.com/espnet/espnet): A powerful open-source toolkit for end-to-end speech processing, including TTS. It supports multiple architectures (Tacotron2, Transformer-TTS, FastSpeech, FastSpeech2, VITS) and vocoders (Parallel WaveGAN, WaveGlow, HiFi-GAN).  
  > ⚠️ Note: ESPnet runs natively on Linux. I attempted using WSL on Windows, but faced library compatibility issues. These problems did not appear when running ESPnet in Google Colab.  

- [**Tortoise-TTS**](https://github.com/neonbjb/tortoise-tts): Unlike ESPnet, it lacks a standardized training pipeline.  
  I used the [**AI Voice Clone GitHub repository**](https://github.com/JarodMica/ai-voice-cloning), which provides a UI-based workflow for dataset preprocessing, training, and inference. The preprocessing step conveniently uses Whisper to generate transcripts from audio.  
  > ⚠️ Limitation: The tool does not support generating transcripts in Buckwalter format, which I was exploring due to the tokenization challenges outlined below.  

---

## 📝 Notes: Challenges in Fine-Tuning Arabic TTS

While working with Arabic datasets to tokenize, I encountered two major challenges:

- **Missing Diacritics**: Arabic is typically written without short vowel markers (tashkeel), leading to pronunciation ambiguity. For example, “كتب” can mean *kataba* (he wrote) or *kutiba* (it was written), making accurate tokenization and alignment difficult.  

- **Complex Morphology**: Arabic has a root-pattern system where one root (e.g., ك-ت-ب) can produce many forms like “كتاب” (book), “كاتب” (writer), and “مكتبة” (library). This morphological diversity made it harder for models to generalize across different word forms.
