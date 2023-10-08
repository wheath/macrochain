import json

nmToVal = {}

nmToVal['tokenId'] = '1'
nmToVal['data'] = {}
nmToVal['data']['name'] = 'macros'
nmToVal['data']['description'] = 'diet macros in grams'
nmToVal['data']['edition'] = '1'
nmToVal['data']['attributes'] = []

nmToAttribute = {}
nmToAttribute['trait_type'] = 'fat'
nmToAttribute['value'] = '25 grams'

nmToVal['data']['attributes'].append(nmToAttribute)

nmToAttribute = {}
nmToAttribute['trait_type'] = 'protein'
nmToAttribute['value'] = '65 grams'

nmToVal['data']['attributes'].append(nmToAttribute)

nmToAttribute = {}
nmToAttribute['trait_type'] = 'carbohydrates'
nmToAttribute['value'] = '95 grams'

nmToVal['data']['attributes'].append(nmToAttribute)

print(json.dumps([nmToVal], indent=2))
