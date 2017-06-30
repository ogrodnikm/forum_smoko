# -*- coding: utf-8 -*-

header = u"""
[size=200]Lista Publicystów[/size]
[table=100,null]
[thead]
[tr=textleft]
[th=10,null]Imię i Nazwisko[/th]
[th=10,null]e-mail[/th]
[th=20,null]Teksty[/th]
[th=40,null]Uwagi[/th]
[/tr]
[/thead]
[tbody]
"""

footer = u"""
[/tbody]
[/table]
"""


def main():
    import json

    output = u""
    output += header
    with open("publicysci.json", "r") as f:
        db = json.load(f)
    for idx, author in enumerate(db):
        output += u"\n[tr=bg{}]".format((idx % 2) + 1)
        output += u"\n[td=null,1]{}[/td]".format(author["name"])
        output += u"\n[td=null,1]{}[/td]".format(author["mail"])
        output += u"\n[td=null,1][list]"
        for pub in author["publications"]:
            output += u"\n[*]{}".format(pub)
        output += u"\n[/list][/td]"
        output += u"\n[td=null,1]{}[/td]".format(author["info"])
    output += footer
    output += u"\n"

    with open("output.txt", 'w') as f:
        f.write(output.encode('utf8'))

    print("Success!")


if __name__ == "__main__":
    main()
