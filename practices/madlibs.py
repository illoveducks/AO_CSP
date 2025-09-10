# AO 6th Mad libs

verb = input("give me a verb:\n").strip().lower()
adjective = input("give me an adjective:\n").strip().lower()
name = input("give me a name:\n").strip().title()
name2 = input("give me another name:\n").strip().title()
candy = input("give me a candy:\n").strip().lower()

print("he was", verb, " with a jolly rancher,", name + ".", "Sure loves his jolly ranchers, he likes it when they're", adjective + "." " Hey that other guy, ", name2, "he likes", candy, " Just how ", name, " likes jolly ranchers.")