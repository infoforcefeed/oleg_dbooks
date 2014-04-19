#!/usr/bin/env python2
from bs4 import BeautifulSoup
import re, random

moons = [
        "Adrastea",
        "Aitne",
        "Amalthea",
        "Ananke",
        "Aoede",
        "Arche",
        "Autonoe",
        "Callirrhoe",
        "Callisto",
        "Carme",
        "Carpo",
        "Chaldene",
        "Cyllene",
        "Elara",
        "Erinome",
        "Euanthe",
        "Eukelade",
        "Euporie",
        "Europa",
        "Eurydome",
        "Ganymede",
        "Harpalyke",
        "Hegemone",
        "Helike",
        "Hermippe",
        "Herse",
        "Himalia",
        "Io",
        "Iocaste",
        "Isonoe",
        "Kale",
        "Kallichore",
        "Kalyke",
        "Kore",
        "Leda",
        "Lysithea",
        "Megaclite",
        "Metis",
        "Mneme",
        "Orthosie",
        "Pasiphae",
        "Pasithee",
        "Praxidike",
        "Sinope",
        "Sponde",
        "Taygete",
        "Thebe",
        "Thelxinoe",
        "Themisto",
        "Thyone"
        ]

def random_moon(matchobj):
    return "#" + random.sample(moons, 1)[0]

def main():
    prepared_html = open("prepared.html")
    soup = BeautifulSoup(prepared_html, "lxml")
    prepared_html.close()

    # Save intermediate step
    output = open("prepared2.html", "w")
    all_ps = soup.find_all("p")
    print "Number of <p> tags found: {}".format(len(all_ps))
    all_lines = [x.get_text().encode("ascii", errors="replace") for x in all_ps]
    print "Number of lines found: {}".format(len(all_lines))
    all_text = "\n".join(all_lines)
    output.write(all_text)
    output.close()

    to_replace = ["postgres", "mongo", "couch", "riak", "basho", "level",
                  "cassandra", "mysql", "maria", "redis", "rethink", "inno"]
    for item in to_replace:
        regex = re.compile(item, re.IGNORECASE)
        all_text = regex.sub("Oleg", all_text)

    regex = re.compile(r"@[\w]+")
    all_text = regex.sub(random_moon, all_text)
    regex = re.compile(r"[\?:\( ]?.https?:\/\/[\w\.\/\)]+")
    all_text = regex.sub("", all_text)

    output = open("prepared3.txt", "w")
    output.write(all_text)
    output.close()


if __name__ == '__main__':
    main()
