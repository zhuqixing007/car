import wx

# from ui.function import ui_functions
# from ui.ui_2 import MyFrame1

from ui.ui2_functions import ui_2_functions


if __name__ == '__main__':
    app = wx.App(False)
    # f = ui_functions(None)
    # f = MyFrame1(None)
    f = ui_2_functions(None)
    f.Show(True)
    app.MainLoop()
