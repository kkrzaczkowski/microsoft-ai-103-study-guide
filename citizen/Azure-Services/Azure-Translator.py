# SLIDE 68
# ============================================================
# TRANSLATE TEXT
# Translates text into one or more target languages and returns the detected source language.
# ============================================================

The Azure Translator global endpoint: api.cognitive.microsofttranslator.com
Azure Translator regional endpoints: These endpoints include api-nam.cognitive.microsofttranslator.com, api-apc.cognitive.microsofttranslator.com, and api-eur.cognitive.microsofttranslator.com
Foundry resource endpoints: {foundry-resource-name}.cognitiveservices.azure.com/


key_credential = AzureKeyCredential("FOUNDRY_KEY")

# Connect to a Foundry resource endpoint
client = TextTranslationClient(credential=key_credential, endpoint="FOUNDRY_ENDPOINT")

# Or connect using a region
client = TextTranslationClient(credential=key_credential, region="FOUNDRY_REGION")

# Text to translate
input_text_elements = [
    InputTextItem(text="Hola"),
    InputTextItem(text="こんにちは")
]

# Translate text
translation_results = client.translate(
    body=input_text_elements,
    to_language=["fr", "en"]
)

# Display translation results
idx = 0

for translation in translation_results:

    input_text = input_text_elements[idx].text
    idx += 1

    source_language = translation.detected_language

    for translated_text in translation.translations:

        print(
            f"'{input_text}' was translated "
            f"from {source_language.language} "
            f"to {translated_text.to} as "
            f"'{translated_text.text}'."
        )

# Example Output:
# 'Hola' was translated from es to fr as 'Bonjour'.
# 'Hola' was translated from es to en as 'Hello'.
#
# 'こんにちは' was translated from ja to fr as 'Bonjour'.
# 'こんにちは' was translated from ja to en as 'Hello'.



# SLIDE 68
# ============================================================
# AZURE AI TRANSLATOR - TRANSLITERATION
# Converts text from one writing system (script) to another while preserving pronunciation.
# ============================================================

# Text to transliterate
input_text_elements = [
    InputTextItem(text="こんにちは")
]

# Transliterate Japanese characters to Latin characters
transliteration_results = client.transliterate(
    body=input_text_elements,
    language="ja",
    from_script="Jpan",
    to_script="Latn"
)

# Display results
for transliteration in transliteration_results:

    source_script = transliteration.script
    transliterated_text = transliteration.text

    print(
        f"'こんにちは' was transliterated from {source_script} to '{transliterated_text}'."
    )

# Example Output:
# 'こんにちは' was transliterated from Jpan to 'konnichiwa'.