
	# kivy package
from android.permissions import request_permissions, Permission
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])	
import kivy
from kivy.app import App
from kivy.lang import  Builder
from kivy.uix.screenmanager import  ScreenManager,Screen
from kivy.metrics import dp
from kivy.clock import  Clock,mainthread
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.core.window import Window
from kivy.animation import Animation,AnimationTransition
from kivy.properties import NumericProperty,ObjectProperty,StringProperty
from kivy.factory import Factory
from kivy.base import EventLoop
from kivy.uix.scrollview import ScrollView
		  
		# kivymd package
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivy.uix.filechooser import  FileChooserIconView
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image,AsyncImage
from kivymd.toast import  toast
from kivymd.uix.button import MDIconButton,MDFlatButton,MDRaisedButton,MDFloatingActionButton
from kivymd.uix.bottomsheet import  MDGridBottomSheet
from kivymd.uix.dialog import  MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.spinner import MDSpinner
from kivymd.utils import asynckivy
from kivymd.uix.picker import *
from kivymd.theming import ThemeManager
from kivymd.uix.imagelist import SmartTileWithStar
		# Requied package


import json
import  requests

import os
import  threading 
from jnius import cast
from jnius import autoclass
try:
	from firebase_admin import credentials, storage
	import  pyrebase
	import firebase_admin
	from PIL import Image 
except:
	exc_type,exc_value,exc_traceback=sys.exc_info()
	with open('/storage/emulated/0/error_module.txt','a+') as f:			
		f.write(f'{exc_type}\n{exc_value}\n{exc_traceback}')
	
		
		
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"

file=''
user_mail=''

class IconToggleButton(ToggleButtonBehavior, MDIconButton):
	def __init__(self, **kwargs):
		super(IconToggleButton, self).__init__()

#Reward Screen
class Reward_Screen(Screen):
	def back(self):
		self.manager.current='main_screen'


#Help Screen	
class Help_Screen(Screen):
	def back_main(self):
		self.manager.current='main_screen' 	

# about screen
class About_Screen(Screen):
    #gif animation
    def on_enter(self):
        self.ids.gif.anim_delay = 0.10
        self.ids.gif._coreimage.anim_reset(True)

    def __init__(self,**kwargs):
        super(About_Screen,self).__init__(**kwargs)
            #code goes here and add:
        Window.bind(on_keyboard=self.Android_back_click)

    def Android_back_click(self,window,key,*largs):
        if key == 27:
            self.manager.current='main_screen' #you can create a method here to cache in a list the number of screens and then pop the last visited screen.
            return True

                
                        
    def facebook(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.renpy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://www.facebook.com/anupam.kayal.146'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open() 
    def whatsapp(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.renpy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://wa.me/919163742623'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
    def gmail(self):
        self.dialog = MDDialog(title='Info',text='anupamkayal35@gmail.com',buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
        self.dialog.open()      
                 
    def youtube(self):
        toast('please wait..')
        try:          
            # import the needed Java class
            PythonActivity = autoclass('org.renpy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            Uri = autoclass('android.net.Uri')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_VIEW)
            intent.setData(Uri.parse('https://youtube.com/channel/UCnYwAFxj9LjaZewOrcIZGxg'))
            # PythonActivity.mActivity is the instance of the current Activity
            # BUT, startActivity is a method from the Activity class, not from our PythonActivity.
            # We need to cast our class into an activity and use it
            currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
            currentActivity.startActivity(intent)
        except Exception as excpet:
            self.dialog = MDDialog(title='Error',text=str(excpet),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()
                                                
            
    def back_main(self):
        self.manager.current='main_screen'
        
                
                                
# upload screen
class Upload_Screen(Screen):
    upload_complete=False
    def __init__(self,**kwargs):
        super(Upload_Screen,self).__init__(**kwargs)
            #code goes here and add:
        Window.bind(on_keyboard=self.Android_back_click)

    def Android_back_click(self,window,key,*largs):
        if key == 27:
            self.manager.current='main_screen'#you can create a method here to cache in a list the number of screens and then pop the last visited screen.
            return True
 
                   
                                                 
   
        
    def show_selected_img(self,path):
        toast(path)
        global file
        file=path
        # update label
        self.manager.get_screen('upload_screen').ids.label.text =str(path)
        self.manager.get_screen('upload_screen').ids.label.font_size=dp(7)       
       # update image
        self.manager.get_screen('upload_screen').ids.upload_btn.background_normal=(path)
        self.manager.get_screen('upload_screen').ids.upload_btn.background_down=(path)
    def processing_func(self):     
        self.submit_btn=self.manager.get_screen('upload_screen').ids.upload_submitbtn
        self.submit_btn.disabled=True
        threading.Thread(target=self.upload,daemon=True).start()
        
 
    def upload(self):
        
        if self.manager.get_screen('account_screen').ids.name_text.text=='guest':
            self.ids.loadingbar.active=False
            Snackbar(text='please create an account').show()
        else:
             
            try:
                self.manager.get_screen('upload_screen').ids.loadingbar.active=True
                self.manager.get_screen('upload_screen').ids.loadingbar.opacity=1                                                           
                toast('uploading')                         
                img_file=file
                if not firebase_admin._apps:
                    cred=credentials.Certificate('serviceAccountKey.json')
                    firebase_admin.initialize_app(cred, {'storageBucket': "database-kivy.appspot.com"})       
                bucket = storage.bucket()
                file2=os.path.basename(img_file)                                        
                blob = bucket.blob(str(user_mail)+'/'+str(file2))
                blob.upload_from_filename(img_file)
                blob.make_public()    
    #here I'd like to have url of file I uploaded      
                img_url=(blob.public_url)
               
    #here append url in main.txt
                with open('main.txt','a+') as url_img:
                    url_img.seek(0)
                    data = url_img.read(2)
                    if len(data) >= 0:
                        url_img.write("\n")                        
                        url_img.write(img_url)
                      
                    else:
                        url_img.write(img_url)
                
                              
                blob1=bucket.delete_blob('main.txt')        
                blob2=bucket.blob('main.txt')
                blob2.upload_from_filename('main.txt')            
                self.ids.loadingbar.active=False
                self.manager.get_screen('upload_screen').ids.loadingbar.opacity=0                                                         
                toast('upload successfull')
                # Terminate the process                      
                self.ids.label.text='No file chosen'                
                self.ids.label.font_size=dp(20)
                self.ids.upload_btn.background_normal="upload img.png"
                self.ids.upload_btn.background_down="upload img.png"
                self.submit_btn.disabled=False
                self.manager.get_screen('upload_screen').ids.loadingbar.active=False                         
                Upload_Screen.upload_complete=True
                print(Upload_Screen.upload_complete)
                   
            except Exception as excep:                
                self.dialog = MDDialog(title='Error',text=str(excep),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss=False )
                self.dialog.open()
                print(excep)
                self.ids.loadingbar.active=False
                stop = threading.Event()               
                stop.set()             
                                            
    def screen_back(self):
        if Upload_Screen.upload_complete==True:
            self.ids.upload_btn.background_normal="upload img.png"
            self.ids.upload_btn.background_down="upload img.png"
            self.manager.get_screen('upload_screen').ids.loadingbar.opacity=0                       
           
        else:
            pass
        self.manager.current='main_screen'
         
        
       
# Filemanager Screen
class  Filemanager_Screen(Screen):
   
    def on_enter(self):
        self.manager_open = True
        Window.bind(on_keyboard=self.events)

         
    def on_leave(self):
        self.manager_open=False  
    def select(self,*args):
         try:
             self.file=(args[1][0] )          
             self.manager.current='upload_screen'
             self.manager_open=False
             Upload_Screen.show_selected_img(self,path=self.file)            
         except:
             pass
    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.manager.current='upload_screen'
        return True   
               
# account screen
class Account_Screen(Screen):

    def on_pre_enter(self):
        self.upload_back=True
        Window.bind(on_keyboard=self.event)  
        
    def event(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.upload_back==True:
                 self.manager.current='main_screen'                   
        return True
    def on_leave(self):
        self.upload_back=False
        if self.btn:
            self.btn.cancel(self.ids.action_btn)
                                              
  
#---------MDFileManager--------
    def on_enter(self):        
        self.manager_open = False
        Window.bind(on_keyboard=self.events)
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,            
        )
       
        #self.ids.action_btn.pos=(self.edit_btn_pos[0],self.edit_btn_pos[1])            
        print(self.ids.action_btn.pos)  
        self.animate_btn_up()
        self.anim(self.ids.first_layout)
        self.anim1(self.ids.second_layout)
        self.anim2(self.ids.third_layout)
        self.anim3(self.ids.forth_layout)
        
                 

#---------- canvas annimation-------------              
    def anim(self,widget):
        animation=Animation(pos_hint={'center_y':1.18,'center_x':0.8},duration=1)
        animation.start(widget)
    def anim1(self,widget):
        animation=Animation(pos_hint={'center_y':0.9,'center_x':0.7})
        animation.start(widget)
    def anim2(self,widget):    	
    	animation=Animation(pos_hint={'center_y':0.96,'center_x':0.75})
    	animation.start(widget)
    def anim3(self,widget):    	
    	animation=Animation(pos_hint={'center_y':0.98,'center_x':0.75})
    	animation.start(widget)	
#--------------------MDFileManager--------------
    	
    def file_manager_open(self):
        if self.manager.get_screen('account_screen').ids.name_text.text=='guest':      
            self.dialog = MDDialog(title='Error',text='Please create an account',buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False  )
            self.dialog.open()           
        else:
            self.file_manager.show('/storage/emulated/0')  # output manager to the screen   
            self.manager_open = True
                       
    def select_path(self, path):      
        self.exit_manager()
        selected_file=(os.path.basename(path))
        file_stats = os.stat(path)
        file_size=(file_stats.st_size / (1024 * 1024))
        if file_size >=1.0:           
            file_list=selected_file.split('.')
            image = Image.open(path)   
            MAX_SIZE = (500, 500) 
            image.thumbnail(MAX_SIZE)  
           # creating thumbnail
           #os.remove('/storage/emulated/0/DCIM/pythonthumb.png')
            image.save('./'+str(file_list[0])+'.png')
            self.manager.get_screen('main_screen').ids.nav_draw_img.source='./'+str(file_list[0])+'.png'
            toast(selected_file)
            Clock.schedule_once(self.profile_pic,2)   
        else:
            self.manager.get_screen('main_screen').ids.nav_draw_img.source=path
            toast(selected_file)
            Clock.schedule_once(self.profile_pic,2)
   
    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''
        self.manager_open = False        
        self.file_manager.close()
        
    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()              
        return True                         

	
      
                  
#----------animate button-----------       
    def animate_btn_up(self,*args): 
        action_btn=self.ids.action_btn
        action_btn.opacity=1
        self.btn=Animation(pos_hint={'center_y':0.22},duration=0.180,transition='out_quart')      
        self.btn.bind(on_complete=self.animate_btn_down)
        self.btn.start(action_btn)
       
    def animate_btn_down(self,*args): 
        action_btn=self.ids.action_btn
        action_btn.opacity=1
        self.btn = Animation(pos_hint={'center_y':0.2},transition='out_bounce')        
        self.btn.bind(on_complete=self.animate_btn_up)
        self.btn.start(action_btn)
       
                            
#---------toolbar backspace----------- 
    def screen_back(self):
        self.manager.current='main_screen'
        self.btn.cancel(self.ids.action_btn)
                               
#---------profile pic change---------            
    def profile_pic(self,*args):      
        toast('Profile picture uploaded')
        with open('./account.json','w+') as testfile:
            testfile.write('{"'+str(user_mail)+'"'+':{"Password":'+'"'+str(self.manager.get_screen('account_screen').ids.password_text.text)+'"'+',"Source":'+'"'+str(self.manager.get_screen('main_screen').ids.nav_draw_img.source)+'"'+',"username":'+'"'+str(self.manager.get_screen('account_screen').ids.username_text.text)+'"'+',"name":'+'"'+str(self.manager.get_screen('account_screen').ids.name_text.text)+'"'+'}}')
   
#-------------profile data edit------------                  
    def profile_edit(self):
        if self.ids.name_text.text=='guest':    
            snackbar=Snackbar(text='Please create an account..')
            snackbar.show()
        else:    
            snackbar=Snackbar(text='Now You Can Edit Your Profile..')
            snackbar.show()
            self.ids.name_text.disabled=False
            self.ids.username_text.disabled=False
            self.ids.password_text.disabled=False

#-----------profile save----------
    def account_save(self):
        self.save_btn=self.manager.get_screen('account_screen').ids.save
        self.save_btn.disabled=True
        #self.t1=threading.Thread(target=self.spinner_func,daemon=True )
        self.t2=threading.Thread(target=self.profile_save,daemon=True )
        #self.t1.start()
        self.t2.start()
        
        
    def spinner_func(self):      
        self.manager.get_screen('account_screen').add_widget(self.ids.spinnerbar)                      
        if self.manager.get_screen('account_screen').ids.spinnerbar.active==False:
            self.manager.get_screen('account_screen').ids.spinnerbar.active=True
            toast('please wait!!')                                                  
        else:
            self.manager.get_screen('account_screen').ids.spinnerbar.active=False
   
    def profile_save(self):
        self.manager.get_screen('account_screen').ids.spinnerbar.active=True
        toast('please wait!!')    
        account_name=self.ids.name_text.text
        if account_name=='guest':
            self.manager.get_screen('account_screen').ids.spinnerbar.active=False
            self.dialog = MDDialog(title='Error',text='Please create an account',buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss=False )
            self.dialog.open()
        
        else:                  
            update_name=self.ids.name_text.text                    
            update_username=self.ids.username_text.text
            update_password=self.ids.password_text.text
            config={'apiKey': "AIzaSyBQpOq-fnqecey1jgL1tacFoDVVIzzoAag",
            'authDomain': "database-kivy.firebaseapp.com",
            'databaseURL': "https://database-kivy-default-rtdb.firebaseio.com",
            'projectId': "database-kivy",
            'storageBucket': "database-kivy.appspot.com",
            'messagingSenderId': "463911016117",
            'appId': "1:463911016117:web:793fa95b350daf110890fc",
            'measurementId': "G-65QQ68TKDB"}
            firebase=pyrebase.initialize_app(config)
            db=firebase.database()
            db.child(user_mail).update({'Name':update_name})
            db.child(user_mail).update({'Username':update_username})
            db.child(user_mail).update({'password':update_password})
            
            # ++++++data file save++++++
            
            with open('./account.json','w+') as testfile:
                testfile.write('{"'+str(user_mail)+'"'+':{"Password":'+'"'+str(update_password)+'"'+',"Source":'+'"'+str(self.manager.get_screen('main_screen').ids.nav_draw_img.source)+'"'+',"username":'+'"'+str(update_username)+'"'+',"name":'+'"'+str(update_name)+'"'+'}}')
            self.manager.get_screen('account_screen').ids.spinnerbar.active=False        
            #self.ids.spinnerbar.active=False                       
            toast('account updated')
            self.save_btn.disabled=False
                           # self.manager.get_screen('account_screen').ids.spinnerbar.active=False
            #self.manager.get_screen('account_screen').remove_widget(self.ids.spinnerbar)
           # stop= threading.Event()
#            stop.set()
#            stop2.set()
          
	
                                     
            
#-----------logout---------------                            
    def logout_func(self):
        file_check=os.path.isfile('./account.json')
        if file_check==True:
            os.remove('./account.json')
            global user_mail
            user_mail=' '
            self.manager.current='login_screen'
        else:
            self.manager.current='login_screen'
	


        
                        
#Main screen            

class Main_Screen(Screen):
    run_func=0
    
    def refresh(self):
        try:
            check_file=os.path.isfile('main.txt')
            if check_file==True:             
                os.remove('main.txt')
                config={'apiKey': "AIzaSyBQpOq-fnqecey1jgL1tacFoDVVIzzoAag",
                'authDomain': "database-kivy.firebaseapp.com",
                'databaseURL': "https://database-kivy-default-rtdb.firebaseio.com",
                'projectId': "database-kivy",
                'storageBucket': "database-kivy.appspot.com",
                'messagingSenderId': "463911016117",
                'appId': "1:463911016117:web:793fa95b350daf110890fc",
                'measurementId': "G-65QQ68TKDB"}           
                pyrebase_firebase=pyrebase.initialize_app(config)
                storage=pyrebase_firebase.storage()
                storage.child('main.txt').download('main.txt')
                self.image_show()
               
            else:
                pass
        except Exception as es:           
            print(es)        
        
        
   
    def on_pre_enter(self):           
        name=self.manager.get_screen('account_screen').ids.name_text.text        
        self.manager.get_screen('main_screen').ids.nav_name.text=' '+str(name).upper()
        self.manager.get_screen('main_screen').ids.nav_email.text='  '+str(user_mail).replace('-','.')
       # self.ids.nav_draw_img.source=user_img
        if self.run_func==0:
            self.run_func=1
            self.image_show()
        else:
            return
 
       
            
      
    @mainthread        
    def image_show(self):
        try:
            
            with open('main.txt','r') as img_file:
                image_list=(img_file.readlines())              
                self.manager.get_screen('main_screen').ids.grid.clear_widgets()
               
                 
                for i in reversed(image_list):               
                	web_img=SmartTileWithStar(source=i,size_hint_y= None,height="240dp",allow_stretch=True) #size_hint=(None,None),height='170dp',width='170dp')
                	self.ids.grid.add_widget(web_img)
               
      			               
        except  IOError or FileNotFoundError:           
            config={'apiKey': "AIzaSyBQpOq-fnqecey1jgL1tacFoDVVIzzoAag",
            'authDomain': "database-kivy.firebaseapp.com",
            'databaseURL': "https://database-kivy-default-rtdb.firebaseio.com",
            'projectId': "database-kivy",
            'storageBucket': "database-kivy.appspot.com",
            'messagingSenderId': "463911016117",
            'appId': "1:463911016117:web:793fa95b350daf110890fc",
            'measurementId': "G-65QQ68TKDB"}           
            pyrebase_firebase=pyrebase.initialize_app(config)
            storage=pyrebase_firebase.storage()
            storage.child('main.txt').download('main.txt')
            self.image_show()
        except OSError as  oserror:
            print(oserror)
        except Exception as er:
            self.dialog = MDDialog(title='Error',text=str(er), buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True))],auto_dismiss=False)
            self.dialog.open()
            print(er)
        
                    
    def add_btn(self):
        refresh_btn=self.ids.refresh_btn
        refresh_btn.opacity=1          
        anim=Animation(pos_hint={'center_x':0.85,'center_y':0.2})
        anim.start(refresh_btn)
        #self.animation.cancel(refresh_btn)
       
    def remove_btn(self):
        refresh_btn=self.ids.refresh_btn        
        refresh_btn.opacity=1
        self.animation=Animation(pos_hint={'center_y':-0.4},duration=0.200)
        self.animation.start(refresh_btn)
           
    def show_theme_picker(self):
        toast('please Wait...')
        self.theme_dialog = MDThemePicker()
        self.theme_dialog.open()        
      
    def show_example_grid_bottom_sheet(self):
        try:                               
           # import the needed Java class
            PythonActivity = autoclass('org.renpy.android.PythonActivity')
            Intent = autoclass('android.content.Intent')
            String = autoclass('java.lang.String')
            # create the intent
            intent = Intent()
            intent.setAction(Intent.ACTION_SEND)           
            intent.setType("text/plain")
          
            intent.putExtra(Intent.EXTRA_TEXT, String('check out  this cool apps \n https:\\\\play.google.com'))          
            chooser = Intent.createChooser(intent, String('Share Via...'))
            PythonActivity.mActivity.startActivity(chooser)        
        except Exception as ex:
            self.dialog = MDDialog(title='Error',text=str(ex),buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss = False )
            self.dialog.open() 
     
# Registration Screen
class Registration_Screen(Screen):
    def __init__(self,**kwargs):
        super(Registration_Screen,self).__init__(**kwargs)
            #code goes here and add:
        Window.bind(on_keyboard=self.back_click)

    def back_click(self,window,key,*largs):
            if key == 27:
                self.manager.current='login_screen'#you can create a method here to cache in a list the number of screens and then pop the last visited screen.
                return True
        #MDSpinner(size_hint=(None, None),size=( dp(46), dp(46)),pos_hint={'center_x': .5, 'center_y': .5},active=True )
    def on_pre_enter(self):
        self.url='https://database-kivy-default-rtdb.firebaseio.com/.json'
        self.auth='JvMoJBZZP1EBkYVeGvVmN2gLhTZcFjUfajXJcvEd'		
      
    def func(self):
        boolval=self.manager.get_screen('registration_screen').ids.pass_word.password
        if boolval==True:
            self.manager.get_screen('registration_screen').ids.pass_word.password=False
        else:
            self.manager.get_screen('registration_screen').ids.pass_word.password=True
    def loading_func(self):
        if self.manager.get_screen('registration_screen').ids.spinner.active==False:
            self.manager.get_screen('registration_screen').ids.spinner.active=True
            Clock.schedule_once(self.sign_up,3)
        else:
            self.manager.get_screen('registration_screen').ids.spinner.active=False
 
    @mainthread       
    def sign_up(self,*args):       
        name=self.manager.get_screen('registration_screen').ids.name.text
        username=self.manager.get_screen('registration_screen').ids.user_name.text
        email=self.manager.get_screen('registration_screen').ids.email.text
        password=self.manager.get_screen('registration_screen').ids.pass_word.text
        req=requests.get(url=self.url+'?auth='+self.auth)
        data=req.json()
        email_set=set()
        for key,value in data.items():
                email_set.add(key)
        
        if name=='' and username=='' and email=='' and password=='':
            self.manager.get_screen('registration_screen').ids.spinner.active=False
            self.snackbar_show()
            return       
      
        elif email.replace('.','-') in email_set:
            self.manager.get_screen('registration_screen').ids.spinner.active=False
            self.dialog = MDDialog(title='Error',text='This Email is already created',buttons=[MDFlatButton(text="CANCEL", on_release=lambda x:self.dialog.dismiss(force=True ))],auto_dismiss=False )
            self.dialog.open()
            
        else:
             
            sign_data=str({f'\"{email}\":{{"Name":\"{name}\","Username":\"{username}\","password":\"{password}\"}}'})
            sign_data=sign_data.replace('.','-')
            sign_data=sign_data.replace("\'"," ")
            data_json=json.loads(sign_data)
            requests.patch(url=self.url,json=data_json)
            self.manager.get_screen('registration_screen').ids.spinner.active=False
 
            toast('Registration Successfull ',3)
            self.manager.current='login_screen'
    def snackbar_show(self):
        snackbar=Snackbar(text="All fields are required..")
        snackbar.show()
    def screen_back(self):
        self.manager.current='login_screen'
    

#Login Screen
class Login_Screen(Screen):
    
                   
    def on_pre_enter(self):
        self.auth='JvMoJBZZP1EBkYVeGvVmN2gLhTZcFjUfajXJcvEd'		
        self.url='https://database-kivy-default-rtdb.firebaseio.com/.json'	
  
   
                
    def anim(self):              
        print('hnnm')
    #    anim=Animation(opacity=0,duration=2)
#        anim +=Animation(opacity=1)
#        anim.start(widget)
            
    def func(self):
       
        boolval=self.manager.get_screen('login_screen').ids.pass_word.password
        if boolval==True:
            self.manager.get_screen('login_screen').ids.pass_word.password=False
        else:
            self.manager.get_screen('login_screen').ids.pass_word.password=True
 
    def  login_func(self):
        try:
        
            toast('please wait..',2)
            email=self.manager.get_screen('login_screen').ids.email.text
            password=self.manager.get_screen('login_screen').ids.pass_word.text
            email=email.replace('.','-')
            password=password.replace('.','-')
            req=requests.get(url=self.url+'?auth='+self.auth)
            data=req.json()
            email_set=set()
            
            for key1,value in data.items():
                email_set.add(key1)    
                             
            if email in email_set and password ==data[email]['password']:         
                dict_user=data[email]
                global user_mail
                user_mail=email
                self.name_user=(dict_user['Name'])
                self.user_name=(dict_user['Username'])
                self.password_user=(dict_user['password'])
                self.manager.get_screen('account_screen').ids.name_text.disabled=False
                self.manager.get_screen('account_screen').ids.username_text.disabled=False                          
                self.manager.get_screen('account_screen').ids.password_text.disabled=False                                
                self.manager.get_screen('account_screen').ids.name_text.text=self.name_user
                self.manager.get_screen('account_screen').ids.username_text.text=self.user_name         
                self.manager.get_screen('account_screen').ids.password_text.text=self.password_user
                self.manager.get_screen('account_screen').ids.password_text.disabled=True
                self.manager.get_screen('account_screen').ids.name_text.disabled=True
                self.manager.get_screen('account_screen').ids.username_text.disabled=True               
                Clock.schedule_once(self.clock_func,3)            
            else:
                snackbar=Snackbar(text="Invalid Email & Password")
                snackbar.show()
                
        except Exception as e:            
            self.dialog = MDDialog(title='Error', radius= [20],text=str(e),buttons=[MDRaisedButton(text='Try Again',on_release=lambda:self.login_func())],auto_dismiss=False )
            self.dialog.open()               
        
       
   
    def skip(self):
        toast('please wait..')             
        self.manager.get_screen('account_screen').ids.name_text.disabled=False
        self.manager.get_screen('account_screen').ids.username_text.disabled=False                          
        self.manager.get_screen('account_screen').ids.password_text.disabled=False                                
        self.manager.get_screen('account_screen').ids.name_text.text='guest'
        self.manager.get_screen('account_screen').ids.username_text.text=''
        self.manager.get_screen('account_screen').ids.password_text.text=''
        self.manager.get_screen('account_screen').ids.password_text.disabled=True
        self.manager.get_screen('account_screen').ids.name_text.disabled=True
        self.manager.get_screen('account_screen').ids.username_text.disabled=True
        self.manager.get_screen('main_screen').ids.nav_draw_img.source='/storage/emulated/0/Download/71234023-5fdb-43f4-bb3b-11ecfb64cb90.png'                           
        
        Clock.schedule_once(self.skip_change_screen,2)
    def skip_change_screen(self,*args):
        
        self.manager.current='main_screen'
    def clock_func(self,*args):
        toast('Login successful')
        with open('./account.json','w+') as testfile:
            testfile.write('{"'+str(user_mail)+'"'+':{"Password":'+'"'+str(self.manager.get_screen('account_screen').ids.password_text.text)+'"'+',"Source":'+'"'+str(self.manager.get_screen('main_screen').ids.nav_draw_img.source)+'"'+',"username":'+'"'+str(self.manager.get_screen('account_screen').ids.username_text.text)+'"'+',"name":'+'"'+str(self.manager.get_screen('account_screen').ids.name_text.text)+'"'+'}}')
        self.manager.current='main_screen'
    
class Forgot_Screen(Screen):
    pass        

                              

class Gallery(MDApp):
    
    def __init__(self,**kwargs):          
        self.title='Gallary'                        
        super().__init__(**kwargs)

    
                   
        
    def build(self):
    	from kivmob import TestIds,KivMob
    	self.ads=KivMob(TestIds.APP)
    	self.ads.new_banner(TestIds.BANNER,top_pos=False)
    	self.ads.request_banner()
    	self.ads.show_banner()
    	self.theme_cls = ThemeManager()  
    	self.theme_cls.theme_style='Dark'
    	self.theme_cls.primary_palette='DeepPurple'
    	self.theme_cls.accent_palette='Blue'
    	self.kv=Builder.load_file("main.kv")
    	return  self.kv
    
    
    def on_start(self):
        login_file=os.path.isfile('./account.json')
        if login_file is True:      
            
            with open('./account.json','r+') as login_file:
                data=json.load(login_file)
            for key in data:
                json_user=data[key]
                global user_mail
                user_mail=key
            self.password_user=json_user['Password']
            source_img=json_user['Source']
            self.name_user=json_user['name']
            self.username=json_user['username']
           
            self.root.get_screen('account_screen').ids.name_text.disabled=False
            self.root.get_screen('account_screen').ids.username_text.disabled=False                          
            self.root.get_screen('account_screen').ids.password_text.disabled=False
            self.root.get_screen('account_screen').ids.name_text.text=' '                  
            self.root.get_screen('account_screen').ids.name_text.text=self.name_user
            self.root.get_screen('account_screen').ids.username_text.text=self.username         
            self.root.get_screen('account_screen').ids.password_text.text=self.password_user
            self.root.get_screen('account_screen').ids.password_text.disabled=True
            self.root.get_screen('account_screen').ids.name_text.disabled=True
            self.root.get_screen('account_screen').ids.username_text.disabled=True
            self.root.get_screen('main_screen').ids.nav_draw_img.source=source_img                                                                                                                  
            self.root.current='main_screen'
        else:
            self.root.current='login_screen'       
    def profile_edit(self,*args):       
        print('ok')
   
            
if __name__=='__main__':
	import sys
	try:
		Gallery().run()
	except:
		exc_type,exc_value,exc_traceback=sys.exc_info()
		with open('/storage/emulated/0/error_app.txt','a+') as f:			
			f.write(f'{exc_type}\n{exc_value}\n{exc_traceback}')
	
    	
  

