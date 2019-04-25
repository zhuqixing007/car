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

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer8.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer8.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"系统日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer5.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.start_server = wx.Button( self, wx.ID_ANY, u"开启服务器", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.start_server.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.start_server, 1, wx.ALL, 5 )

		self.start_all_car = wx.Button( self, wx.ID_ANY, u"启动所有车辆", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.start_all_car.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.start_all_car, 1, wx.ALL, 5 )

		self.shutdown_all_car = wx.Button( self, wx.ID_ANY, u"停止所有车辆", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.shutdown_all_car.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6.Add( self.shutdown_all_car, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer7.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )


		bSizer8.Add( bSizer1, 1, wx.EXPAND, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer8.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )


		gSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )

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

		self.m_staticText2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer11.Add( self.m_staticText2, 1, wx.ALL, 5 )

		self.car1_state = wx.StaticText( self, wx.ID_ANY, u"离线", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_state.Wrap( -1 )

		self.car1_state.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer11.Add( self.car1_state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"车辆感知信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer15.Add( self.m_staticText4, 1, wx.ALL, 5 )


		bSizer13.Add( bSizer15, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"车速(m/s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer17.Add( self.m_staticText5, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_speed = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_speed.Wrap( -1 )

		self.car1_speed.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer17.Add( self.car1_speed, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer17, 0, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"温度(℃)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer19.Add( self.m_staticText7, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_tem = wx.StaticText( self, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_tem.Wrap( -1 )

		self.car1_tem.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer19.Add( self.car1_tem, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer19, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"湿度(%)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer20.Add( self.m_staticText8, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_hum = wx.StaticText( self, wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_hum.Wrap( -1 )

		self.car1_hum.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer20.Add( self.car1_hum, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer20, 0, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"明火", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		self.m_staticText9.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer21.Add( self.m_staticText9, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_fire = wx.StaticText( self, wx.ID_ANY, u"无", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_fire.Wrap( -1 )

		self.car1_fire.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer21.Add( self.car1_fire, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer21, 0, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"烟雾", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer22.Add( self.m_staticText10, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_smog = wx.StaticText( self, wx.ID_ANY, u"轻微", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_smog.Wrap( -1 )

		self.car1_smog.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer22.Add( self.car1_smog, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer22, 0, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"网络列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer18.Add( self.m_staticText6, 0, wx.ALL|wx.EXPAND, 5 )

		car1_netChoices = [ u"wifi1", u"wifi2", u"wifi3", u"wifi4", u"wifi5" ]
		self.car1_net = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, car1_netChoices, 0 )
		self.car1_net.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer18.Add( self.car1_net, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer18, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer13, 0, wx.EXPAND, 5 )

		self.m_staticline15 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer12.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"车速设定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		self.m_staticText18.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer23.Add( self.m_staticText18, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_setspeed = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
		self.car1_setspeed.SetDigits( 0 )
		self.car1_setspeed.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer23.Add( self.car1_setspeed, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_send = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_send.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer23.Add( self.car1_send, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer23, 0, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"运行日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		self.m_staticText19.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer24.Add( self.m_staticText19, 1, wx.ALL|wx.EXPAND, 5 )

		self.car1_start = wx.Button( self, wx.ID_ANY, u"启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_start.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer24.Add( self.car1_start, 0, wx.ALL, 5 )

		self.car1_stop = wx.Button( self, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car1_stop.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer24.Add( self.car1_stop, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer24, 0, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer25.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer25, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )


		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )

		self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( bSizer10, 1, wx.EXPAND, 5 )

		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer2.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )


		gSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticline81 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer26.Add( self.m_staticline81, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline37 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer26.Add( self.m_staticline37, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline141 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer101.Add( self.m_staticline141, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"1号车", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer111.Add( self.m_staticText21, 1, wx.ALL, 5 )

		self.car2_state = wx.StaticText( self, wx.ID_ANY, u"离线", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_state.Wrap( -1 )

		self.car2_state.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer111.Add( self.car2_state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer101.Add( bSizer111, 0, wx.EXPAND, 5 )

		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer131 = wx.BoxSizer( wx.VERTICAL )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"车辆感知信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		self.m_staticText41.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer151.Add( self.m_staticText41, 1, wx.ALL, 5 )


		bSizer131.Add( bSizer151, 0, wx.EXPAND, 5 )

		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"车速(m/s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		self.m_staticText51.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer171.Add( self.m_staticText51, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_speed = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_speed.Wrap( -1 )

		self.car2_speed.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer171.Add( self.car2_speed, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer171, 0, wx.EXPAND, 5 )

		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"温度(℃)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )

		self.m_staticText71.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer191.Add( self.m_staticText71, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_tem = wx.StaticText( self, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_tem.Wrap( -1 )

		self.car2_tem.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer191.Add( self.car2_tem, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer191, 0, wx.EXPAND, 5 )

		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"湿度(%)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		self.m_staticText81.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer201.Add( self.m_staticText81, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_hum = wx.StaticText( self, wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_hum.Wrap( -1 )

		self.car2_hum.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer201.Add( self.car2_hum, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer201, 0, wx.EXPAND, 5 )

		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"明火", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		self.m_staticText91.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer211.Add( self.m_staticText91, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_fire = wx.StaticText( self, wx.ID_ANY, u"无", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_fire.Wrap( -1 )

		self.car2_fire.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer211.Add( self.car2_fire, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer211, 0, wx.EXPAND, 5 )

		bSizer221 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"烟雾", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		self.m_staticText101.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer221.Add( self.m_staticText101, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_smog = wx.StaticText( self, wx.ID_ANY, u"轻微", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_smog.Wrap( -1 )

		self.car2_smog.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer221.Add( self.car2_smog, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer221, 0, wx.EXPAND, 5 )

		bSizer181 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"网络列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		self.m_staticText61.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer181.Add( self.m_staticText61, 0, wx.ALL|wx.EXPAND, 5 )

		car2_netChoices = [ u"wifi1", u"wifi2", u"wifi3", u"wifi4", u"wifi5" ]
		self.car2_net = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, car2_netChoices, 0 )
		self.car2_net.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer181.Add( self.car2_net, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer131.Add( bSizer181, 1, wx.EXPAND, 5 )


		bSizer121.Add( bSizer131, 0, wx.EXPAND, 5 )

		self.m_staticline151 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer121.Add( self.m_staticline151, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer141 = wx.BoxSizer( wx.VERTICAL )

		bSizer231 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText181 = wx.StaticText( self, wx.ID_ANY, u"车速设定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )

		self.m_staticText181.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer231.Add( self.m_staticText181, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_setspeed = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
		self.car2_setspeed.SetDigits( 0 )
		self.car2_setspeed.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer231.Add( self.car2_setspeed, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_send = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_send.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer231.Add( self.car2_send, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer141.Add( bSizer231, 0, wx.EXPAND, 5 )

		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText191 = wx.StaticText( self, wx.ID_ANY, u"运行日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )

		self.m_staticText191.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer241.Add( self.m_staticText191, 1, wx.ALL|wx.EXPAND, 5 )

		self.car2_start = wx.Button( self, wx.ID_ANY, u"启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_start.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer241.Add( self.car2_start, 0, wx.ALL, 5 )

		self.car2_stop = wx.Button( self, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car2_stop.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer241.Add( self.car2_stop, 0, wx.ALL, 5 )


		bSizer141.Add( bSizer241, 0, wx.EXPAND, 5 )

		bSizer251 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer251.Add( self.m_textCtrl3, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer141.Add( bSizer251, 1, wx.EXPAND, 5 )


		bSizer121.Add( bSizer141, 1, wx.EXPAND, 5 )


		bSizer101.Add( bSizer121, 1, wx.EXPAND, 5 )

		self.m_staticline121 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer101.Add( self.m_staticline121, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline38 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer101.Add( self.m_staticline38, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer26.Add( bSizer101, 1, wx.EXPAND, 5 )

		self.m_staticline71 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer26.Add( self.m_staticline71, 0, wx.EXPAND |wx.ALL, 5 )


		gSizer1.Add( bSizer26, 1, wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticline82 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer27.Add( self.m_staticline82, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer102 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline142 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer102.Add( self.m_staticline142, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"1号车", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer112.Add( self.m_staticText22, 1, wx.ALL, 5 )

		self.car3_state = wx.StaticText( self, wx.ID_ANY, u"离线", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_state.Wrap( -1 )

		self.car3_state.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer112.Add( self.car3_state, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer102.Add( bSizer112, 0, wx.EXPAND, 5 )

		bSizer122 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer132 = wx.BoxSizer( wx.VERTICAL )

		bSizer152 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"车辆感知信息", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer152.Add( self.m_staticText42, 1, wx.ALL, 5 )


		bSizer132.Add( bSizer152, 0, wx.EXPAND, 5 )

		bSizer172 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"车速(m/s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		self.m_staticText52.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer172.Add( self.m_staticText52, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_speed = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_speed.Wrap( -1 )

		self.car3_speed.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer172.Add( self.car3_speed, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer172, 0, wx.EXPAND, 5 )

		bSizer192 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText72 = wx.StaticText( self, wx.ID_ANY, u"温度(℃)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )

		self.m_staticText72.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer192.Add( self.m_staticText72, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_tem = wx.StaticText( self, wx.ID_ANY, u"25", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_tem.Wrap( -1 )

		self.car3_tem.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer192.Add( self.car3_tem, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer192, 0, wx.EXPAND, 5 )

		bSizer202 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"湿度(%)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		self.m_staticText82.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer202.Add( self.m_staticText82, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_hum = wx.StaticText( self, wx.ID_ANY, u"40", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_hum.Wrap( -1 )

		self.car3_hum.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer202.Add( self.car3_hum, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer202, 0, wx.EXPAND, 5 )

		bSizer212 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText92 = wx.StaticText( self, wx.ID_ANY, u"明火", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )

		self.m_staticText92.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer212.Add( self.m_staticText92, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_fire = wx.StaticText( self, wx.ID_ANY, u"无", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_fire.Wrap( -1 )

		self.car3_fire.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer212.Add( self.car3_fire, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer212, 0, wx.EXPAND, 5 )

		bSizer222 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText102 = wx.StaticText( self, wx.ID_ANY, u"烟雾", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText102.Wrap( -1 )

		self.m_staticText102.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer222.Add( self.m_staticText102, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_smog = wx.StaticText( self, wx.ID_ANY, u"轻微", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_smog.Wrap( -1 )

		self.car3_smog.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer222.Add( self.car3_smog, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer222, 0, wx.EXPAND, 5 )

		bSizer182 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"网络列表", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		self.m_staticText62.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer182.Add( self.m_staticText62, 0, wx.ALL|wx.EXPAND, 5 )

		car3_netChoices = [ u"wifi1", u"wifi2", u"wifi3", u"wifi4", u"wifi5" ]
		self.car3_net = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, car3_netChoices, 0 )
		self.car3_net.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer182.Add( self.car3_net, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer132.Add( bSizer182, 1, wx.EXPAND, 5 )


		bSizer122.Add( bSizer132, 0, wx.EXPAND, 5 )

		self.m_staticline152 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer122.Add( self.m_staticline152, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer142 = wx.BoxSizer( wx.VERTICAL )

		bSizer232 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText182 = wx.StaticText( self, wx.ID_ANY, u"车速设定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText182.Wrap( -1 )

		self.m_staticText182.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer232.Add( self.m_staticText182, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_setspeed = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 0, 1 )
		self.car3_setspeed.SetDigits( 0 )
		self.car3_setspeed.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer232.Add( self.car3_setspeed, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_send = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_send.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer232.Add( self.car3_send, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer142.Add( bSizer232, 0, wx.EXPAND, 5 )

		bSizer242 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText192 = wx.StaticText( self, wx.ID_ANY, u"运行日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText192.Wrap( -1 )

		self.m_staticText192.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer242.Add( self.m_staticText192, 1, wx.ALL|wx.EXPAND, 5 )

		self.car3_start = wx.Button( self, wx.ID_ANY, u"启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_start.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer242.Add( self.car3_start, 0, wx.ALL, 5 )

		self.car3_stop = wx.Button( self, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.car3_stop.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer242.Add( self.car3_stop, 0, wx.ALL, 5 )


		bSizer142.Add( bSizer242, 0, wx.EXPAND, 5 )

		bSizer252 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl4.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer252.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer142.Add( bSizer252, 1, wx.EXPAND, 5 )


		bSizer122.Add( bSizer142, 1, wx.EXPAND, 5 )


		bSizer102.Add( bSizer122, 1, wx.EXPAND, 5 )

		self.m_staticline122 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer102.Add( self.m_staticline122, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline39 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer102.Add( self.m_staticline39, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer27.Add( bSizer102, 1, wx.EXPAND, 5 )

		self.m_staticline92 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer27.Add( self.m_staticline92, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline72 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL|wx.LI_VERTICAL )
		bSizer27.Add( self.m_staticline72, 0, wx.EXPAND |wx.ALL, 5 )


		gSizer1.Add( bSizer27, 1, wx.EXPAND, 5 )


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


