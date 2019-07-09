import wx

# from ui.function import ui_functions
# from ui.ui_2 import MyFrame1
# from ui.ui2_funcp import ui2_cp
# from ui.ui2_functions import ui_2_functions
from ui.ui_3s_functions import ui_3s_functions


if __name__ == '__main__':
    app = wx.App(False)
    # f = ui_functions(None)
    # f = MyFrame1(None)
    # f = ui2_cp(None)
    # f = ui_2_functions(None)
    f = ui_3s_functions(None)
    f.Show(True)
    app.MainLoop()
