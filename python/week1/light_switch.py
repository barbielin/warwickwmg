def toggle_light(light_on:bool):
    if light_on:
        light_on=False
        print("light turned off")
    else:
        light_on=True
        print("light turned on")
toggle_light(True)
