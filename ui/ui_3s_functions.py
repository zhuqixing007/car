from other_functions.common_functions import *
from ui.map_pygame import car_map
from ui.ui_3s import MyFrame1
from socket import *
import threading
import re
import os
from sql import sql_operations
from other_functions.stop_thread import stop_thread
import wx
import time
class ui_3s_functions(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.connect_flag = 0
        self.HOST = ''
        self.PORT = 0
        self.tcpCliSock = socket(AF_INET, SOCK_STREAM)
        self.ip.SetValue("129.204.16.212")
        self.port.SetValue("9000")

    def MyFrame1OnClose(self, event):
        os._exit(0)
        event.Skip()

    def speed_sendOnButtonClick(self, event):
        # if self.connect_flag == 1:
        #     speed = self.speed_set.GetValue()
        #     self.tcpCliSock.sendall(str(speed).encode('utf-8'))
        #     self.log.AppendText("发送成功。\n")
        # else:
        #     self.log.AppendText("发送失败，服务器未连接。\n")
        # event.Skip()
        bmp = wx.Image(r'D:\PycharmProjects\car\ui\1.png', wx.BITMAP_TYPE_ANY)
        img = bmp.Scale(290, 380).ConvertToBitmap()
        self.img.SetBitmap(img)

    def sample_sendOnButtonClick(self, event):
        if self.connect_flag == 1:
            sample_rate = self.sample.GetValue()
            send_data = '*R"'+str(sample_rate)+'"#'
            self.tcpCliSock.sendall(str(send_data).encode('utf-8'))
            self.log.AppendText("发送成功。\n")
        else:
            self.log.AppendText("发送失败，服务器未连接。\n")
        event.Skip()

    def mapOnButtonClick(self, event):
        t = threading.Thread(target=car_map)
        t.start()
        event.Skip()

    def out_logOnButtonClick(self, event):
        sensor_data = sql_operations.consult_seneor_data()
        with open(r'D:\3s_programma_files\sensor_data.csv', 'a') as f:
            # f.writelines('时间,车速,温度,湿度,明火,烟雾\n')
            for data in sensor_data:
                line = ','.join(data) + '\n'
                f.writelines(line)
        event.Skip()

    def startOnButtonClick(self, event):
        HOST = self.ip.GetValue()
        PORT = self.port.GetValue()
        pattern1 = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
        pattern2 = re.compile('[0-9]{1,5}$')
        match1 = re.match(pattern1, HOST)
        match2 = re.match(pattern2, PORT)

        def recv(tcpCliSock):
            while True:
                accept_data = tcpCliSock.recv(1024000)
                msg = str(accept_data, encoding="utf-8")
                # print(msg)
                msg_list = msg_split(msg)
                values = []
                for m in msg_list:
                    result = msg_convert(m)
                    if result[0] == "S":
                        info = eval(result[1])
                        self.tem.SetLabelText(str(info['tem']))
                        self.hum.SetLabelText(str(info['hum']))
                        fire = str(info['fire'])
                        smoke = str(info['smoke'])
                        if fire == 'ok':
                            self.fire.SetLabelText('无')
                        else:
                            self.fire.SetLabelText('报警')
                        if smoke == '0':
                            self.smoke.SetLabelText('无')
                        else:
                            self.smoke.SetLabelText('报警')
                        wifi = str(info['wifi_name']) + ',' + str(info['RSSI'])
                        self.net.Set([wifi, ])
                    if result[0] == "L":
                        location = eval(result[1])
                        self.speed.SetLabelText(location["s"])
                    values.append(time.strftime("%Y-%m-%d %H:%M", time.localtime()))
                    values.append(self.speed.GetLabelText())
                    values.append(self.tem.GetLabelText())
                    values.append(self.hum.GetLabelText())
                    values.append(self.fire.GetLabelText())
                    values.append(self.smoke.GetLabelText())
                    history = sql_operations.query_last(values[0])
                    print(values)
                    if not history:
                        sql_operations.insert_into_sensor_data(values)
                    # if result[0] == "P":
                    #     im = base64_to_img(msg)
                    #     with open(r"D:\PycharmProjects\car\ui\1.jpg", "wb") as f:
                    #         f.write(im)
                    #     bmp = wx.Image(r'D:\PycharmProjects\car\ui\1.jpg', wx.BITMAP_TYPE_ANY)
                    #     img = bmp.Scale(290, 380).ConvertToBitmap()
                    #     self.img.SetBitmap(img)
                    if result[0] == "R":
                        pass

        if match1:
            if match2:
                if int(PORT) < 65535 and int(PORT) > 0:
                    self.log.AppendText('尝试连接{}:{}。'.format(HOST, PORT)+'\n')
                    if self.connect_flag == 0:
                        self.PORT = int(PORT)
                        self.HOST = HOST
                        try:
                            ADDR = (self.HOST, self.PORT)
                            self.tcpCliSock.connect(ADDR)
                            # print(self.tcpCliSock)
                        except Exception as e:
                            # print(self.tcpCliSock)
                            # print(e)
                            self.log.AppendText("连接失败，请检查地址和端口号是否正确或者服务器是否开启。\n")
                        else:
                            self.connect_flag = 1
                            global recv_thread
                            recv_thread = threading.Thread(target=recv, args=(self.tcpCliSock,))
                            recv_thread.start()
                        try:
                            self.tcpCliSock.sendall(bytes("""*D"device=daddy"#""", encoding="utf-8"))
                        except:
                            pass
                        else:
                            self.log.AppendText("与服务器连接成功。\n")
                    elif self.connect_flag == 1:
                        self.log.AppendText("已与服务器建立连接，请不要重复连接。\n")
                    else:
                        pass
                else:
                    self.log.AppendText('请输入正确端口号。\n')
            else:
                self.log.AppendText('请输入正确端口号。\n')
        else:
            self.log.AppendText('请输入正确IP地址。\n')

        event.Skip()

    def stopOnButtonClick(self, event):
        if self.connect_flag == 1:
            self.tcpCliSock.close()
            stop_thread(recv_thread)
            self.connect_flag = 0
            self.log.AppendText("已断开连接。\n")
            self.tcpCliSock = socket(AF_INET, SOCK_STREAM)
        else:
            self.log.AppendText("已断开连接，请不要重复操作。\n")
        event.Skip()



