import pandas as pd
import matplotlib.pyplot as plt

class AgriculturalAnalysis:
    def __init__(self):
        self.districts = [
            'Thiruvananthapuram', 'Kollam', 'Pathanamthitta',
            'Alappuzha', 'Kottayam', 'Idukki', 'Ernakulam',
            'Thrissur', 'Palakkad', 'Malappuram', 'Kozhikode',
            'Wayanad', 'Kannur', 'Kasaragod'
        ]
        
    def analyze_spice_production(self):
        # Sample data for Kerala spice production
        spice_data = {
            'Idukki': {'cardamom': 2340, 'pepper': 1200},
            'Wayanad': {'cardamom': 890, 'pepper': 2100},
            'Palakkad': {'cardamom': 450, 'pepper': 800}
        }
        return spice_data
    
    def generate_report(self):
        print("Kerala Agricultural Productivity Report")
        print("=====================================")
        data = self.analyze_spice_production()
        for district, crops in data.items():
            print(f"{district}: {crops}")
