from random import choice, getrandbits

good_sin_nouns = ["the crown","the British countryside","Prince William", "David Cameron", "the NHS"]
good_plu_nouns = ["your children","the Royals","family values", "the Conservatives", "nuns", "your daughters"]
bad_sin_nouns = ["cancer", "inflation", "teen pregnency","AIDs"]
bad_plu_nouns = ["video games","yobs","chavs","taxes", "accidents", "immigrants"]

questions_ing = [("Is", "Are")]
questions_not_ing = [("Does", "Do")]

verbs = ["kill", "hurt", "ruin", "devalue", "mutilate", "harm","destroy","deface"]
#["killing", "hurting", "ruining", "devaluing"]
#["kill", "hurt", "ruin", "devalue"]

ing = bool(getrandbits(1))
sin = bool(getrandbits(1))

question = choice(questions_ing) if ing else choice(questions_not_ing)

question = question[0] if sin else question[1]

verb = choice(verbs)
if ing and verb.endswith("e"):
        verb = verb[:-1]
verb = verb if not ing else verb + "ing"
bad_noun = choice(bad_sin_nouns) if sin else choice(bad_plu_nouns)
#bad_noun = choice(bad_sin_nouns+bad_plu_nouns)
good_noun = choice(good_sin_nouns+good_plu_nouns)

print "{0} {1} {2} {3}?".format(question,
                                bad_noun,
                                verb,
                                good_noun
                                )

