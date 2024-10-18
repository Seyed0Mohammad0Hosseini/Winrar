import PySimpleGUI as sg
import zip_creator

input_box_files = sg.InputText(tooltip="Enter files", key='files_box')
input_box_destination = sg.InputText(tooltip="Enter destination", key='destination_box')
files_choose_button = sg.FilesBrowse("Choose", key='files_button')
destination_choose_button = sg.FolderBrowse("Choose", key='destination_button')
files_text = sg.Text("Select files to archive: ")
destination_text = sg.Text("Select destination: ")
compress_button = sg.Button("Compress")
output_label = sg.Text("", key="result")
window = sg.Window('Winrar', layout=[
    [files_text, input_box_files, files_choose_button],
    [destination_text, input_box_destination, destination_choose_button],
    [compress_button, output_label]
], )

while True:
    event, values = window.read()
    files_address = values['files_button'].split(";")
    files_destination = values['destination_button']
    print(event, values)
    match event:
        case "Compress":
            zip_creator.make_archive(files_address, files_destination)
            window['result'].update(value="Compression completed")
        case WIN_CLOSED:
            break

window.close()
