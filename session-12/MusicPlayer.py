from PyQt5 import  QtWidgets
from PyQt5 import uic
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        self.volume=5
        super().__init__(*args, **kwargs)
        self.player = QMediaPlayer()
        uic.loadUi(
            "/Users/alireza/Desktop/pyadv-02/session-12/MusicPlayer.ui", self)
        pixmap = QPixmap('music/play.png')
        self.btn_play.setStyleSheet("""
            QPushButton {
                background-image: url('/Users/alireza/Desktop/pyadv-02/session-12/images/play.png');  /* Replace with your image path */
                background-repeat: no-repeat;
                background-position: center;
                border: none;  /* Remove default button border */
            }
        """)
        
        
        
        
        self.btn_play.clicked.connect(self.play_music)
        self.btn_stop.clicked.connect(self.stop_music)
        self.btn_v_up.clicked.connect(lambda: self.volume_changer(5))
        self.btn_v_down.clicked.connect(lambda: self.volume_changer(-5))
        self.btn_open.clicked.connect(self.open_music)


    def volume_changer(self,v):
        self.volume=self.volume+v
        self.player.setVolume(self.volume)
        print(self.volume)

    
    def stop_music(self):
        self.player.stop()
        
    def play_music(self):
        self.player.play()

    def open_music(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
                    self, 'Open Music File', '', 'Audio Files (*.mp3 *.wav)')
        if file:
            self.label_music.setText(file.split("/")[-1])
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(file)))



#self.slider_music.setVolume(x)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = MainWindow()
    w.show()
    app.exec()
