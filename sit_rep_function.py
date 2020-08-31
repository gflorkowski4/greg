from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime 
from time_function import time_delta
import csv
import pandas as pd 


def create_sit_rep():
    sage_sitrep = Tk()
    sage_sitrep.title("Situation Report")
    #sage_sitrep.wm_iconbitmap('data/airplane.ico')

    def produce_sit_rep():


        filename = "sitrep.csv"

        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

        output_writer.writerow(["Asset","SORTIES","FLIGHT HOURS","GRIDS","UHF/VHF",
                                "DRT HOURS","CELL ACTIVE RF %","802.11%","STRIKES",
                                "OPS","SI TRIGGERS","TD","JP","EKIA","EWIA","EDIA",])

        #DRACO
        #total calculations
        date1= week1_entry.get()
        date2=week5_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        df = df[(df['Mission_Start_Date'].between(date1,date2))&(df['Callsign']=='DRACO')]



        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

        #Total Row
        output_writer.writerow(["DRACO",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        output_file.close()

        #MADMAN
        #total calculations
        date1= week1_entry.get()
        date2=week5_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        df = df[(df['Mission_Start_Date'].between(date1,date2))&(df['Callsign']=='MADMAN')]



        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

        #Total Row
        output_writer.writerow(["MADMAN",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        output_file.close()

        #MUGSHOT
        #total calculations
        date1= week1_entry.get()
        date2=week5_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        df = df[(df['Mission_Start_Date'].between(date1,date2))&(df['Callsign']=='MUGSHOT')]



        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

        #Total Row
        output_writer.writerow(["MUGSHOT",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        output_file.close()
        
        #PHOENIX
        #total calculations
        date1= week1_entry.get()
        date2=week5_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        df = df[(df['Mission_Start_Date'].between(date1,date2))&(df['Callsign']=='PHOENIX')]



        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

        #Total Row
        output_writer.writerow(["PHOENIX",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        output_file.close()
        
        #MENTOR
        #total calculations
        date1= week1_entry.get()
        date2=week5_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        df = df[(df['Mission_Start_Date'].between(date1,date2))&(df['Callsign']=='MENTOR')]



        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

        #Total Row
        output_writer.writerow(["MENTOR",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        

        output_writer.writerow([""])
        output_writer.writerow(["Week"])

        output_file.close()

        #week1 calculations

        date1= week1_entry.get()
        date2=week1_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        mask = df['Mission_Start_Date'].between(date1,date2)
        df = df[mask]

        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

        #Row 1
        output_writer.writerow(["Week 1",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        output_file.close()

        #week2 calculations
        date1= week2_entry.get()
        date2=week2_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        mask = df['Mission_Start_Date'].between(date1,date2)
        df = df[mask]

        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

        #Row 2
        output_writer.writerow(["Week 2",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        output_file.close()

        #week3 calculations
        date1= week3_entry.get()
        date2=week3_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        mask = df['Mission_Start_Date'].between(date1,date2)
        df = df[mask]

        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)


        #Row 3
        output_writer.writerow(["Week 3",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        output_file.close()

        #week4 calculations
        date1= week4_entry.get()
        date2=week4_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        mask = df['Mission_Start_Date'].between(date1,date2)
        df = df[mask]

        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

       
        #Row 4
        output_writer.writerow(["Week 4",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        output_file.close()

        #week5 calculations
        date1= week5_entry.get()
        date2=week5_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        mask = df['Mission_Start_Date'].between(date1,date2)
        df = df[mask]


        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

        #Row 5
        output_writer.writerow(["Week 5",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        output_file.close()

        #TOTAL ROW
        #total calculations
        date1= week1_entry.get()
        date2=week5_2entry.get()
        df = pd.read_csv('example.csv')
        df['Mission_Start_Date'] = pd.to_datetime(df['Mission_Start_Date'])

        mask = df['Mission_Start_Date'].between(date1,date2)
        df = df[mask]


        filename = "sitrep.csv"
        output_file = open(filename, 'a', newline='')
        output_writer = csv.writer(output_file)

        #Total Row
        output_writer.writerow(["Total",df['Sorties'].sum(),df["Flight Duration"].sum(),
                                df["GA's"].sum()+df["SA's"].sum()+df["PG's"].sum()+
                                df["HC's"].sum()+df["SF_IVO's"].sum()+df["SF_@'s"].sum()+
                                df["MA_IVO's"].sum()+df["MA_HC's"].sum(),"","",
                                str(df["Onstation_Duration"].sum()/df["HVR_Hrs"].sum()*100)+"%","",df["Strikes"].sum(),
                                df["Ops Supported"].sum(),df["SI Triggers"].sum(),df["TD"].sum(),df["JP"].sum(),
                                df["EKIA"].sum(),df["EDIA"].sum(),df["EWIA"].sum()])
        output_file.close()

        



    #ENTRY FRAME
    entry_frame = Frame(sage_sitrep)
	entry_frame.grid(row=1,column=0)
    
	#Weeks Array
    week_label = []
    week_entryInit = []
    to_label = []
    week_entryEnd = []
	
	
    w = 0
	
    while w < 5:
        week_label[w] = Label(entry_frame,text="Week " + str(w + 1) + " Dates")
        week_label[w].grid(row=w,column=0, padx=5, pady=5)

        week_entry[w] = DateEntry(entry_frame)
        week_entry[w].grid(row=w,column=1, padx=5, pady=5)

        to_label[w] = Label(entry_frame,text=" TO ")
        to_label[w].grid(row=w,column=2,padx=5, pady=5)

        week_entry[w] = DateEntry(entry_frame)
        week_entry[w].grid(row=w,column=3,padx=5, pady=5)
		
        w += 1
		

    """#WEEK 1
    week1_label = Label(entry_frame,text="Week 1 Dates")
    week1_label.grid(row=0,column=0, padx=5, pady=5)

    week1_entry = DateEntry(entry_frame)
    week1_entry.grid(row=0,column=1,padx=5, pady=5)

    to_label = Label(entry_frame,text=" TO ")
    to_label.grid(row=0,column=2,padx=5, pady=5)

    week1_2entry = DateEntry(entry_frame)
    week1_2entry.grid(row=0,column=3,padx=5, pady=5)

    #WEEK 2
    week2_label = Label(entry_frame,text="Week 2 Dates")
    week2_label.grid(row=1,column=0,padx=5, pady=5)

    week2_entry = DateEntry(entry_frame)
    week2_entry.grid(row=1,column=1,padx=5, pady=5)

    to_label = Label(entry_frame,text=" TO ")
    to_label.grid(row=1,column=2,padx=5, pady=5)

    week2_2entry = DateEntry(entry_frame)
    week2_2entry.grid(row=1,column=3,padx=5, pady=5)

    #WEEK 3
    week3_label = Label(entry_frame,text="Week 3 Dates")
    week3_label.grid(row=2,column=0,padx=5, pady=5)

    week3_entry = DateEntry(entry_frame)
    week3_entry.grid(row=2,column=1,padx=5, pady=5)

    to_label = Label(entry_frame,text=" TO ")
    to_label.grid(row=2,column=2,padx=5, pady=5)

    week3_2entry = DateEntry(entry_frame)
    week3_2entry.grid(row=2,column=3,padx=5, pady=5)

    #WEEK 4
    week4_label = Label(entry_frame,text="Week 4 Dates")
    week4_label.grid(row=3,column=0,padx=5, pady=5)

    week4_entry = DateEntry(entry_frame)
    week4_entry.grid(row=3,column=1,padx=5, pady=5)

    to_label = Label(entry_frame,text=" TO ")
    to_label.grid(row=3,column=2,padx=5, pady=5)

    week4_2entry = DateEntry(entry_frame)
    week4_2entry.grid(row=3,column=3,padx=5, pady=5)

    #WEEK 5
    week5_label = Label(entry_frame,text="Week 5 Dates")
    week5_label.grid(row=4,column=0,padx=5, pady=5)

    week5_entry = DateEntry(entry_frame)
    week5_entry.grid(row=4,column=1,padx=5, pady=5)

    to_label = Label(entry_frame,text=" TO ")
    to_label.grid(row=4,column=2,padx=5, pady=5)

    week5_2entry = DateEntry(entry_frame)
    week5_2entry.grid(row=4,column=3,padx=5, pady=5)"""



    create_sitrep = Button(entry_frame,text="Create Situation Report",
                           command=produce_sit_rep)
    create_sitrep.grid(row=7,column=0,columnspan=6)

    sage_sitrep.mainloop()

   