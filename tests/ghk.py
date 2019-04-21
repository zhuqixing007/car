# from socket import *
# import threading
#
# from other_functions.stop_thread import stop_thread
#
# # HOST = '127.0.0.1'
# # PORT = 12345
# # BUFFSIZE = 1024
# # ADDR = (HOST, PORT)
# #
# # tcpCliSock = socket(AF_INET, SOCK_STREAM)
# # tcpCliSock.bind(('', 9000))
# # tcpCliSock.connect(ADDR)
# #
# #
# # def receive():
# #     while True:
# #         accept_data = tcpCliSock.recv(1024)
# #         msg = str(accept_data, encoding="utf-8")
# #         print('from server：' + msg)
# #
# #
# # def send_msg():
# #     while True:
# #         s = input('>')
# #         if int(s) == 1:
# #             break
# #         else:
# #             tcpCliSock.sendall(bytes(s, encoding="utf-8"))
# #     tcpCliSock.close()
#
#
# # t1 = threading.Thread(target=receive)
# # t1.start()
# # t2 = threading.Thread(target=send_msg)
# # t2.start()
#
#
# import time
#
#
# def test():
#     while True:
#         print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#         time.sleep(1)
#
#
# def test1():
#     while True:
#         global t1
#         t1 = threading.Thread(target=test)
#         t1.start()
#
#
# # t = threading.Thread(target=test1)
# # t.start()
# # time.sleep(5)
# # stop_thread(t1)
#
# def test2():
#     while True:
#         yield time.strftime('%Y-%m-%d %H:%M:%S')
#         print(time.strftime('%Y-%m-%d %H:%M:%S'))
#         time.sleep(2)
#
#
# #
# # line = test2()
# # for l in line:
# #     print(l)
#
#
# # t = threading.Thread(target=test2)
# # t.start()
# # print(t)
#
# def test3():
#     # while True:
#     #     print(time.time())
#     #     time.sleep(2)
#     return 2
# # -*- coding: utf-8 -*-
#
# ###########################################################################
# ## Python code generated with wxFormBuilder (version Mar 18 2019)
# ## http://www.wxformbuilder.org/
# ##
# ## PLEASE DO *NOT* EDIT THIS FILE!
# ###########################################################################
#
# import wx
# import wx.xrc
#
# ###########################################################################
# ## Class MyFrame2
# ###########################################################################
#
# class MyFrame2 ( wx.Frame ):
#
# 	def __init__( self, parent ):
# 		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
#
# 		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
#
# 		bSizer63 = wx.BoxSizer( wx.VERTICAL )
#
# 		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
# 		self.m_staticText50.Wrap( -1 )
#
# 		bSizer63.Add( self.m_staticText50, 0, wx.ALL, 5 )
#
# 		self.m_btn = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
# 		bSizer63.Add( self.m_btn, 0, wx.ALL, 5 )
#
#
# 		self.SetSizer( bSizer63 )
# 		self.Layout()
#
# 		self.Centre( wx.BOTH )
#
# 		# Connect Events
# 		self.m_btn.Bind( wx.EVT_BUTTON, self.m_btnOnButtonClick )
#
# 	def __del__( self ):
# 		pass
#
#
# 	# Virtual event handlers, overide them in your derived class
# 	def m_btnOnButtonClick( self, event ):
# 		event.Skip()
#
#
#
#
# class new_frame(MyFrame2):
#     def __init__(self, parent):
#         MyFrame2.__init__(self, parent)
#
#     def m_btnOnButtonClick(self, event):
#         event.Skip()
#         print('asd')
#         import time
#         self.m_staticText50.SetLabelText(str(time.localtime()))
#
#
#
# app = wx.App(False)
# f = new_frame(None)
# f.Show(True)
# app.MainLoop()

