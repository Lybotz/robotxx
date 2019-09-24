
zara = {"shirts":300, 'shorts':'500', 'coats':'100', 'shoes':'350', 'sox':'100'}

'''for o, v in zara:
    print(o, v)
    print(zara)
    print('shirts'[:])
'''

print(zara['shorts'])

zara['baby clothes'] = 900



if "shirts" in zara:
    counter = 0
    while counter < 5:
        for key, val in zara.items():
            counter += 1
            
            print(key, "=", val)
            break
print (key, "=", val)