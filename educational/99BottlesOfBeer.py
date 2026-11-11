

nbOfBottles = int(99)



for bottles in range(0, 100):
    if nbOfBottles > int(1):
        print(f"""
{nbOfBottles} bottles of beer on the wall,

{nbOfBottles} bottles of beer,

Take one down,

Pass it around,
""")
        nbOfBottles -=1

    else:
        print(f"""
1 bottle of beer on the wall,

1 bottle of beer,

Take one down,

Pass it around,

0 beer on the wall !
""")
        break



