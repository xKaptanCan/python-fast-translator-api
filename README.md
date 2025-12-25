# 🚀 Python Fast Translation API (Google Translate Alternative)

A simple, fast, and reliable Python wrapper for the **Ultimate Translation API**.  
Translate text between **120+ languages** with automatic language detection.

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Get%20Free%20Key-blue)](https://rapidapi.com/kaptancan0707/api/translation-api18)
[![Python](https://img.shields.io/badge/Python-3.x-yellow.svg)](https://www.python.org/)

## 🔥 Features
* **120+ Languages Supported**: From English to Turkish, Spanish to Chinese.
* **Auto Detection**: Automatically detects the source language.
* **High Speed**: Average response time < 200ms.
* **Easy Integration**: Simple Python class ready to use.

## 🛠 Installation

1.  Clone this repository:
    ```bash
    git clone [https://github.com/xKaptanCan/python-fast-translator-api.git](https://github.com/xKaptanCan/python-fast-translator-api.git)
    ```
2.  Install requirements:
    ```bash
    pip install -r requirements.txt
    ```

## 🔑 Get Your API Key
You need an API key to use this library. You can get a **FREE** key from RapidAPI:
👉 **[Click here to get your API Key](https://rapidapi.com/kaptancan0707/api/translation-api18)**

## 💻 Usage Example

```python
from translator import TranslationClient

# Replace with your actual API key from RapidAPI
api_key = "YOUR_RAPIDAPI_KEY"
client = TranslationClient(api_key)

# Translate text
response = client.translate("Hello world", target_lang="tr")

print(response['data']['translatedText']) 
# Output: "Merhaba dünya"
