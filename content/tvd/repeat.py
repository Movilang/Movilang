# Інтервальне повторення: у кожному уроці — пари зі слів, що з'являлися 2–3 уроки тому.
from common import L, grill
D = {
 "diary": "a private book of thoughts", "to stare": "to look for a long time", "comet": "a bright object with a tail in the sky",
 "to sneak out": "to leave secretly", "jealous": "unhappy because someone likes another person",
 "vervain": "a plant that weakens vampires", "to invite in": "to ask someone to enter your home",
 "Founders' Council": "the secret group that knows about vampires", "daylight ring": "a ring that protects from the sun",
 "on purpose": "not by accident", "cellar": "a room under a house", "to starve": "to have no food for a long time",
 "charity": "helping people in need", "to find out": "to discover", "to feed on": "to drink blood from",
 "to keep a secret": "not to tell anyone", "to turn (someone)": "to make someone a vampire", "to be in charge": "to be the boss",
 "transition": "the change from human to vampire", "stake": "a wooden weapon", "costume": "clothes for Halloween",
 "humanity": "the ability to feel and care", "to frame": "to make someone look guilty", "craving": "a very strong wish",
 "to erase": "to remove completely", "witch": "a woman with magic powers", "the tomb": "an underground grave",
 "grimoire": "a witch's book of spells", "compulsion": "a vampire's power to control minds", "look-alike": "a person who looks exactly like another",
 "séance": "a meeting to talk to spirits", "adopted": "raised by non-birth parents", "newbie": "a beginner", "to hunt": "to chase and catch",
 "road trip": "a long journey by car", "stalker": "someone who follows a person secretly", "chaperone": "an adult watching young people",
 "compass": "an instrument that shows direction", "deal": "an agreement", "spell": "magic words", "flashback": "a scene from the past",
 "to dig up": "to take out of the ground", "grief": "deep sadness after a death", "birth mother": "the woman who gave birth to you",
 "to cast a spell": "to use magic words", "heartbroken": "very sad because of love", "folklore": "old stories of a people",
 "revenge": "punishment for a past wrong", "double date": "two couples going out together", "to settle in": "to get comfortable in a new place",
 "invitation": "a request to come in", "to avenge": "to punish someone for a wrong", "cheerleading": "dancing and cheering for a team",
 "pageant": "a beauty contest", "escort": "a partner who goes with you", "to crave": "to want very strongly", "addiction": "a habit you can't stop",
 "under control": "managed, not dangerous", "eternity": "time without end", "misery": "great suffering", "to forgive": "to stop being angry",
 "leverage": "something used to pressure someone", "to reveal": "to make a secret known",
}
R = {
  5: ["diary", "to stare", "comet", "to sneak out", "jealous"],
  7: ["vervain", "to invite in", "Founders' Council", "daylight ring", "on purpose"],
  9: ["daylight ring", "cellar", "to starve", "charity", "cheerleading"],
  10: ["vervain", "to feed on", "to keep a secret", "to turn (someone)", "to be in charge"],
  12: ["daylight ring", "transition", "stake", "costume", "Founders' Council"],
  13: ["to feed on", "humanity", "to frame", "craving", "to erase"],
  15: ["vervain", "witch", "the tomb", "Founders' Council", "grimoire"],
  17: ["humanity", "compulsion", "daylight ring", "look-alike", "séance"],
  18: ["to feed on", "transition", "adopted", "newbie", "to hunt"],
  20: ["vervain", "Founders' Council", "road trip", "stalker", "chaperone"],
  22: ["daylight ring", "grimoire", "compass", "deal", "flashback"],
  23: ["spell", "the tomb", "to feed on", "to dig up", "compulsion"],
  24: ["vervain", "grief", "birth mother", "to cast a spell", "heartbroken"],
  25: ["humanity", "to turn (someone)", "folklore", "revenge", "double date"],
  26: ["vervain", "to feed on", "to settle in", "invitation", "to avenge"],
  30: ["pageant", "escort", "to crave", "addiction", "under control"],
  32: ["eternity", "misery", "vervain", "daylight ring", "to forgive"],
  34: ["Founders' Council", "leverage", "to reveal", "the tomb", "compulsion"],
}
for l in L:
    ws = R.get(l["num"])
    if not ws: continue
    t = grill([(w, D[w]) for w in ws], "Інтервальне повторення: ці слова ти вже зустрічав(ла) 2–3 уроки тому.",
              q="Do you still remember these words?")
    t["label"] = "ПОВТОРЕННЯ"
    l["tasks"].insert(len(l["tasks"]) - 1, t)
