# page 17 menu
# Python data 轉成(dump) Json 格式輸出

import json

menu = {
    "breakfast": {
        "hours": "7-11",
        "items": {
                "breakfast burritos": "$60",
                "pancakes": "$40"
                }
        },
    "lunch" : {
        "hours": "11-3",
        "items": {
            "hamburger": "$50"
                }
        },
    "dinner": {
        "hours": "3-10",
        "items": {
       "spaghetti": "$80"
                }
        }
}
print(json.dumps(menu))