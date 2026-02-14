**PT-BR**

🚗 Sistema de Gestão de Estacionamento
Um sistema robusto de gestão de estacionamentos desenvolvido em Python. O projeto utiliza Programação Orientada a Objetos para gerenciar o fluxo de veículos, ocupação de vagas e cálculo automatizado de tarifas com base no tempo de permanência.

🛠️ Funcionalidades
Check-in Flexível: Registro completo de veículos (placa, modelo, cor) com suporte a escolha de vaga manual ou seleção automática por algoritmo de proximidade.

Cálculo de Tarifas em Tempo Real: Sistema de faturamento preciso que calcula o valor devido com base nos segundos exatos de permanência.

Mapa de Ocupação: Visualização dinâmica do status das vagas (Disponível/Ocupado) com feedback visual colorido via terminal.

Persistência de Dados: Integração com sistema de arquivos JSON para garantir que nenhum dado seja perdido entre sessões do programa.

Busca por Placa: Localização rápida de veículos estacionados e exibição detalhada de informações de entrada.

⚙️ Arquitetura Técnica
O sistema foi modularizado para facilitar a manutenção:

Classe car: Atua como um DTO (Data Transfer Object) para os dados do veículo.

Classe parking: Contém o motor lógico, gerenciando o dicionário de vagas e as operações de persistência.

Módulo Utilities: Biblioteca externa customizada para garantir a integridade dos inputs do usuário e padronização visual.

**ENGLISH**

🚗 Parking Management System
A robust parking management system developed in Python. This project utilizes Object-Oriented Programming (OOP) to manage vehicle flow, spot occupancy, and automated fee calculation based on real-time stay duration.

🛠️ Features
Flexible Check-in: Full vehicle registration (license plate, model, color) with support for manual spot selection or automated vacancy assignment.

Real-Time Billing: Precise pricing engine that calculates the total amount due based on the exact seconds elapsed.

Occupancy Mapping: Dynamic visualization of spot status (Available/Occupied) with color-coded terminal feedback.

Data Persistence: JSON-based storage integration to ensure all records are maintained across program restarts.

License Plate Lookup: Fast vehicle retrieval and display of check-in details and current accrued fees.

⚙️ Technical Architecture
The system is modularized for better maintainability:

car Class: Acts as a DTO (Data Transfer Object) for vehicle-related data.

parking Class: The core logic engine, managing the spot dictionary and data persistence operations.

Utilities Module: A custom external library used to ensure user input integrity and visual consistency.
