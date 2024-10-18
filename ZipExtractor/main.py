import PySimpleGUI as sg
from zip_extractor import archive_extractor

sg.theme("Black")
zip_file_text = sg.Text("Select zip file:", key="zip_file_text")
destination_text = sg.Text("Select file:", key="destination_text")
zip_file_input = sg.InputText(key="zip_file_input")
destination_input = sg.InputText(key="destination_input")

# we count zipfile as a kind of file :)
zip_file_button = sg.FileBrowse("Choose", key="zip_file_button")
destination_button = sg.FolderBrowse("Choose", key="destination_button")
extract_button = sg.Button("Extract")
exit_button = sg.Button("Exit")
output_label = sg.Text(key="output", text_color="green")
window = sg.Window("Winrar", layout=[
    [zip_file_text, zip_file_input, zip_file_button],
    [destination_text, destination_input, destination_button],
    [extract_button, exit_button, output_label]
])
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Extract":
            try:
                archive_extractor(value["zip_file_input"], value["destination_input"])
                window["output"].update(value="Extraction completed")
            except FileNotFoundError:
                sg.popup("file or folder not found")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
