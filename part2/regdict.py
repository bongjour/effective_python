import mwparserfromhell as mwparserfromhell


def function1(s):
    return "우리의 소원은 통일 {}".format(s)


tmpdict = {
    "내용": lambda s: str(s).upper(),
    "예외": function1
}

print(tmpdict['내용']('s'))
print(tmpdict['예외']('s'))



text = "I has a template! {{birth date and age|1961|8|4}} See it?"

wikicode = mwparserfromhell.parse(text)

tmp = wikicode.filter_templates()

print(wikicode)

print(tmp)
