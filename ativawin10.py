import sys
import os

from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QLabel

 
class Window(QWidget):

    def home1(janela):
        if janela.radio.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99 && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio2.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio3.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio4.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio5.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio6.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk MH37W-N47XK-V7XM9-C7227-GCQG9 && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio7.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43 && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio8.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4 && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio9.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2 && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio10.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio11.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk WNMTR-4C88C-JK8YV-HQ7T2-76DF9 && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio12.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk 2F77B-TNFGY-69QQF-B8YKP-D69TJ && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')
            
        elif janela.radio13.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk DCPHK-NFMTC-H88MJ-PFHPY-QJ4BJ && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

        elif janela.radio14.isChecked():
            os.system('slmgr/dlv && slmgr/upk && cscript slmgr.vbs /ipk QFFDN-GRT3P-VKWWX-X7T3R-8B639 && cscript slmgr.vbs /skms kms.lotro.cc && cscript slmgr.vbs /ato')

    def opc1(janela):

        janela.label = QLabel("Windows 10 Ativador",janela)
        janela.label.move(110, 10)
        janela.label.setStyleSheet('font-size:30px')

        janela.radio = QRadioButton("HOME", janela)
        janela.radio.move(10, 100)

        janela.radio2 = QRadioButton("HOME(Country Specific)", janela)
        janela.radio2.move(10, 150)

        janela.radio3 = QRadioButton("HOME(Single Language)", janela)
        janela.radio3.move(10, 200)

        janela.radio4 = QRadioButton("HOME N", janela)
        janela.radio4.move(10, 250)

        janela.radio5 = QRadioButton("PRO", janela)
        janela.radio5.move(180, 100)

        janela.radio6 = QRadioButton("PRO N", janela)
        janela.radio6.move(180, 150)

        janela.radio7 = QRadioButton("Enterprise", janela)
        janela.radio7.move(260, 100)

        janela.radio8 = QRadioButton("Enterprise N", janela)
        janela.radio8.move(260, 150)

        janela.radio9 = QRadioButton("2015 LTSB", janela)
        janela.radio9.move(260, 200)
        
        janela.radio10 = QRadioButton("2015 LTSB N", janela)
        janela.radio10.move(260, 250)

        janela.radio11 = QRadioButton("2016 LTSB", janela)
        janela.radio11.move(260, 300)

        janela.radio12 = QRadioButton("2016 LTSB N", janela)
        janela.radio12.move(260, 350)

        janela.radio13 = QRadioButton("EDUCATION", janela)
        janela.radio13.move(360, 100)

        janela.radio14 = QRadioButton("EDUCATION N", janela)
        janela.radio14.move(360, 150)

        janela.btn1 = QPushButton("ATIVAR",janela)
        janela.btn1.setGeometry(210, 450, 80, 40)
        janela.btn1.setStyleSheet('background-color:BLACK; color:red')#background
        janela.btn1.clicked.connect(janela.home1)

    def __init__(janela):
        super().__init__()
        janela.resize(500, 500)
        janela.setWindowTitle("Ativador Windows10")
        janela.opc1()
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())