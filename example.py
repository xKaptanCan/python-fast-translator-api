from translator import TranslationClient

# ==========================================
# PASTE YOUR API KEY BELOW
# GET FREE KEY: https://rapidapi.com/kaptancan0707/api/translation-api18
# ==========================================
API_KEY = "PASTE_YOUR_RAPIDAPI_KEY_HERE"

def main():
    if API_KEY == "PASTE_YOUR_RAPIDAPI_KEY_HERE":
        print("ERROR: Please open example.py and insert your API Key!")
        return

    # Initialize the client
    client = TranslationClient(API_KEY)

    print("--- 1. Translation Test (English -> Turkish) ---")
    text = "Hello, this is a powerful translation API."
    result = client.translate(text, target_lang="tr", source_lang="en")
    
    if result and "data" in result:
        print(f"Original: {text}")
        print(f"Translated: {result['data']['translatedText']}")
    else:
        print("Error:", result)

    print("\n--- 2. Auto-Detection Test (German -> English) ---")
    german_text = "Guten Morgen, wie geht es dir?"
    result_auto = client.translate(german_text, target_lang="en", source_lang="auto")

    if result_auto and "data" in result_auto:
        print(f"Original: {german_text}")
        print(f"Detected Language: {result_auto['data']['detectedLanguage']}")
        print(f"Translated: {result_auto['data']['translatedText']}")
    else:
        print("Error:", result_auto)

if __name__ == "__main__":
    main()