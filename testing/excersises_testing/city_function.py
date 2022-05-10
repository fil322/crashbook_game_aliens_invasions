def get_city_country(city, country, population=0):
    """Возвращает строку: Город, Страна"""
    city_country = f'{city}, {country}'
    if population:
        return city_country.title() + f' - population {population}'
    else:
        return city_country.title()