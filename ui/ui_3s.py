# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Mar 18 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"无人车后台监控", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer70 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"1号车", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer11.Add( self.m_staticText2, 1, wx.ALL, 5 )

		self.state = wx.StaticText( self, wx.ID_ANY, u"离线", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.state.Wrap( -1 )

		bSizer11.Add( self.state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"车辆感知信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer15.Add( self.m_staticText4, 1, wx.ALL, 5 )


		bSizer13.Add( bSizer15, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"车速(m/s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer17.Add( self.m_staticText5, 1, wx.ALL|wx.EXPAND, 5 )

		self.speed = wx.StaticText( self, wx.ID_ANY, u"__", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.speed.Wrap( -1 )

		bSizer17.Add( self.speed, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer17, 0, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"温度(℃)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer19.Add( self.m_staticText7, 1, wx.ALL|wx.EXPAND, 5 )

		self.tem = wx.StaticText( self, wx.ID_ANY, u"__", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tem.Wrap( -1 )

		bSizer19.Add( self.tem, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer19, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"湿度(%)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer20.Add( self.m_staticText8, 1, wx.ALL|wx.EXPAND, 5 )

		self.hum = wx.StaticText( self, wx.ID_ANY, u"__", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hum.Wrap( -1 )

		bSizer20.Add( self.hum, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer20, 0, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"明火", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer21.Add( self.m_staticText9, 1, wx.ALL|wx.EXPAND, 5 )

		self.fire = wx.StaticText( self, wx.ID_ANY, u"__", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fire.Wrap( -1 )

		bSizer21.Add( self.fire, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"烟雾", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer22.Add( self.m_staticText10, 1, wx.ALL|wx.EXPAND, 5 )

		self.smoke = wx.StaticText( self, wx.ID_ANY, u"__", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.smoke.Wrap( -1 )

		bSizer22.Add( self.smoke, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer22, 0, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"网络列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer18.Add( self.m_staticText6, 0, wx.ALL|wx.EXPAND, 5 )

		netChoices = []
		self.net = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, netChoices, 0 )
		bSizer18.Add( self.net, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer18, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer13, 0, wx.EXPAND, 5 )

		self.m_staticline15 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer12.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"车速设定(m/s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer23.Add( self.m_staticText18, 1, wx.ALL|wx.EXPAND, 5 )

		self.speed_set = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
		self.speed_set.SetDigits( 0 )
		bSizer23.Add( self.speed_set, 1, wx.ALL|wx.EXPAND, 5 )

		self.speed_send = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.speed_send, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer23, 0, wx.EXPAND, 5 )

		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"采样间隔(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer181.Add( self.m_staticText17, 1, wx.ALL|wx.EXPAND, 5 )

		self.sample = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer181.Add( self.sample, 1, wx.ALL|wx.EXPAND, 5 )

		self.sample_send = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer181.Add( self.sample_send, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer181, 0, wx.EXPAND, 5 )

		bSizer251 = wx.BoxSizer( wx.HORIZONTAL )

		self.map = wx.Button( self, wx.ID_ANY, u"显示地图", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer251.Add( self.map, 1, wx.ALL, 5 )

		self.vision = wx.Button( self, wx.ID_ANY, u"显示视频", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer251.Add( self.vision, 1, wx.ALL, 5 )

		self.out_log = wx.Button( self, wx.ID_ANY, u"导出仓库日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer251.Add( self.out_log, 1, wx.ALL, 5 )


		bSizer14.Add( bSizer251, 0, wx.EXPAND, 5 )

		bSizer241 = wx.BoxSizer( wx.VERTICAL )

		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer191 = wx.BoxSizer( wx.VERTICAL )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"运行日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer24.Add( self.m_staticText19, 1, wx.ALL|wx.EXPAND, 5 )

		self.start = wx.Button( self, wx.ID_ANY, u"启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.start, 0, wx.ALL, 5 )

		self.stop = wx.Button( self, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.stop, 0, wx.ALL, 5 )


		bSizer191.Add( bSizer24, 0, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.log = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer25.Add( self.log, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer191.Add( bSizer25, 1, wx.EXPAND, 5 )


		bSizer201.Add( bSizer191, 1, wx.EXPAND, 5 )

		bSizer211 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText181 = wx.StaticText( self, wx.ID_ANY, u"未授权人员", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )

		bSizer211.Add( self.m_staticText181, 0, wx.ALL|wx.EXPAND, 5 )

		self.img = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.img, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer201.Add( bSizer211, 1, wx.EXPAND, 5 )


		bSizer241.Add( bSizer201, 1, wx.EXPAND, 5 )


		bSizer14.Add( bSizer241, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )

		self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( bSizer10, 1, wx.EXPAND, 5 )

		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer70.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer70 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


