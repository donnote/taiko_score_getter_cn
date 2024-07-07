import os
import subprocess
import sys
import time

from mitmproxy.tools.main import mitmdump


def get_resource_real_path(raw_file_name):
    if hasattr(sys, '_MEIPASS'):
        # When running from the bundled app
        return os.path.join(sys._MEIPASS, raw_file_name)
    else:
        # When running from the script directly
        return os.path.join(os.path.dirname(__file__), raw_file_name)


if __name__ == '__main__':
    # 在独立进程中启动mitmproxy
    # 执行bat脚本来配置本地代理和证书文件
    print("正在初始化本地代理与证书")
    pre_config = subprocess.Popen([get_resource_real_path('pre_config.bat')], shell=True)
    pre_config.wait()
    if pre_config.returncode != 0:
        print("初始化失败，请检查错误信息。")
        time.sleep(5)
        exit(1)
    print('正在监听成绩数据。请使用电脑端微信，打开鼓众广场小程序，点击"游戏成绩"，等待程序自动获取成绩数据。')
    mitmdump(['-s', get_resource_real_path('mitm_hook.py'), '-q'])
    print("正在清理本地代理配置")
    post_clean = subprocess.Popen([get_resource_real_path('post_clean.bat')], shell=True)
    post_clean.wait()
