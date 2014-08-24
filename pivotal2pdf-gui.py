import sys
import os
from pivotal2pdf import main as pivotal2pdf
from PyQt5.QtWidgets import QApplication, QFileDialog


def startfile(filename):
    if sys.platform == 'win32':
        os.startfile(filename)
    elif sys.platform.startswith('linux'):
        os.system('xdg-open %s' % filename)
    else:
        os.system('open %s' % filename)


def main():
    app = QApplication(sys.argv)
    dialog = QFileDialog()
    dialog.setNameFilter('Pivotal Tracker stories (*.csv)')
    if dialog.exec_():
        csv_file = dialog.selectedFiles()[0]
        sys.argv.append(csv_file)
        pdf_file = pivotal2pdf()
        startfile(pdf_file)


if __name__ == '__main__':
	main()
