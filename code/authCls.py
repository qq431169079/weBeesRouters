# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import logging

from viewCls import View
from sqlCls import SqlFunctions
from view_defs import auth_defs, general_defs, qt_v_defs

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=general_defs['_logging_level'])


class MyPopupDialog(View):
    def __init__(self, error_msg):
        super(MyPopupDialog, self).__init__()
        logging.error(error_msg)
        err_label = QLabel(error_msg)
        self.close_btn = QPushButton(auth_defs['h_close_popup'])
        self.setWindowTitle(auth_defs['h_error_msg'])
        self.setMinimumWidth(general_defs['popup_window_min_width'])
        grid = QGridLayout()
        grid.addWidget(err_label)
        grid.addWidget(self.close_btn)
        self.setLayout(grid)
        # set button event handler
        self.connect(self.close_btn, SIGNAL("clicked ()"), self.close_popup)

    def close_popup(self):
        self.accept()


class ViewAuthForm (View):
    """
    # err_msgs_inst is a ErrorMsgs instance
    # with which i can pull any type of
    # error message that is written in the program XML
    # according to its type (authentication ,license,...)
    """
    def __init__(self):
        super(ViewAuthForm, self).__init__()

        # Header
        header_label = self.create_qlabel(auth_defs['h_auth_header'], 'header')
        # username group
        self.username_group = self.create_label_lineedit_pair(auth_defs['h_username'])
        # password group
        self.password_group = self.create_label_lineedit_pair(auth_defs['h_password'])

        # button for authentication
        self.auth_btn = self.create_button(auth_defs['h_login'])
        # set the widgets on the layout
        form_grid = QGridLayout()
        self.grid.addLayout(form_grid,0,0,1,2, qt_v_defs['align_r'])  # insert the form grid to the main grid
        form_grid.addWidget(header_label, 0, 0, qt_v_defs['align_r'])  # add Gui Header
        form_grid.addWidget(self.username_group['label'], 1, 0, qt_v_defs['align_r'])  # add username label to grid
        form_grid.addWidget(self.username_group['value'], 1, 1, qt_v_defs['align_r'])  # add username textbox to grid
        form_grid.addWidget(self.password_group['label'], 2, 0, qt_v_defs['align_r'])  # add password label to grid
        form_grid.addWidget(self.password_group['value'], 2, 1, qt_v_defs['align_r'])  # add password textbox to grid
        self.grid.addWidget(self.img_label,0, 2, qt_v_defs['align_l']) # add webees icon on the left
        self.grid.addWidget(self.auth_btn, 1, 1)  # add login button to the grid
        self.grid.addWidget(self.support_label, 2, 2)  # add support label at the left bottom corner
        self.setLayout(self.grid)  # "close" grid

    def create_label_lineedit_pair(self, groupName):
        """
        This method is for creating a group like the one showing the router name
        Recognized automatically
        :param groupName: the
        :return: two horizontal labels and the second is styled
        """
        group = dict()
        group['label'] = self.create_qlabel(groupName)
        group['value'] = QLineEdit("")

        return group


# Here starts the Auth Controller Class definition
class CtrlAuthForm(ViewAuthForm, SqlFunctions):
    """
    # err_msgs_inst is a ErrorMsgs instance
    # with which i can pull any type of
    # error message that is written in the program XML
    # according to its type (authentication ,license,...)
    """
    def __init__(self,  err_msgs_inst):
        super(CtrlAuthForm, self).__init__()
        SqlFunctions.__init__(self)
        ViewAuthForm.__init__(self)
        self._err_msgs_inst = err_msgs_inst
        self._uName = ""
        self._uNameIndex = "NA"
        # just for testing i can set the values for the user
        self.username_group['value'].setText(QString('BeeComm'))
        self.password_group['value'].setText(QString('beecomm13'))
        # self.username_group['value'].setText(QString('Retalix'))
        # self.password_group['value'].setText(QString('Retalix1'))

        # set the login button event handler
        self.connect(self.auth_btn, SIGNAL("clicked ()"), self.authenticate)

    def authenticate(self):
        # a method for handling the login button click event
        # _username = self.username_group['value'].text()
        # _password = self.password_group['value'].text()
        # if its ok data is username
        # if not ,data is an error msg to pass to popup window
        __auth_result, data = self.getUserId(unicode(self.username_group['value'].text()),
                                             unicode(self.password_group['value'].text()))
        if __auth_result == "err":
            _dialog = MyPopupDialog(self._err_msgs_inst.get_error_msg("Authentication"))
            _dialog.exec_()
        else:
            self.set_u_name(data)
            self.set_u_name_index(__auth_result)
            self.accept()

    def get_u_name(self):
        return self._uName

    def set_u_name(self, val):
        self._uName = val

    def get_u_name_index(self):
        return self._uNameIndex

    def set_u_name_index(self, val):
        self._uNameIndex = val