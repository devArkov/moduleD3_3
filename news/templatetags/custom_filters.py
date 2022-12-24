from django import template

register = template.Library()


Banned_List = ["idiot", "stupid", "donkey"]


@register.filter('censor')
def censor(sentence=""):
    new_sentence = ""

    for word in sentence.split():
        if word in Banned_List:
            new_sentence += '* '
        else:
            new_sentence += word + ' '

    return new_sentence
