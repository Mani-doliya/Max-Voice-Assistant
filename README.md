# Max Voice Assistant

**Max** is a Python-based desktop voice assistant that can listen to your commands, open websites, play songs from your library, and search Google for information. It uses speech recognition and text-to-speech features to provide a conversational experience.

---

## Features

* **Wake Word Activation**: Activate Max by saying `Hello Max`.
* **Web Browsing**: Open popular websites like YouTube, Google, Wikipedia, Facebook, Instagram, Twitter, LinkedIn, Reddit, TikTok, Pinterest, Quora, and Snapchat.
* **Music Playback**: Play songs from a predefined music library (YouTube links).
* **AI-like Responses**: Perform Google searches and provide results based on voice input.
* **Sleep Mode**: Deactivate Max with the wake word to save resources.

---

## Requirements

* Python 3.8+
* Windows OS (requires SAPI for text-to-speech)
* Microphone
* Required Python libraries:

  * `speechrecognition`
  * `pywin32`
  * `webbrowser` (built-in)

Install dependencies with:

```bash
pip install SpeechRecognition pywin32
```

---

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/Mani-doliya/Max-Voice-Assistant.git
```

2. **Music Library**
   Create a Python file `musicLibrary.py` with a dictionary of songs and their YouTube links:

```python
music_library = {
    "song name 1": "https://youtube.com/link1",
    "song name 2": "https://youtube.com/link2",
}
```

3. **Run the assistant**

```bash
python maxg.py
```

4. Max will initialize and wait for the wake word. Say:

```
Hello Max
```

to activate it.

---

## Usage

* **Open Websites**
  Say: `Open YouTube` or `Open Google`

* **Play Songs**
  Say: `Play <song name>`

* **Search Google / AI-like Chat**
  Say: `Max ji, <your question>` or `Chat <your question>`

* **Deactivate Max**
  Say the wake word again: `Hello Max`

---

## File Structure

```

├─ maxg.py      # Main voice assistant script
├─ musicLibrary.py       # Music library dictionary
├─ README.md             # Project documentation
└─ License               # License
 
```

---

## Notes

* Works best with a stable internet connection for Google search and YouTube playback.
* Currently supports **English (India)** accent for speech recognition.
* Make sure your microphone is properly configured and not muted.

---

## Author

**Manish Doliya**

* GitHub: [Manish Doliya](https://github.com/Mani-doliya)

---
 
## License

This project is licensed under the MIT License.

---

