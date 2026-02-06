import os, json, time
from datetime import datetime



def erase_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class car:
    def __init__(self, license_plate, car_model, color, time, parking_lot):
        self.license_plate = license_plate
        self.car_model = car_model
        self.color = color
        self.time = time
        self.parking_lot = parking_lot

class parking:
    def __init__(self):
        self.parking_lot = {
            "A1": None, "A2": None, "A3": None, "A4": None, "A5": None, "A6": None, "A7": None, "A8": None, "A9": None,
            "B1": None, "B2": None, "B3": None, "B4": None, "B5": None, "B6": None, "B7": None, "B8": None, "B9": None,
            "C1": None, "C2": None, "C3": None, "C4": None, "C5": None, "C6": None, "C7": None, "C8": None, "C9": None
        }

    def menu(self):
        while True:
            erase_screen()
            print("1. Check-in\n2. Check-out\n3. Listar carros\n4. Sair")
            choose = input()
            try:
                float(choose)
            except ValueError:
                print("ERRO! Digite um número!")
                input()
                return
            
            if float(choose) < 1 or float(choose) > 4:
                print("ERRO! Escolha um número válido!")
                input()
                return
            break

        if choose == '1':
            erase_screen()
            print("Qual a PLACA, MODELO e COR?")
            plate = input()
            model = input()
            color = input()
            hour = datetime.now()
            for spot, vehicle in self.parking_lot.items():
                if vehicle is None:
                    lot_parking = spot
                    break

            self.check_in(plate, model, color, hour, lot_parking)
            erase_screen()
            print("VEICULO CADASTRADO!")
            print(f"VAGA: {lot_parking}")
            input()

        elif choose == '3':
            self.show_parking()

    def check_in(self, license_plate, model, color, time, parking_lot):
        self.parking_lot[parking_lot] = car(license_plate, model, color, time, parking_lot)
        
    def show_parking(self):
        erase_screen()
        for spot, vehicle in self.parking_lot.items():
            if vehicle is None:
                print(f"Vaga {spot}: [ VAZIA ]")
            else:
                print(f"Vaga {spot}: [ {vehicle.license_plate} - {vehicle.car_model} ]")

        input()

estacionamento = parking()

while True:
    estacionamento.menu()
