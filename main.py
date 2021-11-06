import requests
import json
import time


def get_phrases_from_input_file(txt_file):
    input_file_phrases = []
    with open(txt_file) as opened_file:
        for file_line in opened_file:
            input_file_phrases.append(file_line)
            print(file_line)
        opened_file.close()
        return input_file_phrases


def translator(input_phrases, source_language, trans_language, api_key, api_host):
    translated_phrases = []
    url = "https://google-translate20.p.rapidapi.com/translate"
    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': api_host
    }
    for phrase in input_phrases:
        querystring = {'text': phrase, 'tl': trans_language, 'sl': source_language}
        response = requests.request("GET", url, headers=headers, params=querystring)
        translation_dict = json.loads(response.text)
        translated_text = translation_dict['data']['translation']
        translated_phrases.append(translated_text)
        time.sleep(1)

    print(translated_phrases)
    return translated_phrases


def write_to_text_file(translated_phrases, text_file):
    opened_file = open(text_file, "w")
    for phrase in translated_phrases:
        opened_file.write(phrase + "\n")
    opened_file.close()


api_key = input('Enter API Key ')
api_host = input('Enter API Host ')
input_txt_file = r"input/phrases.txt"
output_txt_file = r"output/translatedphrases.txt"
input_file_language = input("insert language input file was written in, ex. 'en' for English, 'es' for Spanish, 'fr' for French, 'it' for Italian ")
new_language = input("insert NEW language, ex. 'en' for English, 'es' for Spanish, 'fr' for French, 'it' for Italian ")
input_file_phrases = get_phrases_from_input_file(input_txt_file)
translated_phases = translator(input_file_phrases, input_file_language, new_language, api_key, api_host)
write_to_text_file(translated_phases, output_txt_file)
