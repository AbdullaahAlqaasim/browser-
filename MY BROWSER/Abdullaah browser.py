
"""
browser implementation by ABDULLAAH ALQAASIM
 
Linked in  @abdullaah alqaasim :  
Instagram @abdullaah_alqaasim: https://www.instagram.com/abdullaah_alqaasim/ 
Github: https://github.com/AbdullaahAlqaasim 

youtube : 
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        self.setWindowTitle('Abdullaah Alqaasim Browser')
   

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        linkedin_btn = QAction('linked in', self)
        linkedin_btn.triggered.connect(self.linkdin_btn)
        navbar.addAction(linkedin_btn)

        instagram_btn = QAction('instagram', self)
        instagram_btn.triggered.connect(self.instagram_btn)
        navbar.addAction(instagram_btn)

        github_btn = QAction('github', self)
        github_btn.triggered.connect(self.github_btn)
        navbar.addAction(github_btn)


        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def linkdin_btn(self):
        self.browser.setUrl(QUrl('https://www.linkedin.com/in/abdullaah-alqaasim-30b960209/')) 

    def instagram_btn(self):
        self.browser.setUrl(QUrl('https://www.instagram.com/abdullaah_alqaasim/'))  

    def github_btn(self):
        self.browser.setUrl(QUrl('https://github.com/AbdullaahAlqaasim'))      
       
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('ABDULLAAH ALQAASIM BROWSER')
window = MainWindow()
app.exec_()

#pip install PyQtWebEngine
# pip install PyQt5
