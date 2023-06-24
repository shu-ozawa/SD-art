 #pipダウンロード pip3 install google-cloud-translate

#from google.cloud import translate

text = 'Dogs in Space'

def pass_unchanged(text):
    text = '(' + text + ')'
    return text

#print(pass_unchanged(text))

'''
def translate_text(text="Hello, world!", project_id="art-stable-diffusion"):

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": "es",
        }
    )

    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))

translate_text()

'''



