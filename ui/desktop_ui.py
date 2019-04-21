# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Mar 18 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"车辆状态", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer5.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"电量", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer6.Add( self.m_staticText2, 1, wx.ALL|wx.EXPAND, 5 )

		self.battery = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.battery.SetValue( 20 )
		bSizer6.Add( self.battery, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"温度(℃)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer7.Add( self.m_staticText4, 1, wx.ALL|wx.EXPAND, 5 )

		self.temperature = wx.StaticText( self, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.temperature.Wrap( -1 )

		bSizer7.Add( self.temperature, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer7, 0, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"湿度（%）", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer8.Add( self.m_staticText6, 1, wx.ALL|wx.EXPAND, 5 )

		self.humidity = wx.StaticText( self, wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.humidity.Wrap( -1 )

		bSizer8.Add( self.humidity, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer8, 0, wx.EXPAND, 5 )


		bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"运行日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer11.Add( self.m_staticText10, 1, wx.ALL|wx.EXPAND, 5 )

		self.open = wx.Button( self, wx.ID_ANY, u"开启服务器", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.open, 0, wx.ALL, 5 )

		self.close = wx.Button( self, wx.ID_ANY, u"关闭服务器", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.close, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer12.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer10, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"发送指令", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer15.Add( self.m_staticText11, 1, wx.ALL|wx.EXPAND, 5 )

		self.send_btn = wx.Button( self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.send_btn, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer15, 0, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer16.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer16, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer13, 0, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"位置信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer17.Add( self.m_staticText12, 1, wx.ALL|wx.EXPAND, 5 )

		self.refresh_btn2 = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.refresh_btn2, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer17, 0, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_animCtrl1 = wx.adv.AnimationCtrl( self, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.adv.AC_DEFAULT_STYLE )
		bSizer18.Add( self.m_animCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer18, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MyFrame1OnClose )
		self.open.Bind( wx.EVT_BUTTON, self.openOnButtonClick )
		self.close.Bind( wx.EVT_BUTTON, self.closeOnButtonClick )
		self.send_btn.Bind( wx.EVT_BUTTON, self.send_btnOnButtonClick )
		self.refresh_btn2.Bind( wx.EVT_BUTTON, self.refresh_btn2OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def MyFrame1OnClose( self, event ):
		event.Skip()

	def openOnButtonClick( self, event ):
		event.Skip()

	def closeOnButtonClick( self, event ):
		event.Skip()

	def send_btnOnButtonClick( self, event ):
		event.Skip()

	def refresh_btn2OnButtonClick( self, event ):
		event.Skip()


