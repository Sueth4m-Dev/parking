import os, json, time
from datetime import datetime
import Utilities as ut

# AJUSTE DE ACORDO COM SEU PREÇO
price_hour = 30
# -----------------

end_program = False
price_minute = price_hour / 60
price_seconds = price_minute / 60

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
        menu = [ut.color('Check-in', "green"), ut.color('Check-out', "red"), ut.color("Listar carros", "yellow"), ut.color('Buscar dados', "blue"), 'Sair']
        ut.erase_screen()
        ut.print_menu(menu)
        choose = ut.read_int('', 1, 5)

        if choose == 1:
            ut.erase_screen()
            print(f"Qual a {ut.color("PLACA", "yellow")}, {ut.color('MODELO', 'green')} e {ut.color("COR", 'blue')}?")
            plate = ut.read_name('Placa inválida!', 'A placa deve ter 7 caracteres!', False, 7, 7).upper()
            model = ut.read_name('Modelo inválido!', 'O modelo deve ter mais de 2 caracteres!', False).upper()
            color = ut.read_name('Cor inválida!', 'A cor deve ter mais de 2 caracteres!').upper()

            hour = datetime.now().strftime("%H:%M:%S")
            now = datetime.now()
            seconds_checkin = now.hour * 3600 + now.minute * 60 + now.second
            for spot, vehicle in self.parking_lot.items():
                if vehicle is None:
                    lot_parking = spot
                    break

            self.check_in(plate, model, color, hour, lot_parking, seconds_checkin)
            ut.erase_screen()
            print(ut.color('VEICULO CADASTRADO!', 'green'))
            print(f"VAGA: {lot_parking}")
            input()
            self.save_data()
        elif choose == 2:
            ut.erase_screen()
            print("Qual a placa do carro?")
            check_out_car = None
            license_plate = ut.read_name('Placa inválida!', 'A placa deve ter 7 caracteres', False, 7, 7).upper()
            for spot, vehicle in self.parking_lot.items():
                if vehicle is not None and vehicle.license_plate == license_plate:
                    check_out_car = vehicle
            if check_out_car == None:
                ut.erase_screen()
                ut.ERROR('CARRO NÃO ENCONTRADO')
                input()
                return

            ut.erase_screen()
            seconds_now = datetime.now().hour * 3600 + datetime.now().minute * 60 + datetime.now().second
            s = seconds_now - check_out_car.second
            hours_total = s // 3600
            minutes_total = (s % 3600) // 60
            second_total = s % 60
            price_total = s * price_seconds
            print(ut.color('CHECK-OUT CONCLUIDO!', 'green'))
            print(f"PLACA: {check_out_car.license_plate}")
            print(f"MODELO: {check_out_car.car_model}")
            print(f"VAGA: {check_out_car.parking_lot}")
            print(f"TEMPO: {hours_total:02d}:{minutes_total:02d}:{second_total:02d}")
            print(f"PREÇO: R${price_total:.2f}")
            self.parking_lot[check_out_car.parking_lot] = None
            input()
            self.save_data() 
        elif choose == 3:
            self.show_parking()
        elif choose == 4:
            ut.erase_screen()
            print("Qual a PLACA do carro?")
            plate_info = ut.read_name('PLACA INVÁLIDA!', 'A placa deve ter 7 caracteres', False, 7, 7).upper()
            car_info = None
            ut.erase_screen()
            for spot, vehicle in self.parking_lot.items():
                if vehicle is not None and vehicle.license_plate == plate_info:
                    car_info = vehicle
            if car_info == None:
                ut.ERROR('CARRO NÃO ENCONTRADO!')
                input()
                return
            
            seconds_now = datetime.now().hour * 3600 + datetime.now().minute * 60 + datetime.now().second
            s = seconds_now - car_info.second
            hours_total = s // 3600
            minutes_total = (s % 3600) // 60
            second_total = s % 60
            price_total = s * price_seconds

            print(f"INFORMAÇÕES - {plate_info}\n")
            print(f"Placa: {car_info.license_plate}")
            print(f"Modelo: {car_info.car_model}")
            print(f"Cor: {car_info.color}")
            print(f"Horário de entrada: {car_info.time}")
            print(f"Vaga: {car_info.parking_lot}")
            print(f"Tempo: {hours_total:02d}:{minutes_total:02d}:{second_total:02d}")
            print(f"Preço: R${price_total:.2f}")
            input()
        elif choose == 5:
            ut.erase_screen()
            print("Salvando dados...")
            time.sleep(0.5)
            print("Finalizando programa...")
            time.sleep(0.5)
            return True

    def check_in(self, license_plate, model, color, time, parking_lot, seconds):
        self.parking_lot[parking_lot] = car(license_plate, model, color, time, parking_lot, seconds)
        
    def show_parking(self):
        row = 0
        ut.erase_screen()
        for spot, vehicle in self.parking_lot.items():
            row += 1
            if row == 10:
                print()
                row = 1
            if vehicle is None:
                print(ut.color(f'Vaga {spot}: [ VAZIA ]', 'green'))
            else:
                print(ut.color(f'Vaga {spot}: [ {vehicle.license_plate} - {vehicle.car_model} ]', 'red'))
        input()

    def save_data(self):
        data_to_save = {}
        for spot, vehicle in self.parking_lot.items():
            if vehicle is not None:
                data_to_save[spot] = vehicle.__dict__
            else:
                data_to_save[spot] = None
        
        ut.save_data(data_to_save, 'parking_data.json')
    
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
end = False
while not end:
    end = estacionamento.menu()