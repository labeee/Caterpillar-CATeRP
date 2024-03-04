import math


temps = {
    'temp_frontal': 20,
    'temp_posterior': 50,
    'temp_teto': 22,
    'temp_piso': 20,
    'temp_lat_direita': 27,
    'temp_lat_esquerda': 26
}

for key in temps:
    temps[key] += 273.15

room = {
    'largura': 2,
    'comprimento': 4,
    'altura': 3,
    'pos_x': 1.2,
    'pos_y': 1,
    'pos_z': 1
}

coordinates = {
    'dist_frontal': room['pos_y'],
    'dist_posterior': room['comprimento'] - room['pos_y'],
    'dist_piso': room['pos_z'],
    'dist_teto': room['altura'] - room['pos_z'],
    'dist_lat_direita': room['pos_x'],
    'dist_lat_esquerda': room['largura'] - room['pos_x'],
}

def ort_ff(a: float, b: float, c: float) -> float:
    """
    Calculates the orthogonal form factor.

    Args:
        a (float): The perpendicular measurement from c.
        b (float): The rest.
        c (float): The distance from the center of the plain to the reference point.

    Returns:
        form_factor (float): The orthogonal form factor.
    """

    x = a / b
    y = c / b

    form_factor = (1 / (2 * math.pi)) * (math.atan(1 / y) - (y / math.sqrt(x**2 + y**2)) * math.atan(1 / math.sqrt(x**2 + y**2)))
    return round(form_factor, 10)

def par_ff(a: float, b: float, c: float) -> float:
    """
    Calculates the paralel form factor.

    Args:
        a (float): The perpendicular measurement from c.
        b (float): The rest.
        c (float): The distance from the center of the plain to the reference point.

    Returns:
        form_factor (float): The paralel form factor.
    """
    x = a / c
    y = b / c

    form_factor = (1 / (2 * math.pi)) * ((x / math.sqrt(1 + x**2)) * math.atan(y / math.sqrt(1 + x**2)) + (y / math.sqrt(1 + y**2)) * math.atan(x / math.sqrt(1 + y**2)))
    return round(form_factor, 10)

def calculate_radiant_temperature():
    ort_ff_frontal_dict = {
        'ff_teto_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
        'ff_teto_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
        'ff_piso_dir': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
        'ff_piso_esq': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
        'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
        'ff_lat_dir_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita']),
        'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_esq_cima': ort_ff(a=coordinates['dist_frontal'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda'])
    }

    ort_ff_posterior_dict = {
        'ff_teto_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_teto']),
        'ff_teto_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_teto']),
        'ff_piso_esq': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_esquerda'], c=coordinates['dist_piso']),
        'ff_piso_dir': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_lat_direita'], c=coordinates['dist_piso']),
        'ff_lat_esq_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_esq_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_esquerda']),
        'ff_lat_dir_baixo': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_piso'], c=coordinates['dist_lat_direita']),
        'ff_lat_dir_cima': ort_ff(a=coordinates['dist_posterior'], b=coordinates['dist_teto'], c=coordinates['dist_lat_direita'])
    }

    par_ff_dict = {
        'ff_frontal_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_frontal']),
        'ff_frontal_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_frontal']),
        'ff_posterior_quad_1': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_2': par_ff(b=coordinates['dist_teto'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_3': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_direita'], c=coordinates['dist_posterior']),
        'ff_posterior_quad_4': par_ff(b=coordinates['dist_piso'], a=coordinates['dist_lat_esquerda'], c=coordinates['dist_posterior'])
    }

    conferencia = {
        'sum_ff_frontal': round((sum(ort_ff_frontal_dict.values()) + par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 10),
        'sum_ff_posterior': round((sum(ort_ff_posterior_dict.values()) + par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 10)
    }

    ajuste_frontal = 0
    ajuste_posterior = 0

    if conferencia['sum_ff_frontal'] != 1:
        ajuste_frontal = conferencia['sum_ff_frontal']
        ajuste_frontal = 1 - ajuste_frontal
        ajuste_frontal = ajuste_frontal / 4
    
    if conferencia['sum_ff_posterior'] != 1:
        ajuste_posterior = conferencia['sum_ff_posterior']
        ajuste_posterior = 1 - ajuste_posterior
        ajuste_posterior = ajuste_posterior / 4

    result_data = {
        'ff_frontal_total': round((par_ff_dict['ff_frontal_quad_1'] + par_ff_dict['ff_frontal_quad_2'] + par_ff_dict['ff_frontal_quad_3'] + par_ff_dict['ff_frontal_quad_4']), 10),
        'ff_posterior_total': round((par_ff_dict['ff_posterior_quad_1'] + par_ff_dict['ff_posterior_quad_2'] + par_ff_dict['ff_posterior_quad_3'] + par_ff_dict['ff_posterior_quad_4']), 10),
        'ff_frontal_lat_dir_total': round(((ort_ff_frontal_dict['ff_lat_dir_baixo'] + ort_ff_frontal_dict['ff_lat_dir_cima']) + ajuste_frontal), 10),
        'ff_frontal_lat_esq_total': round(((ort_ff_frontal_dict['ff_lat_esq_baixo'] + ort_ff_frontal_dict['ff_lat_esq_cima']) + ajuste_frontal), 10),
        'ff_posterior_lat_dir_total': round(((ort_ff_posterior_dict['ff_lat_dir_baixo'] + ort_ff_posterior_dict['ff_lat_dir_cima']) + ajuste_posterior), 10),
        'ff_posterior_lat_esq_total': round(((ort_ff_posterior_dict['ff_lat_esq_baixo'] + ort_ff_posterior_dict['ff_lat_esq_cima']) + ajuste_posterior), 10),
        'ff_frontal_teto_total': round(((ort_ff_frontal_dict['ff_teto_dir'] + ort_ff_frontal_dict['ff_teto_esq']) + ajuste_frontal), 10),
        'ff_frontal_piso_total': round(((ort_ff_frontal_dict['ff_piso_dir'] + ort_ff_frontal_dict['ff_piso_esq']) + ajuste_frontal), 10),
        'ff_posterior_teto_total': round(((ort_ff_posterior_dict['ff_teto_dir'] + ort_ff_posterior_dict['ff_teto_esq']) + ajuste_posterior), 10),
        'ff_posterior_piso_total': round(((ort_ff_posterior_dict['ff_piso_dir'] + ort_ff_posterior_dict['ff_piso_esq']) + ajuste_posterior), 10)
    }

    radiant_temperatures = {
        'frontal': round((((temps['temp_frontal']**4)*result_data['ff_frontal_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_frontal_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_frontal_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_frontal_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_frontal_piso_total']))**0.25, 10),
        'posterior': round((((temps['temp_posterior']**4)*result_data['ff_posterior_total']) + ((temps['temp_lat_direita']**4)*result_data['ff_posterior_lat_dir_total']) + ((temps['temp_lat_esquerda']**4)*result_data['ff_posterior_lat_esq_total']) + ((temps['temp_teto']**4)*result_data['ff_posterior_teto_total']) + ((temps['temp_piso']**4)*result_data['ff_posterior_piso_total']))**0.25, 10)
    }

    radiant_temperatures['frontal_celsius'] = round((radiant_temperatures['frontal'] - 273.15), 10)
    radiant_temperatures['posterior_celsius'] = round((radiant_temperatures['posterior'] - 273.15), 10)
    radiant_temperatures['assimetry'] = round(abs(radiant_temperatures['frontal'] - radiant_temperatures['posterior']), 10)

    return ort_ff_frontal_dict, ort_ff_posterior_dict, par_ff_dict, conferencia, ajuste_frontal, ajuste_posterior, result_data, radiant_temperatures

if __name__ == '__main__':
    ort_ff_frontal_dict, ort_ff_posterior_dict, par_ff_dict, conferencia, ajuste_frontal, ajuste_posterior, result_data, radiant_temperatures = calculate_radiant_temperature()
    print('\n')
    print('Temperature in Kelvin')
    print(temps)
    for key in temps:
        temps[key] -= 273.15
    print('Temperature in Celsius')
    print(temps)
    print('\n')
    print('Room')
    print(room)
    print('\n')
    print('Coordinates')
    print(coordinates)
    print('\n')
    print('Orthogonal Frontal Form Factor')
    print(ort_ff_frontal_dict)
    print('\n')
    print('Orthogonal Posterior Form Factor')
    print(ort_ff_posterior_dict)
    print('\n')
    print('Paralel Form Factor')
    print(par_ff_dict)
    print('\n')
    print('Somatory of Form Factors')
    print(conferencia)
    print('\n')
    print('Ajuste frontal e posterior')
    print(round(ajuste_frontal*4, 10), ' / ', round(ajuste_posterior*4, 10))
    print('Dividindo por 4:')
    print(round(ajuste_frontal, 10), ' / ', round(ajuste_posterior, 10))
    print('\n')
    print('Result Data')
    print(result_data)
    print('\n')
    print('Radiant Temperatures')
    print(radiant_temperatures)
    print('\n')