#!/usr/bin/env
import calendar
    def display_current_datetime():
        current_date= datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Current date and time: {formatted_datetime}") 
         
