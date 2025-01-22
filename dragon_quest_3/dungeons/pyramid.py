from dragon_quest_3.monsters import(
    Illusion_Shadow,
    King_Frog
)

U1_2 = {
    "name": "ピラミッド 地下1階・地下2階",
    "monstors": [
        Illusion_Shadow.model_dump_json(),
        King_Frog.model_dump_json(),
        {"name": "ミイラおとこ", "drop_item": "まほうのせいすい"},
        {"name": "マミー", "drop_item": "せいすい"},
    ],
    "items": [
        {"name": "52ゴールド", "location": "地下1階 宝箱"},
        {"name": "どくばり", "location": "地下1階 宝箱"},
        {"name": "おうごんのつめ", "location": "地下2階 棺"},
    ],
    "recommend_level": 15,
    "warnings": [
        "地下では呪文が使えないため、回復アイテムを十分に用意してください。",
        "おうごんのつめを入手すると、ピラミッドを出るまでエンカウント率が上昇します。",
    ],
}


F1_2 = {
    "name": "ピラミッド 1階・2階",
    "monsters": [
        {"name": "だいおうガマ", "drop_item": "とげのむち"},
        {"name": "わらいぶくろ", "drop_item": "においぶくろ"},
        {"name": "ミイラおとこ", "drop_item": "まほうのせいすい"},
        {"name": "かえんムカデ", "drop_item": "かしこさのたね"},
    ],
    "items": [
        {"name": "まほうのせいすい", "location": "1階 宝箱"},
        {"name": "ささやきのみつ", "location": "1階 宝箱"},
        {"name": "ちいさなメダル", "location": "1階 宝箱"},
        {"name": "パワーナックル", "location": "1階 宝箱"},
        {"name": "いのりのゆびわ", "location": "1階 宝箱"},
        {"name": "128ゴールド", "location": "1階 宝箱"},
        {"name": "どくがのこな", "location": "1階 宝箱"},
        {"name": "かしこさのたね", "location": "2階 宝箱"},
        {"name": "244ゴールド", "location": "2階 宝箱"},
        {"name": "せいすい", "location": "2階 宝箱"},
        {"name": "ラックのたね", "location": "2階 宝箱"},
    ],
    "recommend_level": 15,
    "warnings": [
        "1階の十字路中央は落とし穴になっており、地下に落とされ呪文が使えなくなるため注意してください。",
        "1階の左上の宝箱には「ひとくいばこ」が潜んでいる可能性があるため、避けて通ることをおすすめします。",
    ],
}


F3_5 = {
    "name": "ピラミッド 3階・4階・5階",
    "monsters": [
        {"name": "だいおうガマ", "drop_item": "とげのむち"},
        {"name": "わらいぶくろ", "drop_item": "においぶくろ"},
        {"name": "ミイラおとこ", "drop_item": "まほうのせいすい"},
        {"name": "マミー", "drop_item": "せいすい"},
    ],
    "items": [
        {"name": "まよけのすず", "location": "3階 宝箱"},
        {"name": "まほうのかぎ", "location": "3階 宝箱"},
        {"name": "エルフののみぐすり", "location": "4階 宝箱"},
        {"name": "マジカルスカート", "location": "4階 宝箱"},
        {"name": "1120ゴールド", "location": "4階 宝箱"},
        {"name": "すばやさのたね", "location": "4階 宝箱"},
        {"name": "せかいじゅのは", "location": "4階 宝箱"},
        {"name": "710ゴールド", "location": "4階 宝箱"},
        {"name": "ちからのたね", "location": "4階 宝箱"},
        {"name": "キメラのつばさ", "location": "4階 宝箱"},
        {"name": "バイキルミン", "location": "4階 宝箱"},
        {"name": "578ゴールド", "location": "4階 宝箱"},
        {"name": "いしのかつら", "location": "4階 宝箱"},
        {"name": "348ゴールド", "location": "4階 宝箱"},
        {"name": "特やくそう", "location": "4階 宝箱"},
        {"name": "ホーリーランス", "location": "4階 宝箱"},
        {"name": "まじないしの服", "location": "5階 宝箱"},
        {"name": "ちいさなメダル", "location": "屋上 足元"},
    ],
    "recommend_level": 15,
    "warnings": [
        "3階のボタンは、最初に一番右下のまるいボタンを押し、次に一番左下のまるいボタンを押すと中央の扉が開きます。",
        "4階の宝箱は開けるたびに戦闘が発生します。回復手段を十分に用意してください。",
        "屋上では一番奥の足元を調べると「ちいさなメダル」が入手できます。",
    ],
}


if __name__ == "__main__":
    print(U1_2["monstors"])
   