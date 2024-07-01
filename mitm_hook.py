import datetime
import json
import threading
import time

from mitmproxy.http import HTTPFlow
from mitmproxy import ctx


class Hook:
    def __init__(self):
        self.score_fetch = False
        self.zipped_scores = []

    def exit_later(self):
        print("数据已成功上传。程序将在3秒后执行自动清理动作。")
        time.sleep(3)
        ctx.master.shutdown()

    def response(self, flow: HTTPFlow):

        if "https://www.baidu.com/api/ahfsdafbaqwerhue" in flow.request.url and self.score_fetch:
            print("get request")
            flow.response.headers.add("X-Data-Fetched", "1")
            encoded_zipped_scores = json.dumps(self.zipped_scores)
            flow.response.set_content(encoded_zipped_scores.encode())
            flow.response.status_code = 200
            flow.response.headers["Content-Type"] = "application/json"
            threading.Thread(target=self.exit_later).start()
            return

        if ("https://wl-taiko.wahlap.net/api/user/profile/songscore" in flow.request.url
                and flow.request.headers.get('Authorization')):
            resp_dict = flow.response.json()
            if resp_dict.get("status") != 0:
                print(f"错误: {resp_dict.get('message')}")
                return
            zipped_scores = []
            score_items = resp_dict.get("data", {}).get("scoreInfo", [])
            for score_item in score_items:
                zipped_scores.append((
                    score_item['song_no'],
                    score_item['level'],
                    score_item['high_score'],
                    score_item['best_score_rank'],
                    score_item['good_cnt'],
                    score_item['ok_cnt'],
                    score_item['ng_cnt'],
                    score_item['pound_cnt'],
                    score_item['combo_cnt'],
                    score_item['stage_cnt'],
                    score_item['clear_cnt'],
                    score_item['full_combo_cnt'],
                    score_item['dondaful_combo_cnt'],
                    score_item['update_datetime'],
                ))
            self.score_fetch = True
            self.zipped_scores = zipped_scores
            encoded_zipped_scores = json.dumps(self.zipped_scores, separators=(',', ':'))
            # 使用gzip
            file_name = f"scores_{datetime.datetime.now()}.json"
            print(
                f"成绩数据已获取。保持本程序打开，在电脑版微信打开DonNote小程序，选择“导入成绩”功能，数据将会被自动提交给DonNote。")


addons = [Hook()]
