"""
view.py

Driver function that creates ARTView display.
"""
import os
import sys

from ..core import Variable, QtGui, QtCore
from ..components import RadarDisplay, Menu
from ._common import _add_all_advanced_tools, _parse_dir, _parse_field


def run(DirIn=None, filename=None, field=None):
    """
    artview execution for advanced IO display
    """
    DirIn = _parse_dir(DirIn)

    app = QtGui.QApplication(sys.argv)

    # start Menu and initiate Vradar
    menu = Menu(DirIn, filename=False, mode=(), name="Menu")
    Vradar = menu.Vradar

    field = _parse_field(Vradar.value, field)

    # start Displays
    from ..plugins import AdvancedIO
    view = AdvancedIO(DirIn)

    Vtilt = Variable(0)
    plot1 = RadarDisplay(view.Vradar, Variable(field), Vtilt, name="Display",
                         parent=menu)

    menu.addLayoutWidget(view)

    # add grafical starts
    _add_all_advanced_tools(menu)

    menu.setGeometry(0, 0, 700, 700)

    # start program
    app.exec_()
