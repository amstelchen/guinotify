# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0pre on Tue Apr 19 16:32:06 2022
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class ScriptDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ScriptDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize(wx.DLG_UNIT(self, wx.Size(200, 200)))
        self.SetTitle(_("dialog"))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_LEFT | wx.TE_WORDWRAP)
        self.text_ctrl_1.SetMinSize(wx.DLG_UNIT(self.text_ctrl_1, wx.Size(190, 190)))
        sizer_3.Add(self.text_ctrl_1, 0, wx.ALL, 10)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.AddButton(self.button_CANCEL)

        self.button_HELP = wx.Button(self, wx.ID_HELP, "")
        sizer_2.AddButton(self.button_HELP)

        sizer_2.Realize()

        self.panel_1.SetSizer(sizer_3)

        self.SetSizer(sizer_1)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())

        self.Layout()
        # end wxGlade

# end of class ScriptDialog
