import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

root = tk.Tk()
root.title("Weather App [By-Vedananda.N]")
root.geometry("400x400")


main_frame = tk.Frame(root, bg="#87CEEB")  
main_frame.pack(fill=tk.BOTH, expand=True)

def get_weather(city):
    API_key = "1e2b1dc4801948321a3ceb4abf238748"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city, country = result
    location_label.configure(text=f" {city}, {country} ", font=("Helvetica", 20, "bold"))
    
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C", font=("Helvetica", 14))
    description_label.configure(text=f"Description: {description}", font=("Helvetica", 14))


city_entry = tk.Entry(main_frame, font="Helvetica 18", bd=5)
city_entry.pack(pady=10)

search_button = tk.Button(main_frame, text="Search", command=search, font=("Helvetica", 14), bg="#90EE90") 
search_button.pack(pady=10)

location_label = tk.Label(main_frame, font=("Helvetica", 25), bg="#87CEEB")     
location_label.pack(pady=20)

icon_label = tk.Label(main_frame, bg="#87CEEB")     
icon_label.pack()

temperature_label = tk.Label(main_frame, font=("Helvetica", 20), bg="#87CEEB") 
temperature_label.pack()

description_label = tk.Label(main_frame, font=("Helvetica", 20), bg="#87CEEB")  
description_label.pack()

root.mainloop()
