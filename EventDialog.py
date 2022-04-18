# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0pre on Mon Apr 18 14:49:03 2022
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class EventDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: EventDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize(wx.DLG_UNIT(self, wx.Size(150, 100)))
        self.SetTitle(_("dialog"))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        self.check_list_box_1 = wx.CheckListBox(self.panel_1, wx.ID_ANY, choices=[_("choice 1")])
        self.check_list_box_1.SetMinSize(wx.DLG_UNIT(self.check_list_box_1, wx.Size(120, 80)))
        sizer_3.Add(self.check_list_box_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.AddButton(self.button_CANCEL)

        sizer_2.Realize()

        self.panel_1.SetSizer(sizer_3)

        self.SetSizer(sizer_1)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())

        self.Layout()
        # end wxGlade

# end of class EventDialog
