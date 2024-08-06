import PySimpleGUI as sg
import sys

sg.theme("Black")

def main():
    x = input('''
              How do you want to use your calculator?
              
              (1) Terminal
              (2) Interface
              
Type: ''')
    if x == '1':
        print(calculator(input("type the math expression: ")))
    elif x == '2':
        interface()
    else:
        sys.exit("Invalid function...")

def layout(): #TENTAR JUNTAR TODOS OS NUMEROS AQUI
    return [
        [sg.Multiline(
            "", size=(18, 4), key="-DISPLAY-", justification="r", 
            font="digit 22", no_scrollbar=True
        )],
        [sg.Button("clear", size=(5, 3)), sg.Button("(", size=(5, 3)), sg.Button(")", size=(5, 3)), sg.Button("/", size=(5, 3))],
        [sg.Button("7", size=(5, 3)), sg.Button("8", size=(5, 3)), sg.Button("9", size=(5, 3)), sg.Button("*", size=(5, 3))],
        [sg.Button("4", size=(5, 3)), sg.Button("5", size=(5, 3)), sg.Button("6", size=(5, 3)), sg.Button("-", size=(5, 3))],
        [sg.Button("1", size=(5, 3)), sg.Button("2", size=(5, 3)), sg.Button("3", size=(5, 3)), sg.Button("+", size=(5, 3))],
        [sg.Button("0", size=(5, 3)), sg.Button(".", size=(5, 3)), sg.Button("%", size=(5, 3)), sg.Button("=", size=(5, 3))]
    ]

def calculator(command):
    try:
        result = eval(command)
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result
    except Exception:
        return "Error..."

def interface():
    display = ""
    window = sg.Window("Calculator", layout(), element_justification="center")

    while True: #NÇÃO ESQUECE DE FECHAR ESSE LOOP
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*", "-", "+", "(", ")"]:
            display += str(event)
            window["-DISPLAY-"].update(display)
        
        elif event == "clear":
            display = ""
            window["-DISPLAY-"].update(display)
        
        elif event == "%":
            try:
                result = eval(display) / 100
                display = str(result)
                window["-DISPLAY-"].update(display)
            except:
                display = "Error..."
                window["-DISPLAY-"].update(display)
        
        elif event == "=":
            display = calculator(display)
            window["-DISPLAY-"].update(display)

    window.close()

if __name__ == "__main__":
    main()
