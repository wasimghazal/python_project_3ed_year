# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/frame.html
# https://www.tutorialspoint.com/python/tk_relief.htm#:~:text=Advertisements,be%20used%20for%20relief%20attribute.
# def main()
# ---------------------------------
# project 1
# Date: 08 / 12 / 2020
# time: 14:00
# Group number  : 4
# Name          : Wasim G Aswad
# Student ID    : 17193559
#
# Assisted and worked with Damian Larkin (18230253) & Ash
# ---------------------------------
import msvcrt as mm
import csv
import tkinter as tk
import os
import time
from doctest import master
import sys
import numpy as np
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
from shutil import copyfile
from PIL import Image
from PIL import ImageTk


def splash_window():
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    width = 400
    height = 400
    x = w / 2 - width / 2
    y = h / 2 - height / 2

    splash.geometry('%dx%d+%d+%d' % (width, height, x, y))
    splash.overrideredirect(1)
    splash.configure(bg='black')

    label1 = tk.Label(
        splash,
        text='Convert file to CSV and read it',
        font='helvetica 20')  #,
        #bg='black',
       # fg='blue')

    label1.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

    image = Image.open('./image.jpg')
    logo = ImageTk.PhotoImage(image)
    label2 = tk.Label(splash, image=logo)
    label2.image = logo

    label2.grid(column=0, row=1, padx=10, pady=10, sticky='ew')
    loading_bar2 = ttk.Progressbar(
        splash,
        orient='horizontal',
        length=185,
        mode="determinate")
    loading_bar2.grid(column=0, row=3, padx=10, pady=10, sticky='ew')
    loading_bar2.start(interval=18)
    splash.destroy()


def log_meg(mes):
    general_message = mes + '\n'
    display_the_system.insert(tk.END, general_message)
    display_the_system.see(tk.END)
    with open("./temp_log_file.txt", 'a+') as log_file:
        log_file.write(time.strftime('%c\t') + general_message)
    return


def create_graph():
    print('starting create graph')
    global the_row, fig1, accelerometer_x, accelerometer_y, accelerometer_z, temperature, gyroscope_x
    global gyroscope_y, gyroscope_z, pitch, roll, results, flag_clear_graph

    if flag_clear_graph == 1:
        del ax1.lines[0]  # to clear the graph before to call the new one
        flag_clear_graph = 0

    samples = []
    accelerometer_x = []
    accelerometer_y = []
    accelerometer_z = []
    temperature = []
    gyroscope_x = []
    gyroscope_y = []
    gyroscope_z = []
    pitch = []
    roll = []
    results = []
    for i in range(1, 241):
        samples.append(i)

    the_row = []
    line_count = 0
    if os.path.isfile('./output.csv'):
        with open('./output.csv', newline='') as csvfile:
            filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in filereader:
                line_count += 1
                if line_count >= 8:
                    accelerometer_x.append(row[1])
                    accelerometer_y.append(row[2])
                    accelerometer_z.append(row[3])
                    temperature.append(row[4])
                    gyroscope_x.append(row[5])
                    gyroscope_y.append(row[6])
                    gyroscope_z.append(row[7])
                    pitch.append(row[8])
                    roll.append(row[9])
                    the_row.append(row)

        the_row = np.array(the_row, dtype=object)
        print([the_row[1][0]])
        x = np.array([samples])

        if select_item.current() == 0:

            log_meg("[WARNING]: No graph type selected")

        # ----------------------------------------------------------------

        elif select_item.current() == 1:
            flag_clear_graph = 1
            results = list(map(float, accelerometer_x))
            y = np.array([results])
            results = []
            ax1.set_xlabel('Sample')
            ax1.set_ylabel('Accelerometer (x)')
            ax1.set_title('Plot accelerometer (x) vs. sample')
            ax1.plot(x[0], y[0])
            canvas1.draw_idle()
            log_meg("[INFORMATION]: Call plot accelerometer (x) vs. sample")

        # ----------------------------------------------------------------

        elif select_item.current() == 2:
            flag_clear_graph = 1
            results = list(map(float, accelerometer_y))
            y = np.array([results])
            results = []
            ax1.set_title('Plot accelerometer (y) vs. sample')
            ax1.set_ylabel('Accelerometer (y)')
            ax1.set_xlabel('Sample')
            ax1.plot(x[0], y[0])
            canvas1.draw_idle()
            log_meg("[INFORMATION]: Call plot accelerometer (y) vs. sample")
        elif select_item.current() == 3:
            flag_clear_graph = 1
            results = list(map(float, accelerometer_z))
            y = np.array([results])
            results = []
            ax1.set_title('Plot accelerometer (z) vs. sample')
            ax1.set_ylabel('Accelerometer (z)')
            ax1.set_xlabel('Sample')
            ax1.plot(x[0], y[0])
            canvas1.draw_idle()
            log_meg("[INFORMATION]: Call plot accelerometer (z) vs. sample")
        elif select_item.current() == 4:
            flag_clear_graph = 1
            results = list(map(float, temperature))
            y = np.array([results])
            results = []
            ax1.set_title('Plot temperature vs. sample')
            ax1.set_ylabel('Temperature')
            ax1.set_xlabel('Sample')
            ax1.plot(x[0], y[0])
            canvas1.draw_idle()
            log_meg("[INFORMATION]: Call plot temperature vs. sample")
        elif select_item.current() == 5:
            flag_clear_graph = 1
            results = list(map(float, gyroscope_x))
            y = np.array([results])
            results = []
            ax1.set_title('Plot gyroscope (x) vs. sample')
            ax1.set_ylabel('Gyroscope (x)')
            ax1.set_xlabel('Sample')
            ax1.plot(x[0], y[0])
            canvas1.draw_idle()
            log_meg("[INFORMATION]: Call plot gyroscope (x) vs. sample")
        elif select_item.current() == 6:
            flag_clear_graph = 1
            results = list(map(float, gyroscope_y))
            y = np.array([results])
            results = []
            ax1.set_title('Plot gyroscope (y) vs. sample')
            ax1.set_ylabel('Gyroscope (y)')
            ax1.set_xlabel('Sample')
            ax1.plot(x[0], y[0])
            canvas1.draw_idle()
            log_meg("[INFORMATION]: Call plot gyroscope (y) vs. sample")
        elif select_item.current() == 7:
            flag_clear_graph = 1
            results = list(map(float, gyroscope_z))
            y = np.array([results])
            results = []
            ax1.set_title('Plot gyroscope (z) vs. sample')
            ax1.set_ylabel('Gyroscope (z)')
            ax1.set_xlabel('Sample')
            ax1.plot(x[0], y[0])
            canvas1.draw_idle()
            log_meg("[INFORMATION]: Call plot gyroscope (z) vs. sample")
        elif select_item.current() == 8:
            flag_clear_graph = 1
            results = list(map(float, pitch))
            y = np.array([results])
            results = []
            ax1.set_title('Plot angle (pitch) vs. sample')
            ax1.set_ylabel('angle (pitch)')
            ax1.set_xlabel('Sample')
            ax1.plot(x[0], y[0])
            canvas1.draw_idle()
            log_meg("[INFORMATION]: Call plot angle (pitch) vs. sample")
        elif select_item.current() == 9:
            flag_clear_graph = 1
            results = list(map(float, roll))
            y = np.array([results])
            results = []
            ax1.set_title('Plot angle (roll) vs. sample')
            ax1.set_ylabel('angle (roll)')
            ax1.set_xlabel('Sample')
            ax1.plot(x[0], y[0])
            canvas1.draw_idle()
            log_meg("[INFORMATION]: Call plot angle (roll) vs. sample")

        print('plot complete - creating log entry')

    else:
        general_message = '[WARNING]: \"./output.csv\" not found - plot aborted\n'
        display_the_system.insert(tk.END, general_message)
        # log
        with open("./log_file.txt", 'a+') as log_file:
            log_file.write(time.strftime('%c\n') + general_message)
    ####################################################################################################


def sample_operation(i, file):
    # add new line in the file with i
    file.write("\n" + str(i))


def operation(line, empty_list, name):
    # To check if it was there 'Accelerometer' word
    if name in line:
        # Read first row from the file
        for row in line:
            # Store each object in the variable X
            x = ','.join(row)
            for number in range(0, len(x)):
                number_or_char = (x[number])
                # check if the number_or_char = , or - or .
                if number_or_char == ',' or number_or_char == '-' or number_or_char == '.':
                    # add the number_or_char to the empty list
                    empty_list.append(number_or_char)
                # check if the number_or_char not number or alphabet
                elif not number_or_char.isnumeric() and not number_or_char.isdigit() and not number_or_char.isalpha():
                    # check if the number_or_char not < or > or ]
                    if not number_or_char == '<' and not number_or_char == '>' and not number_or_char == ']':
                        # check if the number_or_char not space or [ or =
                        if not number_or_char == '[' and not number_or_char == ' ' and not number_or_char == '=':
                            # check if the number_or_char is not \n (new line)
                            if not number_or_char == '\n':
                                # add the number_or_char to the empty list just to be sure it will add just the
                                # Comma and Negative sign then it will add to empty list
                                empty_list.append(number_or_char)
                # check if the number_or_char is number
                elif number_or_char.isnumeric():
                    # add the number_or_char to the empty list
                    empty_list.append(number_or_char)


def cleartext():
    print("clear the text")
    display_the_text.delete('1.0', tk.END)
    display_the_csv.delete('1.0', tk.END)
    display_the_system.delete('1.0', tk.END)
    display_the_system.insert(tk.END, 'reset\n')
    display_the_system.insert(tk.END, 'Start script run ' + time.strftime('%c\n'))


def clear_text():
    log_meg("[INFORMATION]: Clear everything")
    cleartext()
    check = os.path.isfile('output.csv')
    if check:
        os.remove("output.csv")
    select_item.current(0)
    global flag_clear_graph
    if flag_clear_graph == 1:
        del ax1.lines[0]  # to clear the graph before to call the new one
        flag_clear_graph = 0



def firstoperation(i, file1, lines, empty_list):
    for line in lines:
        if "Sample" in line:
            # if there is so will add 1 to i
            i += 1
            # calling the function with passing the i number and file name
            sample_operation(i, file1)
        elif "Accelerometer" in line:
            # It's called the function with passing the name want to search for, line number and the list
            operation(line, empty_list, "Accelerometer")
        elif "Temperature" in line:
            # It's called the function with passing the name want to search for, line number and the list
            operation(line, empty_list, "Temperature")
        elif "Gyroscope" in line:
            # It's called the function with passing the name want to search for, line number and the list
            operation(line, empty_list, "Gyroscope")
        elif "Pitch" in line:
            # It's called the function with passing the name want to search for, line number and the list
            operation(line, empty_list, "Pitch")

        if empty_list:
            # convert the list to string
            # https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
            print_list_to_file = ''.join(map(str, empty_list))
            # write the string print_list_to_file to the file
            file1.write(print_list_to_file)
            # delete all the element on the list
            empty_list = []


def export_to_txt():
    print("extract_to_txt")
    empty_list = []
    i = 0
    file1 = open("export_to_txt.txt", 'w')
    file1.write('project 1\n\nName: Wasim G Aswad\nStudent ID: 17193559\n')
    file1.write(time.strftime('%c\n'))
    file1.write('---------------------------\n')
    file_name = filename
    print("file_name " + file_name)
    print("filename " + filename)
    file2 = open(file_name, "r")
    lines = file2.readlines()
    firstoperation(i, file1, lines, empty_list)
    log_meg("[INFORMATION]: The file has been successfully exported to .txt.")


def export_to_csv():
    print("extract_to_csv")
    check = os.path.isfile('filename')
    # https://careerkarma.com/blog/python-check-if-file-exists/#:~:text=To%20check%20if%2C%20in%20Python,number%20of%20uses%20in%20Python.
    # check if the text file is exist
    if check:   # if the file exist
        print("file exist")
        oldir = os.getcwd()
        # create variable have the path and file name
        nameofthefile = oldir + "\\" + "export_to_txt.txt"
        # create temp name (wwww12345678.txt)
        tempfile = "wwww12345678.txt"
        # copy the text file to the temp file have name (wwww12345678.txt)
        copyfile(nameofthefile, oldir + "\\" + tempfile)
    else:   # if the file not exist
        print("file not exist")
        # will call the export_to_txt() function
        export_to_txt()
        # get the path of the file
        oldir = os.getcwd()
        # create variable have the path and file name
        nameofthefile = oldir + "\\" + "export_to_txt.txt"
        tempfile = "wwww12345678.txt"
        copyfile(nameofthefile, oldir + "\\" + tempfile)
        # delete the file that create when we call the function
        os.remove("export_to_txt.txt")

    empty_list = []
    file2 = open(tempfile, "r")
    lines = file2.readlines()
    with open('output.csv', 'w', newline='') as csvfile:
        file1 = csv.writer(
            csvfile,
            delimiter=',',
            quotechar=' ',
            quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(lines)):
            empty_list.append(lines[i])
            empty_list[-1] = empty_list[-1].strip()
            if empty_list:
                file1.writerows(map(lambda x: [x], empty_list))
                empty_list = []
    file2.close()
    # delete the temp file
    os.remove("wwww12345678.txt")
    with open('output.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count >= 8:
                display_the_csv.insert(tk.END, f'{row[0]}\n', )
                display_the_csv.insert(tk.END, f'{row[1]},{row[2]},{row[3]}\n')
                display_the_csv.insert(tk.END, f'{row[4]}\n')
                display_the_csv.insert(tk.END, f'{row[5]},{row[6]},{row[7]}\n')
                display_the_csv.insert(tk.END, f'{row[8]},{row[9]}\n')
                display_the_csv.see(tk.END)


def save_graph():
    print('saving')
    f = fig1
    if flag_clear_graph != 0:
        f.savefig("image")
        log_meg("[INFORMATION]: Graph saved under name image.png")
    else:
        log_meg("[WARNING]: Plot a graph before saving.")


def exit_window():
    print("exit")
    oldir = os.getcwd()
    msgbox1 = tk.messagebox.askyesno(
        title='Quit',
        message='Do you want save the system log?')

    if msgbox1 is True:
        copyfile(oldir + "\\" + "temp_log_file.txt", oldir + "\\" + "log_file.txt")
        log_meg("[INFORMATION]: Close the programme and save the system log as log_file.txt.")
        os.remove("temp_log_file.txt")
        root.destroy()
    else:
        log_meg("[INFORMATION]: Close the programme without to save the system log.")
        os.remove("temp_log_file.txt")
        root.destroy()


def browse_button():
    print("browse")
    global filename
    oldir = os.getcwd()
    display_the_text.delete('1.0', tk.END)  # delete the old input every time we press the button
    # allowed user see just text files
    filename = filedialog.askopenfilename(parent=root, initialdir=oldir, title='Please select file',
                                          filetypes=(("Text files", "*.txt"),
                                                     ("all files", "*.*")))
    # display_the_system.insert(tk.END, "open file name: " + filename + '\n')
    log_meg("[INFORMATION]: Open file name: " + filename)
   # display_the_system.see(tk.END)
    file = open(filename, "r")
    # https://stackoverflow.com/questions/59689761/python-attributeerror-str-object-has-no-attribute-read
    print("import the text file")
    # path_view.set(filename)                                   # set the pathname
    lines = file.readlines()
    for line in lines:
        display_the_text.insert(tk.END, line)
        file.close()
    display_the_text.see(tk.END)


def go_():
    print("go button")
    export_to_csv()
    log_meg("[INFORMATION]: " + "Convert the file " + filename + ' to CSV format type.')


def selected(event):
    print(select_item.current(), select_item.get())
    log_meg("[INFORMATION]: " + select_item.get())


def create_widgets():

    print("Create Widgets")


    global folder_path
    global display_the_text
    global display_the_csv
    global display_the_system
    global pathview
    global oldir
    global select_item
    global choices
    global general_message
    global frame_1, frame_2
    global x1

    global fig1
    global flag_clear_graph
    global value, input_
    flag_clear_graph = 0

    # -------------------------------------------
    
    global canvas1

    # -------------------------------------------   

    frame1 = Frame(root, height=45, width=1160, background='white')
    smallframe1 = Frame(frame1, height=45, width=300, background='white')
    smallframe2 = Frame(frame1, height=45, width=850, background='white')
    frame2 = Frame(root, height=410, width=440, background='white')
    frame3 = Frame(root, height=220, width=440, background='white')
    global frame4
    frame4 = Frame(root, height=650, width=700, background='black')
    frame_1 = Frame(frame4, width=510, height=45, background='white')
    frame_2 = Frame(frame4, width=680, height=530, background='white')
    smallframe1.grid(row=0, column=5, columnspan=4, sticky=W+E+N+S)
    smallframe2.grid(row=0, column=0, columnspan=5, sticky=W+E+N+S)
    frame1.grid(row=0, columnspan=2, padx=10, pady=10)
    frame2.grid(row=1, column=0, padx=10, pady=10)
    frame3.grid(row=2, column=0, padx=10, pady=10)
    frame4.grid(row=1, rowspan=2, column=1, padx=10, pady=10)
    frame_1.grid(column=0, row=2, padx=10, pady=10, sticky='ew')
    frame_2.grid(column=0, row=1, padx=10, pady=10, sticky='ew')

    frame1.grid_propagate(0)
    smallframe1.grid_propagate(0)
    smallframe2.grid_propagate(0)
    frame2.grid_propagate(0)
    frame3.grid_propagate(0)
    frame4.grid_propagate(0)
    frame_1.grid_propagate(0)
    frame_2.grid_propagate(0)

    label_introduction_name = tk.Label(smallframe1,
                                       text="Name: Wasim G Aswad",
                                       fg="white",
                                       bg="black")
    label_introduction_name.grid(column=1, row=0, padx=10, pady=10, sticky='we')
    label_introduction_student_id = tk.Label(smallframe1,
                                             text="Student ID: 17193559",
                                             fg="white",
                                             bg="black")
    label_introduction_student_id.grid(column=2, row=0, padx=20, pady=10, sticky='we')
    label_control = tk.Label(smallframe2,
                             bg="white",
                             text="Control panel")
    label_control.grid(column=0, row=0, padx=10, pady=1, sticky='we')
    browsebutton = tk.Button(smallframe2,
                             text="Browse",
                             command=browse_button)
    browsebutton.grid(column=1, row=0, padx=50, pady=10, sticky="we")
    go_button = tk.Button(smallframe2,
                          text='GO',
                          fg='purple',
                          command=go_)
    go_button.grid(column=2, row=0, padx=10, pady=10, sticky='we')
    clear_button = tk.Button(smallframe2,
                             text="Clear",
                             command=clear_text)
    clear_button.grid(column=3, row=0, padx=10, pady=10, sticky='we')

    exit_button = tk.Button(smallframe2,
                            text='Quit',
                            fg='red',
                            command=exit_window)
    exit_button.grid(column=4, row=0, padx=10, pady=10, sticky='we')
    label_txt = tk.Label(frame2,
                         bg="white",
                         text="Select result text file")
    label_txt.grid(column=0, row=1, padx=10, pady=1, sticky='ws')
    display_the_text = scrolledtext.ScrolledText(frame2,
                                                 fg="white",
                                                 bg="black",
                                                 height=10,
                                                 width=50)
    display_the_text.grid(column=0, row=2, columnspan=2, padx=10, pady=1, sticky='ES')
    label_empty2 = tk.Label(frame2,
                            background='white',
                            text="   ")
    label_empty2.grid(column=0, row=3, padx=10, pady=1, sticky='w')
    label_csv = tk.Label(frame2,
                         bg="white",
                         text="Results CSV file data")
    label_csv.grid(column=0, row=4, padx=10, pady=1, sticky='w')
    display_the_csv = scrolledtext.ScrolledText(frame2,
                                                fg="white",
                                                bg="black",
                                                height=10,
                                                width=50)
    display_the_csv.grid(column=0, row=5, columnspan=2, padx=10, pady=1, sticky='ES')
    label_empty3 = tk.Label(frame3,
                            background='white',
                            text="   ")
    label_empty3.grid(column=0, row=0, padx=0, pady=0, sticky='w')
    label_system_log = tk.Label(frame3,
                                bg="white",
                                text="System log")
    label_system_log.grid(column=0, row=1, padx=10, pady=1, sticky='W')
    display_the_system = scrolledtext.ScrolledText(frame3,
                                                   fg="white",
                                                   bg="black",
                                                   height=10,
                                                   width=50)
    display_the_system.grid(column=0, row=2, columnspan=2, padx=10, pady=1, sticky='ES')
    label_plot = tk.Label(frame4,
                          bg="white",
                          relief=FLAT,
                          text="Plot window")
    label_plot.grid(column=0, row=0, padx=10, pady=1, sticky='w')
    display_the_system.insert(tk.END, 'Start script run ' + time.strftime('%c\n'))

    # ----------------------------------------------------------
    
    fig1 = plt.Figure(figsize=(5, 4), dpi=130)
    fig1.tight_layout()
    global ax1
    ax1 = fig1.add_subplot(111)
    canvas1 = FigureCanvasTkAgg(fig1, master=frame4)
    canvas1.draw()
    x1 = canvas1.get_tk_widget()
    x1.grid(column=0, row=1)

    # ----------------------------------------------------------

    select_plot = tk.Label(frame_1,
                           bg="white",
                           relief=FLAT,
                           text="Select plot")
    select_plot.grid(column=0, row=0, padx=10, pady=10, sticky='w')
    update_button = tk.Button(frame_1,
                              text='update',
                              command=create_graph)
    update_button.grid(column=2, row=0, padx=10, pady=10, sticky='we')
    save_plot_button = tk.Button(frame_1,
                                 text='save plot',
                                 command=save_graph)
    save_plot_button.grid(column=3, row=0, padx=10, pady=10, sticky='we')
    drop_list = StringVar()
    choices = ['Select a plot ...',
               'Plot accelerometer (x) vs. sample',
               'Plot accelerometer (y) vs. sample',
               'Plot accelerometer (z) vs. sample',
               'Plot temperature vs. sample',
               'Plot gyroscope (x) vs. sample',
               'Plot gyroscope (y) vs. sample',
               'Plot gyroscope (z) vs. sample',
               'Plot angle (pitch) vs. sample',
               'Plot angle (roll) vs. sample']
    drop_list.set('Select a plot ...')
    select_item = ttk.Combobox(frame_1, value=choices, width=30, state="readonly")
    select_item.current(0)
    select_item.bind("<<ComboboxSelected>>", selected)
    select_item.grid(row=0, column=1, padx=10, sticky='we')
    log_meg("[INFORMATION]: Run the programme.")


def main():
    print("main")
    root.title("Project")
    root.resizable(width=False, height=False)
    root.geometry("1185x740")
    create_widgets()


if __name__ == "__main__":
    print("Strat")

    root = tk.Tk()
    splash = tk.Toplevel()
    splash.attributes('-topmost', True)
    splash_window()
    splash.after(3600, splash.destroy)

    root.iconbitmap('logo.ico')

    main()
    root.mainloop()
    #mainloop()

    print("End")


# ---------------------------------
# End of script
