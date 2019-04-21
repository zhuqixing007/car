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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"协同智能车后台监控系统", pos = wx.DefaultPosition, size = wx.Size( 1200,900 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer73 = wx.BoxSizer( wx.VERTICAL )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer1.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline23 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer1.Add( self.m_staticline23, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer62.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline24 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer62.Add( self.m_staticline24, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"系统日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer8.Add( self.m_staticText1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer62.Add( bSizer8, 0, wx.EXPAND, 5 )

		bSizer63 = wx.BoxSizer( wx.HORIZONTAL )

		self.start_server = wx.Button( self, wx.ID_ANY, u"开启服务器", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.start_server.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer63.Add( self.start_server, 1, wx.ALL|wx.EXPAND, 5 )

		self.start_all_car = wx.Button( self, wx.ID_ANY, u"启动所有车辆", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.start_all_car.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer63.Add( self.start_all_car, 1, wx.ALL|wx.EXPAND, 5 )

		self.shutdown_all_car = wx.Button( self, wx.ID_ANY, u"关闭所有车辆", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.shutdown_all_car.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer63.Add( self.shutdown_all_car, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer62.Add( bSizer63, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer10.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer62.Add( bSizer10, 1, wx.EXPAND, 5 )

		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer62.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer62, 1, wx.EXPAND, 5 )

		self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer1.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer73.Add( bSizer1, 1, wx.EXPAND, 5 )


		gSizer1.Add( bSizer73, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer76 = wx.BoxSizer( wx.VERTICAL )

		bSizer77 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline16 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer77.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline27 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer77.Add( self.m_staticline27, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"1号车", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer5.Add( self.m_staticText2, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_state = wx.StaticText( self, wx.ID_ANY, u"离线", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_state.Wrap( -1 )

		self.car1_state.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.car1_state.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer5.Add( self.car1_state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer77.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"车辆感知信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer15.Add( self.m_staticText11, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer15, 0, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"车速(m/s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer16.Add( self.m_staticText12, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer16.Add( self.m_staticText13, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer16, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"温度(℃)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer17.Add( self.m_staticText14, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer17.Add( self.m_staticText15, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer17, 0, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"湿度(%)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer18.Add( self.m_staticText16, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		self.m_staticText17.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer18.Add( self.m_staticText17, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer18, 0, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"明火", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer19.Add( self.m_staticText18, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"无", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer19.Add( self.m_staticText19, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer19, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"烟雾", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer20.Add( self.m_staticText20, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"轻微", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer20.Add( self.m_staticText21, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer20, 0, wx.EXPAND, 5 )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"网络列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		self.m_staticText47.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer60.Add( self.m_staticText47, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox4Choices = [ u"a", u"b", u"c", u"d", u"e", u"f", u"g" ]
		self.m_listBox4 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox4Choices, 0 )
		self.m_listBox4.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer60.Add( self.m_listBox4, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer60, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer13, 0, wx.EXPAND, 5 )

		self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer12.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"车速设定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer21.Add( self.m_staticText22, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_speed = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.car1_speed.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer21.Add( self.car1_speed, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_send = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_send.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer21.Add( self.car1_send, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer65 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"运行日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		self.m_staticText23.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer65.Add( self.m_staticText23, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer22.Add( bSizer65, 1, wx.EXPAND, 5 )

		bSizer64 = wx.BoxSizer( wx.HORIZONTAL )

		self.car1_start = wx.Button( self, wx.ID_ANY, u"启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_start.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer64.Add( self.car1_start, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_stop = wx.Button( self, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_stop.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer64.Add( self.car1_stop, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer22.Add( bSizer64, 1, wx.EXPAND, 5 )


		bSizer14.Add( bSizer22, 0, wx.EXPAND, 5 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer23.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer23, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer77.Add( bSizer12, 1, wx.EXPAND, 5 )

		self.m_staticline28 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer77.Add( self.m_staticline28, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer76.Add( bSizer77, 1, wx.EXPAND, 5 )


		bSizer2.Add( bSizer76, 1, wx.EXPAND, 5 )

		self.m_staticline25 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline25, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline26 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline26, 0, wx.EXPAND |wx.ALL, 5 )


		gSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticline29 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer3.Add( self.m_staticline29, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline30 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer3.Add( self.m_staticline30, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer75 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline15 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer75.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"2号车", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.m_staticText3, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_state = wx.StaticText( self, wx.ID_ANY, u"离线", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_state.Wrap( -1 )

		self.car2_state.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.car2_state.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer6.Add( self.car2_state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer75.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer131 = wx.BoxSizer( wx.VERTICAL )

		bSizer151 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"车辆感知信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		self.m_staticText111.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer151.Add( self.m_staticText111, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer151, 0, wx.EXPAND, 5 )

		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"车速(m/s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		self.m_staticText121.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer161.Add( self.m_staticText121, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		self.m_staticText131.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer161.Add( self.m_staticText131, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer161, 0, wx.EXPAND, 5 )

		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText141 = wx.StaticText( self, wx.ID_ANY, u"温度(℃)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		self.m_staticText141.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer171.Add( self.m_staticText141, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText151 = wx.StaticText( self, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )

		self.m_staticText151.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer171.Add( self.m_staticText151, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer171, 0, wx.EXPAND, 5 )

		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText161 = wx.StaticText( self, wx.ID_ANY, u"湿度(%)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		self.m_staticText161.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer181.Add( self.m_staticText161, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText171 = wx.StaticText( self, wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )

		self.m_staticText171.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer181.Add( self.m_staticText171, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer181, 0, wx.EXPAND, 5 )

		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText181 = wx.StaticText( self, wx.ID_ANY, u"明火", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )

		self.m_staticText181.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer191.Add( self.m_staticText181, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText191 = wx.StaticText( self, wx.ID_ANY, u"无", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )

		self.m_staticText191.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer191.Add( self.m_staticText191, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer191, 0, wx.EXPAND, 5 )

		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText201 = wx.StaticText( self, wx.ID_ANY, u"烟雾", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )

		self.m_staticText201.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer201.Add( self.m_staticText201, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText211 = wx.StaticText( self, wx.ID_ANY, u"轻微", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		self.m_staticText211.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer201.Add( self.m_staticText211, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer201, 0, wx.EXPAND, 5 )

		bSizer601 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText471 = wx.StaticText( self, wx.ID_ANY, u"网络列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText471.Wrap( -1 )

		self.m_staticText471.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer601.Add( self.m_staticText471, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox41Choices = [ u"a", u"b", u"c", u"d", u"e", u"f", u"g" ]
		self.m_listBox41 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox41Choices, 0 )
		self.m_listBox41.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer601.Add( self.m_listBox41, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer601, 1, wx.EXPAND, 5 )


		bSizer121.Add( bSizer131, 0, wx.EXPAND, 5 )

		self.m_staticline19 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer121.Add( self.m_staticline19, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer141 = wx.BoxSizer( wx.VERTICAL )

		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText221 = wx.StaticText( self, wx.ID_ANY, u"车速设定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		self.m_staticText221.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer211.Add( self.m_staticText221, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_speed = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.car2_speed.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer211.Add( self.car2_speed, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_send = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_send.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer211.Add( self.car2_send, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer141.Add( bSizer211, 0, wx.EXPAND, 5 )

		bSizer221 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText231 = wx.StaticText( self, wx.ID_ANY, u"运行日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )

		self.m_staticText231.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer71.Add( self.m_staticText231, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer221.Add( bSizer71, 1, wx.EXPAND, 5 )

		bSizer641 = wx.BoxSizer( wx.HORIZONTAL )

		self.car2_start = wx.Button( self, wx.ID_ANY, u"启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_start.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer641.Add( self.car2_start, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_stop = wx.Button( self, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_stop.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer641.Add( self.car2_stop, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer221.Add( bSizer641, 1, wx.EXPAND, 5 )


		bSizer141.Add( bSizer221, 0, wx.EXPAND, 5 )

		bSizer231 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl21.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer231.Add( self.m_textCtrl21, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer141.Add( bSizer231, 1, wx.EXPAND, 5 )


		bSizer121.Add( bSizer141, 1, wx.EXPAND, 5 )


		bSizer75.Add( bSizer121, 1, wx.EXPAND, 5 )

		self.m_staticline31 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer75.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline32 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer75.Add( self.m_staticline32, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( bSizer75, 1, wx.EXPAND, 5 )

		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer3.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )


		gSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer78 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticline17 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer78.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer79 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline18 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer79.Add( self.m_staticline18, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"3号车", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer7.Add( self.m_staticText4, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_state = wx.StaticText( self, wx.ID_ANY, u"离线", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_state.Wrap( -1 )

		self.car3_state.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.car3_state.SetForegroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer7.Add( self.car3_state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer79.Add( bSizer7, 0, wx.EXPAND, 5 )

		bSizer122 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer132 = wx.BoxSizer( wx.VERTICAL )

		bSizer152 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText112 = wx.StaticText( self, wx.ID_ANY, u"车辆感知信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText112.Wrap( -1 )

		self.m_staticText112.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer152.Add( self.m_staticText112, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer152, 0, wx.EXPAND, 5 )

		bSizer162 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText122 = wx.StaticText( self, wx.ID_ANY, u"车速(m/s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText122.Wrap( -1 )

		self.m_staticText122.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer162.Add( self.m_staticText122, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText132 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText132.Wrap( -1 )

		self.m_staticText132.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer162.Add( self.m_staticText132, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer162, 0, wx.EXPAND, 5 )

		bSizer172 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText142 = wx.StaticText( self, wx.ID_ANY, u"温度(℃)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText142.Wrap( -1 )

		self.m_staticText142.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer172.Add( self.m_staticText142, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText152 = wx.StaticText( self, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText152.Wrap( -1 )

		self.m_staticText152.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer172.Add( self.m_staticText152, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer172, 0, wx.EXPAND, 5 )

		bSizer182 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText162 = wx.StaticText( self, wx.ID_ANY, u"湿度(%)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )

		self.m_staticText162.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer182.Add( self.m_staticText162, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText172 = wx.StaticText( self, wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText172.Wrap( -1 )

		self.m_staticText172.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer182.Add( self.m_staticText172, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer182, 0, wx.EXPAND, 5 )

		bSizer192 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText182 = wx.StaticText( self, wx.ID_ANY, u"明火", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText182.Wrap( -1 )

		self.m_staticText182.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer192.Add( self.m_staticText182, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText192 = wx.StaticText( self, wx.ID_ANY, u"无", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText192.Wrap( -1 )

		self.m_staticText192.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer192.Add( self.m_staticText192, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer192, 0, wx.EXPAND, 5 )

		bSizer202 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText202 = wx.StaticText( self, wx.ID_ANY, u"烟雾", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText202.Wrap( -1 )

		self.m_staticText202.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer202.Add( self.m_staticText202, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText212 = wx.StaticText( self, wx.ID_ANY, u"轻微", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )

		self.m_staticText212.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer202.Add( self.m_staticText212, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer202, 0, wx.EXPAND, 5 )

		bSizer602 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText472 = wx.StaticText( self, wx.ID_ANY, u"网络列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText472.Wrap( -1 )

		self.m_staticText472.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer602.Add( self.m_staticText472, 0, wx.ALL|wx.EXPAND, 5 )

		m_listBox42Choices = [ u"a", u"b", u"c", u"d", u"e", u"f", u"g" ]
		self.m_listBox42 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox42Choices, 0 )
		self.m_listBox42.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer602.Add( self.m_listBox42, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer602, 1, wx.EXPAND, 5 )


		bSizer122.Add( bSizer132, 0, wx.EXPAND, 5 )

		self.m_staticline20 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer122.Add( self.m_staticline20, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer142 = wx.BoxSizer( wx.VERTICAL )

		bSizer212 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText222 = wx.StaticText( self, wx.ID_ANY, u"车速设定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText222.Wrap( -1 )

		self.m_staticText222.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer212.Add( self.m_staticText222, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_speed = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0 )
		self.car3_speed.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer212.Add( self.car3_speed, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_send = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_send.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer212.Add( self.car3_send, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer142.Add( bSizer212, 0, wx.EXPAND, 5 )

		bSizer222 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer72 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText232 = wx.StaticText( self, wx.ID_ANY, u"运行日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText232.Wrap( -1 )

		self.m_staticText232.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer72.Add( self.m_staticText232, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer222.Add( bSizer72, 1, wx.EXPAND, 5 )

		bSizer642 = wx.BoxSizer( wx.HORIZONTAL )

		self.car3_start = wx.Button( self, wx.ID_ANY, u"启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_start.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer642.Add( self.car3_start, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_stop = wx.Button( self, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_stop.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer642.Add( self.car3_stop, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer222.Add( bSizer642, 1, wx.EXPAND, 5 )


		bSizer142.Add( bSizer222, 0, wx.EXPAND, 5 )

		bSizer232 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl22.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer232.Add( self.m_textCtrl22, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer142.Add( bSizer232, 1, wx.EXPAND, 5 )


		bSizer122.Add( bSizer142, 1, wx.EXPAND, 5 )


		bSizer79.Add( bSizer122, 1, wx.EXPAND, 5 )

		self.m_staticline35 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer79.Add( self.m_staticline35, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline36 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer79.Add( self.m_staticline36, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer78.Add( bSizer79, 1, wx.EXPAND, 5 )

		self.m_staticline33 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer78.Add( self.m_staticline33, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline34 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer78.Add( self.m_staticline34, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer4.Add( bSizer78, 1, wx.EXPAND, 5 )


		gSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.MyFrame1OnClose )
		self.start_server.Bind( wx.EVT_BUTTON, self.start_serverOnButtonClick )
		self.start_all_car.Bind( wx.EVT_BUTTON, self.start_all_carOnButtonClick )
		self.shutdown_all_car.Bind( wx.EVT_BUTTON, self.shutdown_all_carOnButtonClick )
		self.car1_send.Bind( wx.EVT_BUTTON, self.car1_sendOnButtonClick )
		self.car1_start.Bind( wx.EVT_BUTTON, self.car1_startOnButtonClick )
		self.car1_stop.Bind( wx.EVT_BUTTON, self.car1_stopOnButtonClick )
		self.car2_send.Bind( wx.EVT_BUTTON, self.car2_sendOnButtonClick )
		self.car2_start.Bind( wx.EVT_BUTTON, self.car2_startOnButtonClick )
		self.car2_stop.Bind( wx.EVT_BUTTON, self.car2_stopOnButtonClick )
		self.car3_send.Bind( wx.EVT_BUTTON, self.car3_sendOnButtonClick )
		self.car3_start.Bind( wx.EVT_BUTTON, self.car3_startOnButtonClick )
		self.car3_stop.Bind( wx.EVT_BUTTON, self.car3_stopOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def MyFrame1OnClose( self, event ):
		event.Skip()

	def start_serverOnButtonClick( self, event ):
		event.Skip()

	def start_all_carOnButtonClick( self, event ):
		event.Skip()

	def shutdown_all_carOnButtonClick( self, event ):
		event.Skip()

	def car1_sendOnButtonClick( self, event ):
		event.Skip()

	def car1_startOnButtonClick( self, event ):
		event.Skip()

	def car1_stopOnButtonClick( self, event ):
		event.Skip()

	def car2_sendOnButtonClick( self, event ):
		event.Skip()

	def car2_startOnButtonClick( self, event ):
		event.Skip()

	def car2_stopOnButtonClick( self, event ):
		event.Skip()

	def car3_sendOnButtonClick( self, event ):
		event.Skip()

	def car3_startOnButtonClick( self, event ):
		event.Skip()

	def car3_stopOnButtonClick( self, event ):
		event.Skip()


