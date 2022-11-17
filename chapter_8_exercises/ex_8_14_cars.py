def make_car(manufacturer, model, **make_car):
    """Returns car information"""
    make_car["manufacturer_info"] = manufacturer
    make_car["model_info"] = model
    return make_car

car = make_car("subaru", "outback", color="blue", tow_package=True)

print(car)