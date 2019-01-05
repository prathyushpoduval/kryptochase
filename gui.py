import sys
from PyQt4 import QtGui,QtCore, uic

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        #self.setGeometry(0, 0, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        uic.loadUi('cops.ui', self)
        self.home()

    def home(self):
        a='''
        screen = QtGui.QDesktopWidget().screenGeometry()
        SCREEN_HEIGHT=screen.height()
        SCREEN_WIDTH=screen.width()

        self.SCREEN_HEIGHT=screen.height()
        self.SCREEN_WIDTH=screen.width()

        #String Operators
        string_btn_h=SCREEN_HEIGHT/7 #height
        string_btn_w=3*SCREEN_WIDTH/16  #width
        string_btn_x=(SCREEN_WIDTH-4*string_btn_w)/5
        string_btn_y=0.93*SCREEN_HEIGHT-string_btn_h

        self.string_btn_h=SCREEN_HEIGHT/7 #height
        self.string_btn_w=3*SCREEN_WIDTH/16  #width
        self.string_btn_x=(SCREEN_WIDTH-4*string_btn_w)/5
        self.string_btn_y=0.93*SCREEN_HEIGHT-string_btn_h

        self.string_btn={}
        for i in range(4):
            self.string_btn[i]=QtGui.QPushButton("String Op "+str(i), self)
            self.string_btn[i].clicked.connect(self.string_operation(i))
            self.string_btn[i].resize(string_btn_w,string_btn_h)
            self.string_btn[i].move((i+1)*string_btn_x+i*string_btn_w, string_btn_y)
        '''

        self.showFullScreen()
        self.show()
'''
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.string_btn_x/2, self.string_btn_y-self.SCREEN_WIDTH/50, self.SCREEN_WIDTH-self.string_btn_x/2,self.string_btn_y-self.SCREEN_WIDTH/50)

    def string_operation(self,i):
        def func():
            print(i)
       return func
'''

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
print("h")
run()
