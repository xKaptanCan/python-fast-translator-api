import requests

class TranslationClient:
    def __init__(self, api_key):
        """
        Client for the Ultimate Translation API.
        Get your API Key here: https://rapidapi.com/kaptancan0707/api/translation-api18
        """
        self.api_key = api_key
        # Host address from the screenshot
        self.host = "translation-api18.p.rapidapi.com"
        self.base_url = f"https://{self.host}"
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.host,
            "Content-Type": "application/json"
        }

    def translate(self, text, target_lang, source_lang="auto"):
        """
        Translates text to the specified language.
        Endpoint: /translateText (POST)
        
        Args:
            text (str): The text to translate.
            target_lang (str): The target language code (e.g., 'tr', 'en', 'de').
            source_lang (str): The source language code (default: 'auto').
            
        Returns:
            dict: The JSON response containing the translation.
        """
        url = f"{self.base_url}/translateText"
        
        payload = {
            "text": text,
            "source": source_lang,
            "target": target_lang
        }
        
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": True, "message": str(e)}

    def get_supported_languages(self):
        """
        Retrieves the list of supported languages.
        Endpoint: /getLanguages (GET)
        """
        url = f"{self.base_url}/getLanguages"
        
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": True, "message": str(e)}