import pymysql


def connectDb():
    db_settings = {
        "host": "192.168.56.102",  # 連線資料庫ip
        "port": 3306,
        "user": "yupoo",
        "password": "1234",
        "db": "ec2",  # 連線資料庫名稱
        "charset": "utf8"
    }

    conn = None
    try:
        conn = pymysql.connect(**db_settings)  # 連線成功取得conn物件
    except Exception as ex:
        print(ex)  # 失敗顯示錯誤原因
    finally:
        return conn

connectDb()