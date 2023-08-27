from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
import sys, os
from PyQt5.QtGui import *
from asyncio import threads
import re 
from pathlib import Path
from subprocess import list2cmdline
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys
from time import sleep
import zipfile,os 
import subprocess
from selenium import webdriver

from random import choice 
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtGui 
import sys,os
import sys
from selenium import  webdriver  
from selenium.webdriver.common.by import By 
# pip install pyqt5, pip install pyqt5 tools
from PyQt5.QtWidgets import QApplication, QMainWindow
# just change the name
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
import time
import requests 
from PyQt5.QtWidgets import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PyQt5 import QtCore
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from phu import Ui_MainWindow
class UI(QMainWindow):
    """docstring for MainWindow"""
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("main.ui",self)
        self.setWindowTitle("Zumery")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.thread={}
        self.tabel_feed.setColumnWidth(0,537)
        self.tabel_feed.setColumnWidth(1,460)
        self.tabel_feed.setColumnWidth(2,100)

        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,120)
        self.tableWidget.setColumnWidth(2,120)
        self.tableWidget.setColumnWidth(4,120)
        self.tableWidget.setColumnWidth(5,263)
        self.tableWidget.setColumnWidth(6,100)
        self.tableWidget.setColumnWidth(7,120)
        self.QuanLyTk.clicked.connect(self.quanlytk)
        self.comen.clicked.connect(self.quanlycm)
        self.kb.clicked.connect(self.quanlykb)
        self.btn_show_feed.clicked.connect(self.show_view_feed)
        self.btn_show_home.clicked.connect(self.show_view_home)
        self.load_account()
        
        self.load_data_feed()
        self.show()

    #Chuyển màn hinh 
    def show_view_home(self):     
        self.listview.setCurrentWidget(self.home) 
    def show_view_feed(self):     
        self.listview.setCurrentWidget(self.Baidang)      
    # tải dữ liệu lên màn hình bài đăng 
    def load_data_feed(self):
        self.tabel_feed.setRowCount(0) 
        path='./data/feed.txt' 
        with open(path) as file:

            for line in file:
                print(line)
                if line != '':
                    try:
                         
                        content=line.split('|')[0]
                        try:
                            img =line.split('|')[1]
                        except:
                            img=""

                        
                    except:
                        pass      
                    row = self.tabel_feed.rowCount()
                    self.tabel_feed.insertRow(row)
                    item = QTableWidgetItem(content) # create the item
                    item.setTextAlignment(Qt.AlignCenter)                
                    self.tabel_feed.setItem(row, 0, QtWidgets.QTableWidgetItem(content))
                    self.tabel_feed.setItem(row, 1, QtWidgets.QTableWidgetItem(img))
                    btn_remote_feed=QPushButton('Xóa')
                    btn_remote_feed.setStyleSheet("""
                            QPushButton{
                                background-color: rgb(255, 0, 0);
                            }
                            QPushButton:hover{
                                color:#fff;  
                                background-color: rgb(0, 255, 255);
                            }
                        """)
                    btn_remote_feed.clicked.connect(self.remote_feed)
                    self.tabel_feed.setCellWidget(row,2,btn_remote_feed)            
    def remote_feed(self):
       button=self.sender()
       index=self.tabel_feed.indexAt(button.pos())
       path='./data/feed.txt' 
       
       if index.isValid():
           row=index.row()
           with open(path, "r+") as f:
                data_feed = f.readlines()
                f.close()
           with open(path, "w") as f:
               for i in data_feed:
                   if i != data_feed[row]:
                       f.write(i)
           f.close()
           self.load_data_feed()                

    def quanlykb(self):
        self.add=QMainWindow()
        self.uic2=Ui_MainWindow()
        self.uic2.setupUi(self.add)
        path='./data/kb.txt'
        try: 
            with open(path,encoding='UTF-8') as f:
                datalist = f.read() 
                data  = datalist[0].strip()
                print(data)
                self.uic2.plainTextEdit.setPlainText(datalist)
        except: 
            f =open(path,'a+')
        self.uic2.save.clicked.connect(self.Save_kb)
        self.add.show()
    def Save_kb(self,):
        
        path='./data/kb.txt'

        data  = self.uic2.plainTextEdit.toPlainText()
        f=open(path,'w',encoding='UTF-8')
        f.write(data)
        f.close()
        self.uic2.save.setEnabled(False)
    #quản lý comment 
    def quanlycm(self):
        self.add=QMainWindow()
        self.uic1=Ui_MainWindow()
        self.uic1.setupUi(self.add)
        path='./data/comen.txt'
        try: 
            with open(path,encoding='UTF-8') as f:
                datalist = f.read() 
                data  = datalist[0].strip()
                print(data)
                self.uic1.plainTextEdit.setPlainText(datalist)
        except: 
            f =open(path,'a+')
        self.uic1.save.clicked.connect(self.Save_come)
        self.add.show()
    def Save_come(self,):
        
        path='./data/comen.txt'

        data  = self.uic1.plainTextEdit.toPlainText()
        f=open(path,'w',encoding='UTF-8')
        f.write(data)
        f.close()
        self.uic1.save.setEnabled(False)
    def quanlytk(self):
        self.add=QMainWindow()
        self.uic5=Ui_MainWindow()
        self.uic5.setupUi(self.add)
        path='./data/accout.txt'
        try: 
            with open(path,encoding='UTF-8') as f:
                datalist = f.read() 
                data  = datalist[0].strip()
                print(data)
                self.uic5.plainTextEdit.setPlainText(datalist)
        except: 
            f =open(path,'a+')
        self.uic5.save.clicked.connect(self.Save_Tk)
        self.add.show()
    def Save_Tk(self,):
        
        path='./data/accout.txt'

        data  = self.uic5.plainTextEdit.toPlainText()
        f=open(path,'w',encoding='UTF-8')
        f.write(data)
        f.close()
        self.uic5.save.setEnabled(False)
        self.load_account()
    def load_account(self):

        self.tableWidget.setRowCount(0) 
        path='./data/accout.txt' 
        with open(path) as file:

            for line in file:
                print(line)
                if line != []:
                    try:
                         
                        id=line.split('|')[0]
                        mk=line.split('|')[1]
                        try:
                            fa =line.split('|')[2]
                        except:
                            fa=""

                        try:
                            proxy=line.split('|')[3]
                        except:
                            proxy="105.214.80.151:5678"
                    except:
                        pass      
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    item = QTableWidgetItem(id) # create the item
                    item.setTextAlignment(Qt.AlignCenter)
                    
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(id))
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(mk))
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(fa))
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(proxy))
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(''))
                    self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(''))
                    
                    btn=QPushButton('Chạy')
                    btn.clicked.connect(self.star)
                    self.tableWidget.setCellWidget(row,6,btn)
                    item = QTableWidgetItem('OFF') # create the item
                    item.setTextAlignment(Qt.AlignCenter)
                    
                    self.tableWidget.setItem(row,7,item)
    def star(self):
        button=self.sender()
        index=self.tableWidget.indexAt(button.pos())
        if index.isValid():
            row=index.row()
            tn=QPushButton('Dừng')
            tn.clicked.connect(self.dung)
            self.tableWidget.setCellWidget(row,6,tn)
            self.upxanh(row)
            
            getid=self.tableWidget.item(row,0)
            id=getid.text()
            getpasword=self.tableWidget.item(row,1)
            password=getpasword.text()
            getfa1=self.tableWidget.item(row,2)
            fa1=getfa1.text()
            item = QTableWidgetItem('ON') # create the item
            item.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(row,7,item)
            self.upxanh(row)
            self.thread[row]=multi_thread(indexx=row,id=id,password=password,fa1=fa1)
            self.thread[row].start()
            self.thread[row].signal.connect(self.load_show)
        
           
    
            
    def dung(self):
        button=self.sender()
        index=self.tableWidget.indexAt(button.pos())
        if index.isValid():
            row=index.row()
            btn=QPushButton('Chạy')
            btn.clicked.connect(self.star)
            self.tableWidget.setCellWidget(row,6,btn)
            self.uptrang(row)        
            item = QTableWidgetItem('OFF') # create the item
            item.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(row,7,item)
            self.thread[row].stop()
    def upxanh(self,row):
        for i in range(8):
            try:
                self.tableWidget.item(row,i).setBackground(QtGui.QColor(85,255,0))
          
            except:
                pass            
           #  self.tableWidget.item(row,i).setBackground(QtGui.QColor(255,255,255)) 
    def uptrang(self,row):
        for i in range(8):
            try:
                self.tableWidget.item(row,i).setBackground(QtGui.QColor(255,255,255))    
            except:
                pass 
    def load_show(self,indexx,th):
        if th=="Hoàn Tất":
            self.tableWidget.setItem(indexx,5,QTableWidgetItem(str(th)))
            self.uptrang(indexx)
            
            btn=QPushButton('Chạy')
            btn.clicked.connect(self.star)
            item = QTableWidgetItem('OFF') # create the item
            item.setTextAlignment(Qt.AlignCenter)
                    
            self.tableWidget.setItem(indexx,7,item)

            self.tableWidget.setCellWidget(indexx,6,btn)
        else:
            self.tableWidget.setItem(indexx,5,QTableWidgetItem(str(th)))
            self.upxanh(indexx)


        

class multi_thread(QThread):
    signal=pyqtSignal(object,object)
    

    ipp=pyqtSignal(object,object)
    def __init__(self,indexx,id,password,fa1):
        super(multi_thread,self).__init__()
        self.index=indexx
        self.id=id 
        self.password=password
        self.fa1=fa1
    def get_chromedriver(self,mypath):
        
        chrome_options = webdriver.ChromeOptions()
        
        chrome_options.add_argument('user-data-dir='+mypath)
        chrome_options.add_argument("--window-size=400,600")
            
            
            
            
        driver = webdriver.Chrome(options=chrome_options)
    

        return driver
    def send(self,driver,path,keys):
        for i in keys:  
            driver.find_element(By.ID,path).send_keys(i)
            time.sleep(0.25) 
    def send_xpath(self,driver,path,keys):
        for i in keys:  
            driver.find_element(By.XPATH,path).send_keys(i)
            time.sleep(0.25)
    def click_xpath(self,driver,path):
         driver.find_element(By.XPATH,path).click()      
    def Login(self,driver,id,password,fa1):
        th='đang tiến hành đăng nhập'
        self.signal.emit(self.index,th)
        path='//*[@id="m_login_email"]'
        key=self.id 
        self.send_xpath(driver,path,key)
        path='//*[@id="password_input_with_placeholder"]/input'
        key=self.password 
        self.send_xpath(driver,path,key)
        path='login'
        driver.find_element(By.NAME,path).click()
        key=requests.get(f'https://2fa.live/tok/{fa1}').json()['token']    
        path='//*[@id="approvals_code"]'
        self.send_xpath(driver,path,key)
        path='//*[@id="checkpointSubmitButton"]'
        self.click_xpath(driver,path)
        path='//*[@id="checkpointSubmitButton"]'
        self.click_xpath(driver,path)
    def run(self):

       print(self.id)
       path='.\\profileChrome\\'+str(self.id)
       mypath =str(Path().absolute())+'\\profileChrome\\'+str(self.id)

       driver = self.get_chromedriver(mypath)
       self.driver=driver
       driver.get('https://mbasic.facebook.com/')
       sleep(5)
       th=f'Đã nhắn tin lần '
       self.signal.emit(self.index,th)
       try:
        self.Login(driver,self.id,self.password,self.fa1)
       except:
        th='Đã đăng nhập'
        self.signal.emit(self.index,th)
       # Mở tệp để đọc
       with open('./data/kb.txt', 'r',encoding='UTF-8') as file:
        for line in file:
            th='Đang tải lên bài viết'
            self.signal.emit(self.index,th)
            path='//*[@id="mbasic-composer-form"]/table/tbody/tr/td[2]/div/textarea'
            key=(line.strip())
            self.send_xpath(driver,path,key)
            sleep(5)
            path='//*[@id="mbasic-composer-form"]/table/tbody/tr/td[3]/div/input'
            self.click_xpath(driver,path)
            driver.get('https://mbasic.facebook.com/')
            th='Đã tải lên bài viết'
            self.signal.emit(self.index,th)

            delay=int(15)
            for x in range(delay, -1, -1):
                th=f'Tiếp Tục Sau {x} Giây '
                self.signal.emit(self.index,th)
                sleep(1)
        th="Hoàn Tất"
        self.signal.emit(self.index,th)
        self.driver.quit()
    def stop(self):
        self.terminate()
        th="Đã dừng tác vụ"
        try:
            self.driver.quit()
        except:
            pass
        self.signal.emit(self.index,th)
    

    
    
 
       


      
                 

       
       
app =QApplication(sys.argv)
UIWindow=UI()
app.exec_()
        
        