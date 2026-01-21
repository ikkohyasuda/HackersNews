import time
import requests


def get_toppage_ids():
    toppage_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
    response = requests.get(toppage_url)
    ids = response.json()  # .jsonの処理は文字列をリストへ変換するのに必要
    return ids[:30]


def get_item(item_id):
    each_url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json?print=pretty"
    response = requests.get(each_url)
    return response.json()


def list_titlelink():
    id_groups = get_toppage_ids()

    for item_id in id_groups:
        time.sleep(1)  # 連続アクセス防止のために1秒待つ

        item = get_item(item_id)

        title = item.get("title")  # .get()を使用すると、対応するキーがない場合は"None"と表示される
        link = item.get("url")

        print(f"{{'title': '{title}', 'link': '{link}'}}")  # "{{"や"}}"で"{"や"}"は文字としての処理となる
        # data = {"title": title, "link": link}とdictにしてもできる


list_titlelink()
