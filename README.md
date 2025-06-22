# Flight-Planning
A command-line tool to estimate the profitability of proposed commercial passenger flights between a UK airport (Liverpool John Lenon or Bournemouth International) and an overseas destination, based on routing, aircraft choice, seating seating configuration, and ticket pricing.

## Files used in this project:
- CODE_FINAL_Airports.py: Main Python script implementing all functionality
[ Detailed project report and documentation in docs folder]
- UKAirports.txt: UK airport codes and names
- OverseasAirports.txt: Overseas airport codes, names, and distances
- AirCraftType.txt: Aircraft type data (running cost, range, seat capcities)

## Features: 
- Airport Details: List and validate UK and overseas airport codes

- Aircraft Selection: Display aircraft specs and validate the user’s choice

- Seating Configuration: Input number of first-class seats and compute standard-class capacity

- Cost & Revenue Calculation: Calculate per‑seat operating cost, total flight cost, income from ticket sales, and overall profit

- Error Handling: Robust input checks (menus, integer parsing, invalid codes)

- Persistent Save: Interim entries saved to myfile.txt; option to clear all data and start fresh

## Installation:
- Python 3.x
- idlecolors module for colored terminal output
- All .txt data files should reside in the same directory as the script

## Usage:
### Run the script from the terminal:
python CODE_FINAL_Airports.py

### Follow the on‑screen menu:
1. Enter airport details: choose UK and overseas airports by 3‑letter code
2. Enter flight details: choose aircraft type and number of first‑class seats
3. Enter price plan & calculate profit: set ticket prices and view detailed cost/income breakdown
4. Clear data: reset all entries and delete myfile.txt
5. Exit

### Output (example):
After selecting option 3, the program will print a summary:

UK AIRPORT: LJL Liverpool John Lennon
OVERSEAS AIRPORT: CDG Charles de Gaulle
DISTANCE: 450 KM
FLIGHT COST PER SEAT: £XXX.XX
FLIGHT COST: £YYYY.YY
FLIGHT INCOME: £ZZZZ.ZZ
FLIGHT PROFIT: £PPPP.PP

Intermediate entries are saved to myfile.txt for persistence; choose 'Clear data' to delete it.

## Project Report
See the full project write‑up in the docs directory, which includes:
- Project specification and objectives
- System design (flowcharts, use‑case diagrams)
- Algorithm description and pseudocode
- Test plan and evaluation results
- Reflection and future improvements

Author: Aditi Bhat