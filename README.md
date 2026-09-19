<div align="center">

# Smart Summarization App
# 📝🤖

### A Persian Text Summarizer Built with Streamlit and Transformers

A small web app that takes a long Persian text, runs a Hugging Face summarization model, and shows a shorter version in the same page.

<br>

# 👨‍💻 **Sadra Hatami**

### *Developer • Software Engineer • Creator*

<br>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Transformers](https://img.shields.io/badge/Hugging%20Face-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Model](https://img.shields.io/badge/Model-T5%20ParsBERT-8E44AD?style=for-the-badge)
![Language](https://img.shields.io/badge/Language-Persian-success?style=for-the-badge)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
![GitHub](https://img.shields.io/badge/Open_Source-Project-black?style=for-the-badge&logo=github)

<br>

[🌐 GitHub Profile](https://github.com/sadra-hatami)
•
[📧 Contact](mailto:sadra.hatami.1732@gmail.com)

</div>

---

# 📑 Table of Contents

- [About](#-about)
- [Why This App?](#-why-this-app)
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Technologies](#️-technologies)
- [Usage](#️-usage)
- [Target Audience](#-target-audience)
- [Roadmap](#-roadmap)
- [FAQ](#-frequently-asked-questions)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [License](#-license)
- [Copyright](#-copyright)
- [Support](#-support)

---

# 📖 About

**Smart Summarization App** is a Persian text-summarization tool written in Python.

The interface is a Streamlit page. The user pastes a long text, presses one button, and the app runs the Hugging Face model `m3hrdadfi/t5-base-parsbert-summarization`. The shorter text is shown on the same page.

The model is loaded once with `@st.cache_resource`, so later clicks in the same session do not download it again.

> **Tagline:** *A Streamlit app that summarizes Persian text with a T5 / ParsBERT Hugging Face model.*

---

# 🚀 Why This App?

A summarizer does not need a large custom backend to be useful.

This project keeps the path short:

- One file
- A Persian-ready model
- A browser UI from Streamlit
- Cached model loading
- Clear error and empty-input messages

It is a compact NLP app, not a full writing suite.

---

# ✨ Key Features

- 🇮🇷 Built for Persian text
- 📝 One text box and one action button
- 🤗 Hugging Face `summarization` pipeline
- 📦 Model: `m3hrdadfi/t5-base-parsbert-summarization`
- ⚡ Cached model load with Streamlit
- ⏳ Spinner while the text is processed
- ⚠️ Warning if the box is empty
- 🌐 Runs locally in the browser

---

# ⚙️ How It Works

1. Streamlit opens a page titled **خلاصه‌ساز هوشمند فارسی**.
2. The first request loads the T5 / ParsBERT summarization pipeline.
3. The pipeline is stored in Streamlit resource cache.
4. The user pastes Persian text and clicks **خلاصه‌سازی کن**.
5. The model runs with `max_length=150`, `min_length=40`, and `do_sample=False`.
6. The app shows `result[0]['summary_text']`.

Empty input is blocked. Other errors are printed in the page.

---

# 📁 Project Structure

```text
Smart-Summarization-App/
└── app.py
```

`app.py` contains the page config, model loader, text area, button, and result panel.

---

# 🛠️ Technologies

- Python 3.8+
- Streamlit
- Hugging Face Transformers
- T5 / ParsBERT summarization model

---

# ▶️ Usage

### Install

```bash
git clone https://github.com/sadra-hatami/Smart-Summarization-App.git
cd Smart-Summarization-App
pip install streamlit transformers torch
```

If `torch` install fails on your system, follow the official PyTorch command for your OS.

### Run

```bash
streamlit run app.py
```

The first run may take a while because the model is downloaded. Later runs in the same environment are faster.

---

# 🎓 Target Audience

- Persian writers who want a short draft summary
- Developers trying Streamlit with Transformers
- Students learning Hugging Face pipelines

---

# 🚀 Roadmap

Possible later improvements:

- 📄 Upload a `.txt` file
- 🎚️ Controls for `min_length` and `max_length`
- 📋 Copy-summary button
- 💾 Keep recent summaries in the session
- 🌙 Better page layout and font for long Persian text

---

# ❓ Frequently Asked Questions

### Does the app work offline after the first run?

The model files stay in the local Hugging Face cache after the first download. You still need a machine that can run PyTorch.

### Why is the first click slow?

The model is downloaded and loaded into memory once. Streamlit then reuses that loaded pipeline.

### Can I summarize English with this page?

The selected model is trained for Persian. English may work poorly.

### What if I see a memory or install error?

The model needs a working `transformers` + `torch` install and enough RAM. A small CPU machine can be slow.

---

# 🤝 Contributing

Contributions are welcome.

You can:

- Report bugs
- Improve the Persian UI
- Add length controls
- Submit Pull Requests

---

# 📬 Contact

**Developer:**

### **Sadra Hatami**

📧 [Email](mailto:sadra.hatami.1732@gmail.com)

🌐 [GitHub](https://github.com/sadra-hatami)

---

# 📄 License

This project is licensed under the **MIT License**.

The summarization model is third-party Hugging Face content and keeps its original license.

---

# © Copyright

© 2026 **Sadra Hatami**

All rights reserved.

The source code, page design, documentation, and project structure are protected under applicable copyright laws.

---

# ⭐ Support the Project

If this summarizer helped you, please consider:

⭐ Starring this repository

🐛 Reporting issues

💡 Suggesting improvements

---

<div align="center">

## Designed & developed with ❤️ for the developer community of Iran and the world

<br>

</div>
