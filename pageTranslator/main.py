import openai
from decouple import config
import requests
from bs4 import BeautifulSoup as bs
from mediawiki import MediaWiki
openai.api_key = config("KEY")

wiki = MediaWiki()


# domain = input("Please enter the domain name to get a Twitter post!\n")

def aiText(prompt):
    if len(prompt) == 0:
        return "This site does not have any usable p tags!"
    aiPrompt = f"Create a Twitter post from this text: {str(prompt)}"
    # print(aiPrompt)
    response = openai.Completion.create(model="text-davinci-003", prompt=aiPrompt, temperature=0, max_tokens=3000)
    text = response["choices"][0]["text"]
    print(text)
    return text


def aiSum(prompt):
    if len(prompt) == 0:
        return "This site does not have any usable p tags!"
    aiPrompt = f"Summarize this text: {str(prompt)}"
    # print(aiPrompt)
    response = openai.Completion.create(model="text-davinci-003", prompt=aiPrompt, temperature=0, max_tokens=1000)
    text = response["choices"][0]["text"]
    print(text)
    return text


def scrape(domain):
    r = requests.get(f'https://{domain}')

    soup = bs(r.content, features="lxml")

    p_tagList = []
    for p_tag in soup.find_all('p'):
        if "©" not in p_tag.text:
            p_tagList.append(p_tag.text)

    return aiText(p_tagList)


def scrapeSum(domain):
    r = requests.get(f'https://{domain}')

    soup = bs(r.content, features="lxml")

    p_tagList = []
    for p_tag in soup.find_all('p'):
        if "©" not in p_tag.text:
            p_tagList.append(p_tag.text)

    return aiSum(p_tagList)

def wikipedia(query):
    p = wiki.page(query).summarize(2)
    return p