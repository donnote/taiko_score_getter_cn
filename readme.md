# taiko-score-getter: 太鼓成绩获取

## 介绍
这是一个用于获取太鼓达人成绩的工具。使用本工具可以方便到获取到您的太鼓达人的成绩信息。

## 使用方法
直接运行我们释出的版本exe文件即可，按照提示操作即可获取成绩。


## 打包
使用pyinstaller进行打包，命令如下：
```shell
pyinstaller --add-data 'pre_config.bat;.'  --add-data 'mitm_hook.py;.' --add-data 'post_clean.bat;.' --icon=icon.ico -F taiko_score.py
```
打包后可执行文件在dist目录下。

## 将成绩上传到其他服务器
本程序转送成绩的方式为代理拦截，因此您可以在您的应用中访问代码中固定的api地址，以从拦截地址中获取到成绩信息。

当前的api地址为`https://www.baidu.com/api/ahfsdafbaqwerhue`

一旦用户已经成功设置代理，程序会改写请求返回信息，将成绩返回到这个接口上。 紧接着，您可以将获取到的成绩信息上传到您的第三方服务器上。

请注意，我们不对您的服务器的安全性负责，因此请确保您的服务器安全性。

## 贡献
任何形式的贡献都是欢迎的，包括但不限于：
- 提交issue
- 提交pull request

## 免责声明
使用本工具意味着您同意以下免责声明：
- 您同意提供您从鼓众广场查询得到的成绩信息转发给我们的服务器，以便我们为您进行成绩记录与查询
- 您同意我们将您的成绩信息存储在我们的服务器上，以便为您提供成绩查询服务