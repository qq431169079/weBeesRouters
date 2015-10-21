# -*- coding: utf-8 -*-
# This Class contains all the UI/View definitions
# that are going to be used during the work of the app.
from PyQt4.QtGui import QDialog, QPalette, QFont, QLabel, QComboBox, \
    QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QPainter, QColor, QFrame
from PyQt4.QtCore import Qt

from view_defs import general_defs, reg_defs


class View(QDialog):

    def __init__(self):
        super(View, self).__init__()
        ##########################
        # Start global definitions
        ##########################
        self.setLayoutDirection(Qt.RightToLeft)
        self.grid = QGridLayout()

        hpalette = QPalette()  # Header Palette
        lpalette = QPalette()  # simple label Palette
        bpalette = QPalette()  # button Palette
        bgpalette = QPalette()  # background Palette

        hpalette.setColor(QPalette.WindowText, QColor("#6F3662") )  # Header Color

        lpalette.setColor(QPalette.WindowText, QColor("#74828F"))  # labels color
        lpalette.setColor(QPalette.Window, QColor("#DDDDDD"))  # labels color

        bpalette.setColor(QPalette.ButtonText, QColor("#6F3662"))  # button text color
        bpalette.setColor(QPalette.Button, QColor("#6F3662"))      # button background color
        # bgpalette.setColor(QPalette.Window, QColor("#F8F8F8"))     # background color

        self.palettes = dict()
        self.palettes['header'] = hpalette
        self.palettes['button'] = bpalette
        self.palettes['label'] = lpalette
        self.palettes['support'] = lpalette
        self.palettes['bg'] = bgpalette

        self.label_types = dict()
        self.label_types['label'] = QFont(general_defs['_font'], general_defs['label_font_size'])
        self.label_types['button'] = QFont(general_defs['_font'], general_defs['button_font_size'])
        self.label_types['support'] = QFont(general_defs['_font'], general_defs['support_font_size'])
        self.label_types['header'] = QFont(general_defs['_font'], general_defs['header_font_size'], QFont.Bold)
        ##########################
        # End global definitions
        ##########################

        self.support_label = self.create_qlabel(general_defs['en_support'], 'support')

    def create_qlabel(self, string_to_label, wtype='label'):
        # label_type can be label, button  or header, support

        qlbl = QLabel(string_to_label)
        qlbl.setFont(self.label_types[wtype])
        qlbl.setPalette(self.palettes[wtype])
        if string_to_label == ".":
            qlbl.setFixedWidth(15)
        return qlbl

    def create_label_as_bg(self):
        """
        a method for creating label as beckground for frame
        and highlighting manipulations.
        :return:
        """
        l = QLabel()
        # l.setFrameShape(QFrame.Panel)
        # l.setFrameShadow(QFrame.Sunken)
        # l.setFrameStyle(1)
        l.setPalette(self.palettes['label'])
        l.setAutoFillBackground(True)
        return l

    def create_combobox(self):
        comboboxMinWidth = 200
        cb = QComboBox()
        cb.setMinimumWidth(comboboxMinWidth)
        cb.setAutoFillBackground(True)
        return cb

    def create_octet(self):
        octet = QLineEdit()
        octet.setMaxLength(3)
        octet.setMaximumWidth(30)
        # octet.setPlaceholderText('0')
        return octet

    def create_button(self, btn_label):
        b = QPushButton(btn_label)
        b.setFont(self.label_types['button'])
        b.setPalette(self.palettes['button'])
        b.setAutoFillBackground(True)
        return b

    def create_ip_style_group(self, groupName):

        group = dict()
        group['name'] = self.create_qlabel(groupName)
        group['octet1'] = self.create_octet()
        group['octet2'] = self.create_octet()
        group['octet3'] = self.create_octet()
        group['octet4'] = self.create_octet()

        group['dotLbl1'] = self.create_qlabel(reg_defs['dot'])
        group['dotLbl2'] = self.create_qlabel(reg_defs['dot'])
        group['dotLbl3'] = self.create_qlabel(reg_defs['dot'])

        group['grid'] = QGridLayout()
        name_h_box = QHBoxLayout()
        h_box = QHBoxLayout()

        group['grid'].addLayout(name_h_box, 0, 0)
        group['grid'].addLayout(h_box, 0, 1)

        name_h_box.addWidget(group['name'])
        h_box.addWidget(group['octet1'])
        h_box.addWidget(group['dotLbl1'])
        h_box.addWidget(group['octet2'])
        h_box.addWidget(group['dotLbl2'])
        h_box.addWidget(group['octet3'])
        h_box.addWidget(group['dotLbl3'])
        h_box.addWidget(group['octet4'])

        return group

