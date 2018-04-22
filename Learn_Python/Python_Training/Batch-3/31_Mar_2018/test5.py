tmp = {"A":1,
    "B":{"C":[1,2,3]},
        "C":10}
#~ print(tmp["A"]["B"])
tmp["B"]["C"][0] = 100
print tmp