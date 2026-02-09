import os, json, time
from datetime import datetime

def erase_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class car:
    def __init__(self, license_plate, car_model, color, time, parking_lot, seconds):
        self.license_plate = license_plate
        self.car_model = car_model
        self.color = color
        self.time = time
        self.parking_lot = parking_lot
        self.second = seconds

class parking:
    def __init__(self):
        self.parking_lot = {
            "A1": None, "A2": None, "A3": None, "A4": None, "A5": None, "A6": None, "A7": None, "A8": None, "A9": None,
            "B1": None, "B2": None, "B3": None, "B4": None, "B5": None, "B6": None, "B7": None, "B8": None, "B9": None,
            "C1": None, "C2": None, "C3": None, "C4": None, "C5": None, "C6": None, "C7": None, "C8": None, "C9": None
        }
        self.load_data()

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
            hour = datetime.now().strftime("%H:%M:%S")
            now = datetime.now()
            seconds_checkin = now.hour * 3600 + now.minute * 60 + now.second
            for spot, vehicle in self.parking_lot.items():
                if vehicle is None:
                    lot_parking = spot
                    break

            self.check_in(plate, model, color, hour, lot_parking, seconds_checkin)
            erase_screen()
            print("VEICULO CADASTRADO!")
            print(f"VAGA: {lot_parking}")
            input()
            self.save_data()
        elif choose == '2':
            erase_screen()
            print("Qual a placa do carro?")
            license_plate = input()
            for spot, vehicle in self.parking_lot.items():
                if vehicle is not None and vehicle.license_plate == license_plate:
                    check_out_car = vehicle

            erase_screen()
            seconds_now = datetime.now().hour * 3600 + datetime.now().minute * 60 + datetime.now().second
            s = seconds_now - check_out_car.second
            hours_total = s // 3600
            minutes_total = (s % 3600) // 60
            second_total = s % 60
            print("CHECK-OUT CONCLUIDO!\n")
            print(f"PLACA: {check_out_car.license_plate}")
            print(f"MODELO: {check_out_car.car_model}")
            print(f"VAGA: {check_out_car.parking_lot}")
            print(f"TEMPO: {hours_total}:{minutes_total}:{second_total}")
            self.parking_lot[check_out_car.parking_lot] = None
            input()
            self.save_data()
        elif choose == '3':
            self.show_parking()
        elif choose == '4':
            erase_screen()
            print("Salvando dados...")
            time.sleep(0.5)
            print("Finalizando programa...")
            time.sleep(0.5)

    def check_in(self, license_plate, model, color, time, parking_lot, seconds):
        self.parking_lot[parking_lot] = car(license_plate, model, color, time, parking_lot, seconds)
        
    def show_parking(self):
        row = 0
        erase_screen()
        for spot, vehicle in self.parking_lot.items():
            row += 1
            if row == 10:
                print()
                row = 1
            if vehicle is None:
                print(f"Vaga {spot}: [ VAZIA ]")
            else:
                print(f"Vaga {spot}: [ {vehicle.license_plate} - {vehicle.car_model} ]")
        input()

    def save_data(self):
        data_to_save = {}
        for spot, vehicle in self.parking_lot.items():
            if vehicle is not None:
                data_to_save[spot] = vehicle.__dict__
            else:
                data_to_save[spot] = None
        
        with open('parking_data.json', 'w', encoding='utf-8') as arquivo:
            json.dump(data_to_save, arquivo, indent=4, ensure_ascii=False)
    
    def load_data(self):
        if os.path.exists('parking_data.json'):
            with open('parking_data.json', 'r', encoding='utf-8') as arquivo:
                data = json.load(arquivo)
                for spot, info in data.items():
                    if info is not None:
                        self.parking_lot[spot] = car(
                            info['license_plate'], 
                            info['car_model'], 
                            info['color'], 
                            info['time'], 
                            info['parking_lot'], 
                            info['second']
                        )

estacionamento = parking()
while True:
    estacionamento.menu()


# VOCE ESTÁ TENTANDO SALVAR OS DADOS DOS CARROS NO JSON, E ACABOU SE DEPARANDO COM UM ERRO, 
# QUE ERRO? O JSON NAO CONSEGUE ARMAZENAR CLASSES, E VOCE ESTÁ PROCURANDO UMA ALTERNATIVA PRA ISSO