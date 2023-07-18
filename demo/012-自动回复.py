import schedule

# import time

# import uiautomation as uia
import importlib


# from PyOfficeRobot.core.WeChatType import WeChat
import PyOfficeRobot

importlib.reload(PyOfficeRobot)
# importlib.reload(PyOfficeRobot.core.WeChatType)

# wx = WeChat()

# # 自己的微信名
# my_wechat_name = "Kimo"

# # 自动回复消息内容
# response_text = "已收到您的订单信息"


# def auto_response():
#     # 双击聊天按钮，会话列表跳到有新消息的会话
#     uia.WindowControl(ClassName="WeChatMainWndForPC").SwitchToThisWindow()
#     uia.WindowControl(ClassName="WeChatMainWndForPC").ButtonControl(
#         Name="聊天"
#     ).DoubleClick(simulateMove=False)
#     time.sleep(0.5)

#     # 获取会话列表
#     chats = wx.GetSessionList()
#     if len(chats) > 0:
#         # 打开第一个聊天窗口
#         wx.ChatWith(chats[0])
#         try:
#             # 获取当前窗口中最后一条聊天记录，返回数据类型是个tuple（微信名，信息内容，runtime ID）
#             last_msg = wx.GetLastMessage
#             if last_msg[0] != my_wechat_name:
#                 """
#                 条件：
#                 不是自己:(last_msg[0] != my_wechat_name)
#                 """
#                 PyOfficeRobot.chat.send_message(who=last_msg[0], message=response_text)
#         except:
#             pass


schedule.every(10).seconds.do(PyOfficeRobot.chat.auto_response)
while True:
    schedule.run_pending()
