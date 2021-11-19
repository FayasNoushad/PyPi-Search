import requests
from requests.utils import requote_uri


API = "https://api.abirhasan.wtf/pypi?query="


def pypi(query):
    r = requests.get(API + requote_uri(query))
    info = r.json()
    return info


def search(query):
    info = pypi(query)
    text = "Information\n"
    text += f"\nPackage Name: {info['PackageName']}"
    text += f"\nTitle: {info['Title']}"
    text += f"\nAbout: {info['About']}"
    text += f"\nLatest Release Date: {info['LatestReleaseDate']}"
    text += f"\nPip Command: {info['PipCommand']}"
    return text


def main():
    query = input("Enter package name for search\n:- ")
    print(search(query))


main()
