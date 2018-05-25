# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(1200, 700))

        text = wx.StaticText(self, -1, '스토어팜 소비자 반응 워드클라우드 && 단어 빈도 차트', (20, 20))
        text.SetFont( wx.Font( 26, 72, 90, 90, False, "HY수평선M" ) )

        panel = wx.Panel(self, -1, (20, 150), (550, 400),  style=wx.SUNKEN_BORDER)
        self.picture = wx.StaticBitmap(panel)
        panel.SetBackgroundColour(wx.WHITE)

        panel2 = wx.Panel(self, -1, (600, 150), (550, 400), style=wx.SUNKEN_BORDER)
        self.picture2 = wx.StaticBitmap(panel2)
        panel2.SetBackgroundColour(wx.WHITE)

        self.images = ['Chrysanthemum.jpg', 'feuchtwanger.jpg', 'balzac.jpg', 'pasternak.jpg']
        self.images2 = ['Desert.jpg', 'feuchtwanger.jpg', 'balzac.jpg', 'pasternak.jpg']
        authors = ['전체', '만족', '보통', '불만' ]


        wx.ComboBox(self, -1, pos=(20, 80), size=(100, -1), choices=authors, style=wx.CB_READONLY)
        wx.Button(self, 1, 'View', (140, 80))

        self.Bind(wx.EVT_BUTTON, self.OnSelect)


        self.Centre()

    def OnSelect(self, event):
        item = event.GetSelection()
        self.picture.SetFocus()
        self.picture.SetBitmap(wx.Bitmap('C:/untitled/' + self.images[item]))
        self.picture2.SetFocus()
        self.picture2.SetBitmap(wx.Bitmap('C:/untitled/' + self.images2[item]))

class MyApp(wx.App):
    def OnInit(self):
        dlg = MyDialog(None, -1, '워드클라우드')
        dlg.ShowModal()
        dlg.Destroy()
        return True

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()