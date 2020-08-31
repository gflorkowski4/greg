from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime 
from time_function import time_delta
import csv


def add():
	sage_add = Tk()
	sage_add.title("Add Mission")
	#sage_add.wm_iconbitmap('data/airplane.ico')
	
	#Submit Mission
	def submit_mission():

		totime = totime_h.get()+totime_m.get()
		ltime = ltime_h.get()+ltime_m.get()
		total_time = time_delta(ltime,totime)


		oftime = offtime_h.get()+offtime_m.get()
		onntime = ontime_h.get()+ontime_m.get()
		sta_duration =time_delta(oftime,onntime)

		htime = hvrtime_h.get()+hvrtime_m.get()
		ctime = clvldtime_h.get()+clvldtime_m.get()
		hoover_duration = time_delta(ctime,htime)






		filename = "C:\\Users\\jivib\\OneDrive\\Documents\\Work\\Projects\\PostMsn\\example.csv"
		output_file = open(filename, 'a', newline='')
		output_writer = csv.writer(output_file)
		'''
		output_writer.writerow(['Mission_Start_Date','Mission_End_Date','Operator', 'Trainee', 'SI_Mission_Num',
			'Mission_Num','Sorties','Callsign','Wheels_Up(Z)', 'Wheels_Down(Z)','Flight Duration','Onstation(Z)',
			'Offstation(Z)','Onstation_Duration','HVR_Time','CLVLD_Time','HVR_Hrs','GA\'s','SA\'s','PG\'s','HC\'s',
			'SF_IVO\'s','SF_@\'s','MA_IVO\'s','MA_HC\'s','Size of SF Data Transferred (MASF)',
			'Size of MA Data Transferred (MASF)','Strikes','Ops Supported','Obj Name','EKIA','EWIA','EDIA','TD','JP',
			'SI Triggers','Correlation','Province','Triggered_Target','Remarks'])
		'''
		output_writer.writerow([msn_start_date.get(), msn_end_date.get(),operator_entry.get(),trainee_entry.get(),
			si_msn_num_entry.get(),msn_number_entry.get(),sorties_entry.get(),call_sign_entry.get(),totime_h.get()+totime_m.get(),
			ltime_h.get()+ltime_m.get(),total_time,ontime_h.get()+ontime_m.get(),offtime_h.get()+offtime_m.get(),
			sta_duration,hvrtime_h.get()+hvrtime_m.get(),clvldtime_h.get()+clvldtime_m.get(),hoover_duration,GA_entry.get(),
			SA_entry.get(),PG_entry.get(),HC_entry.get(),SF_IVO_entry.get(),SF_entry.get(),MA_IVO_entry.get(),
			MA_HC_entry.get(),SF_DATA_entry.get(),MA_DATA_entry.get(),strikes_entry.get(),ops_entry.get(),objective_name_entry.get(),
			EKIA_entry.get(),EWIA_entry.get(),EDIA_entry.get(),td_entry.get(),jp_entry.get(),si_trigger_entry.get(),
			correlation_entry.get(),province_entry.get(),triggered_target_entry.get(),msn_sum.get("1.0","end-1c") ])
		
		output_file.close()
		sage_add.destroy()

	#Mission frame 
	mission_frame = Frame(sage_add)
	mission_frame.grid(row=0, column=0, padx=5, pady=5)

	#operator 
	operator_label = Label(mission_frame, text='Operator')
	operator_label.grid(row=0,column=0, padx=5, pady=5)
	operator_entry = Entry(mission_frame)
	operator_entry.grid(row=1, column=0, padx=5, pady=5)
	#Trainee

	trainee_label = Label(mission_frame, text='Trainee')
	trainee_label.grid(row=0,column=1, padx=5, pady=5)
	trainee_entry = Entry(mission_frame)
	trainee_entry.grid(row=1,column=1, padx=5, pady=5)

	#SI Mission Number
	si_msn_num_label = Label(mission_frame, text='SI Mission Number')
	si_msn_num_label.grid(row=0,column=2,padx=5, pady=5)

	si_msn_num_entry = Entry(mission_frame,)
	si_msn_num_entry.grid(row=1,column=2,padx=5, pady=5)

	#MSN Number

	msn_number_label = Label(mission_frame, text="Mission Number")
	msn_number_label.grid(row=0, column=3,padx=5, pady=5)

	msn_number_entry = Entry(mission_frame)
	msn_number_entry.grid(row=1, column=3,padx=5, pady=5)
	

	#Sorties 
	sorties_label = Label(mission_frame, text="Sorties")
	sorties_label.grid(row=0, column=4, padx=5, pady=5)

	sorties_entry = Spinbox(mission_frame, from_=0, to=5, wrap=True, width=4)
	sorties_entry.grid(row=1, column=4, padx=5, pady=5)



	#Callsign
	call_sign_label = Label(mission_frame, text='Callsign')
	call_sign_label.grid(row=0,column=5, padx=5, pady=5)

	call_sign_entry = ttk.Combobox(mission_frame, values = ["DRACO",
											"MADMAN",
											"MUGSHOT",
											"MENTOR",
											"PHOENIX"])
	call_sign_entry.grid(row=1, column=5)
	
	#Date frame
	date_frame = Frame(sage_add)
	date_frame.grid(row=1, column=0, columnspan=4)

	#Start Date
	msn_start_date_label = Label(date_frame, text='Mission Start Date')
	msn_start_date_label.grid(row=0, column=0, padx=20)

	msn_start_date = DateEntry(date_frame)
	msn_start_date.grid(row=1, column=0,padx=20)

	#End Date
	msn_end_date_label = Label(date_frame, text='Mission End Date')
	msn_end_date_label.grid(row=0, column=1,padx=20)

	msn_end_date = DateEntry(date_frame)
	msn_end_date.grid(row=1, column=1,padx=20)

	#Time Frame
	time_frame = Frame (sage_add)
	time_frame.grid(row=2, column=0)

	#takeoff

	take_off_frame = Frame(time_frame)
	take_off_frame.grid(row=0,column=0,padx=20,pady=5) 
	take_off_frame.configure(background="white")
	take_off_label= Label(take_off_frame, text="Take Off Time")
	take_off_label.grid(row=0, column=0,columnspan=2)


	totime_h = Spinbox(take_off_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24'), wrap=True, width=4)
	totime_h.grid(row=1, column=0)

	totime_m = Spinbox(take_off_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24','25','26',
											'27','28','29','30','31','32','33','34','35',
											'36','37','38','39','40','41','42','43','44',
											'45','46','47','48','49','50','51','52','53',
											'54','55','56','57','58','59'), wrap=True, width=4)

	

	
	totime_m.grid(row=1,column=1)
	
	#landing time 
	landing_frame = Frame(time_frame)
	landing_frame.configure(background="white")
	landing_frame.grid(row=0, column=1,padx=20,pady=5)
	landing_label= Label(landing_frame, text="Landing Time")
	landing_label.grid(row=0, column=0,columnspan=2)

	ltime_h = Spinbox(landing_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24'), wrap=True, width=4)
	ltime_h.grid(row=1, column=0)

	ltime_m = Spinbox(landing_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24','25','26',
											'27','28','29','30','31','32','33','34','35',
											'36','37','38','39','40','41','42','43','44',
											'45','46','47','48','49','50','51','52','53',
											'54','55','56','57','58','59'), wrap=True, width=4)



	ltime_m.grid(row=1,column=1)

	


	
	#on sta time 

	on_sta_frame = Frame(time_frame)
	on_sta_frame.configure(background="white")
	on_sta_frame.grid(row=0, column=2,padx=20,pady=5)
	
	on_sta_label= Label(on_sta_frame, text="On Station Time")
	on_sta_label.grid(row=0, column=0,columnspan=2)

	ontime_h = Spinbox(on_sta_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24'), wrap=True, width=4)
	ontime_h.grid(row=1, column=0)

	ontime_m = Spinbox(on_sta_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24','25','26',
											'27','28','29','30','31','32','33','34','35',
											'36','37','38','39','40','41','42','43','44',
											'45','46','47','48','49','50','51','52','53',
											'54','55','56','57','58','59'), wrap=True, width=4)
	ontime_m.grid(row=1,column=1)


	
	#off sta time 
	off_sta_frame = Frame(time_frame)
	off_sta_frame.configure(background="white")
	off_sta_frame.grid(row=0, column=3,padx=20,pady=5)
	off_sta_label= Label(off_sta_frame, text="Off Station Time")
	off_sta_label.grid(row=0,column=0, columnspan=2)

	offtime_h = Spinbox(off_sta_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24'), wrap=True, width=4)
	offtime_h.grid(row=1, column=0)

	offtime_m = Spinbox(off_sta_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24','25','26',
											'27','28','29','30','31','32','33','34','35',
											'36','37','38','39','40','41','42','43','44',
											'45','46','47','48','49','50','51','52','53',
											'54','55','56','57','58','59'), wrap=True, width=4)
	offtime_m.grid(row=1,column=1)


	
	#hvr time 

	hvr_frame = Frame(time_frame)
	hvr_frame.configure(background="white")
	hvr_frame.grid(row=0, column=4,padx=20,pady=5)

	hvr_label= Label(hvr_frame, text="Hoover Time")
	hvr_label.grid(row=0,column=0,columnspan=2)

	hvrtime_h = Spinbox(hvr_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24'), wrap=True, width=4)
	hvrtime_h.grid(row=1, column=0)

	hvrtime_m = Spinbox(hvr_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24','25','26',
											'27','28','29','30','31','32','33','34','35',
											'36','37','38','39','40','41','42','43','44',
											'45','46','47','48','49','50','51','52','53',
											'54','55','56','57','58','59'), wrap=True, width=4)
	hvrtime_m.grid(row=1,column=1)



	#clvld time 

	clvld_frame = Frame(time_frame)
	clvld_frame.configure(background="white")
	clvld_frame.grid(row=0,column=5,padx=20,pady=5)
	clvld_label= Label(clvld_frame, text="Cleveland Time")
	clvld_label.grid(row=0,column=0,columnspan=2)

	clvldtime_h = Spinbox(clvld_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24'), wrap=True, width=4)
	clvldtime_h.grid(row=1, column=0)

	clvldtime_m = Spinbox(clvld_frame, values=('00','01','02','03','04','05','06','07','08',
											'09','10','11','12','13','14','15','16','17',
											'18','19','20','21','22','23','24','25','26',
											'27','28','29','30','31','32','33','34','35',
											'36','37','38','39','40','41','42','43','44',
											'45','46','47','48','49','50','51','52','53',
											'54','55','56','57','58','59'), wrap=True, width=4)
	clvldtime_m.grid(row=1,column=1)
	
	#Grids frame
	grid_frame = Frame(sage_add)
	grid_frame.grid(row=3, column=0)

	#GAs
	GA_label = Label(grid_frame, text="GA's")
	GA_label.grid(row=0, column=0, padx=10, pady=5)
	

	GA_entry = Spinbox(grid_frame,from_=0, to=50, wrap=True, width=4)
	GA_entry.grid(row=1, column=0, padx=10, pady=5)
	
	#SAs
	SA_label = Label(grid_frame, text="SA's")
	SA_label.grid(row=0, column=1, padx=10, pady=5)
	

	SA_entry = Spinbox(grid_frame,from_=0, to=50, wrap=True, width=4)
	SA_entry.grid(row=1, column=1, padx=10, pady=5)

	#PGs
	PG_label = Label(grid_frame, text="PG's")
	PG_label.grid(row=0, column=2, padx=20, pady=5)
	

	PG_entry = Spinbox(grid_frame,from_=0, to=50, wrap=True, width=4)
	PG_entry.grid(row=1, column=2, padx=20, pady=5)

	#HCs
	HC_label = Label(grid_frame, text="HC's")
	HC_label.grid(row=0, column=3, padx=20, pady=5)
	

	HC_entry = Spinbox(grid_frame,from_=0, to=50, wrap=True, width=4)
	HC_entry.grid(row=1, column=3, padx=20, pady=5)

	#SF IVOs
	SF_IVO_label = Label(grid_frame, text="SF IVO's")
	SF_IVO_label.grid(row=0,column=4, padx=20, pady=5)
	

	SF_IVO_entry = Spinbox(grid_frame,from_=0, to=50, wrap=True, width=4)
	SF_IVO_entry.grid(row=1, column=4, padx=20, pady=5)

	#SF @s
	SF_label = Label(grid_frame, text="SF @'s")
	SF_label.grid(row=0, column=5, padx=20, pady=5)
	

	SF_entry = Spinbox(grid_frame,from_=0, to=50, wrap=True, width=4)
	SF_entry.grid(row=1, column=5, padx=20, pady=5)

	#MA IVOS
	MA_IVO_label = Label(grid_frame, text="MA IVO's")
	MA_IVO_label.grid(row=0, column=6, padx=20, pady=5)
	

	MA_IVO_entry = Spinbox(grid_frame,from_=0, to=50, wrap=True, width=4)
	MA_IVO_entry.grid(row=1, column=6, padx=20, pady=5)
	
	#MA HCS
	MA_HC_label = Label(grid_frame, text="MA HC's")
	MA_HC_label.grid(row=0, column=7, padx=20, pady=5)
	

	MA_HC_entry = Spinbox(grid_frame,from_=0, to=50, wrap=True, width=4)
	MA_HC_entry.grid(row=1, column=7, padx=20, pady=5)

	#Stats Frame 
	stats_frame = Frame(sage_add)
	stats_frame.grid(row=4, column=0,padx=5, pady=5,columnspan=6)

	#Size of SF data transferred 
	SF_DATA_label = Label(stats_frame, text="Size of SF Data Transferred")
	SF_DATA_label.grid(row=0, column=0,padx=5, pady=5)
	

	SF_DATA_entry = Entry(stats_frame)
	SF_DATA_entry.grid(row=1, column=0,padx=5, pady=5)

	#Size of MA Data Transferred

	MA_DATA_label = Label(stats_frame, text="Size of MA Data Transferred")
	MA_DATA_label.grid(row=0, column=1,padx=5, pady=5)
	

	MA_DATA_entry = Entry(stats_frame)
	MA_DATA_entry.grid(row=1, column=1,padx=5, pady=5)


	#ops 

	ops_label = Label(stats_frame, text="OPs supported")
	ops_label.grid(row=0, column=2,padx=5, pady=5)
	

	ops_entry = Spinbox(stats_frame,from_=0, to=50, wrap=True, width=4)
	ops_entry.grid(row=1, column=2,padx=5, pady=5)

	

	
	#Objective Name 
	objective_name_label = Label(stats_frame, text="Objective Name")
	objective_name_label.grid(row=0, column=3,padx=5, pady=5)
	

	objective_name_entry = Entry(stats_frame)
	objective_name_entry.grid(row=1, column=3,padx=5, pady=5)

	#Province
	province_label = Label(stats_frame, text="Province")
	province_label.grid(row=0, column=4, padx=5, pady=5)

	province_entry = Entry(stats_frame, text='')
	province_entry.grid(row=1, column=4, padx=5, pady=5)


	#Triggered target
	triggered_target_label = Label(stats_frame, text="Triggered Target")
	triggered_target_label.grid(row=0, column=6)

	triggered_target_entry = Entry(stats_frame, text='')
	triggered_target_entry.grid(row=1, column=6)

	#Strikes
	strikes_label = Label(stats_frame,text='Strikes')
	strikes_label.grid(row=0,column=7)

	strikes_entry = Spinbox(stats_frame, from_=0, to=10, width=4, wrap=True)
	strikes_entry.grid(row=1, column=7)

	#EKIA 
	EKIA_label = Label(stats_frame, text="EKIA")
	EKIA_label.grid(row=2, column=0)
	

	EKIA_entry = Spinbox(stats_frame, from_=0, to=10, wrap=True, width=4)
	EKIA_entry.grid(row=3, column=0)

	#EWIA 
	EWIA_label = Label(stats_frame, text="EWIA")
	EWIA_label.grid(row=2, column=1)

	EWIA_entry = Spinbox(stats_frame, from_=0, to=10, wrap=True, width=4)
	EWIA_entry.grid(row=3, column=1)


	#EDIA 
	EDIA_label = Label(stats_frame, text="EDIA")
	EDIA_label.grid(row=2, column=2)

	EDIA_entry = Spinbox(stats_frame, from_=0, to=10, wrap=True, width=4)
	EDIA_entry.grid(row=3, column=2)

	#TD
	td_label = Label(stats_frame, text="Touchdowns")
	td_label.grid(row=2, column=3)
	

	td_entry = Spinbox(stats_frame, from_=0, to=10, wrap=True, width=4)
	td_entry.grid(row=3, column=3)

	#JP
	jp_label = Label(stats_frame, text="Jackpots")
	jp_label.grid(row=2, column=4)
	

	jp_entry = Spinbox(stats_frame, from_=0, to=10, wrap=True, width=4)
	jp_entry.grid(row=3, column=4)

	#Si triggers
	si_trigger_label = Label(stats_frame, text="SI Trigger")
	si_trigger_label.grid(row=2, column=5)
	
	si_trigger_entry = Spinbox(stats_frame, from_=0, to=10, width=4, wrap=True)
	si_trigger_entry.grid(row=3, column=5)

	#Correlation
	correlation_label = Label(stats_frame, text="Correlation")
	correlation_label.grid(row=2, column=5, columnspan=2)
	
	correlation_entry = Spinbox(stats_frame, from_=0, to=10, width=4, wrap=True)
	correlation_entry.grid(row=3, column=5, columnspan=2)


	#remarks frame 
	remarks_frame = Frame(sage_add)
	remarks_frame.grid(row=5, column=0)

	#remarks box 
	#Mission Summary 
	msn_sum = Text(remarks_frame)
	msn_sum.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

	#mission submit 
	submit_button = Button(remarks_frame, text="Submit Mission", command=submit_mission)
	submit_button.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

	#Main Loop Call
	sage_add.mainloop()
	

