meme_dict = {
            "ROFL": "shutka",
            "AGRITSYA": "silno zlitsya",
            "LOL": "chto to smeshnoe",
            "KRIPOVIY": "strashniy",
            "SCHISCH": "vostorg"
            }
word = input("Введите непонятное слово (большими буквами!): ")
    
if word in meme_dict.keys():
   print(meme_dict[word])
else:
    word = input("takogo slova net")
