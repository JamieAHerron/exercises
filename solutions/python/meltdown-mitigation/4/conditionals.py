"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    
    product = temperature * neutrons_emitted
    
    return temperature < 800 and neutrons_emitted > 500 and product < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage_value = (generated_power/theoretical_max_power)*100

    if percentage_value >= 80:
        return 'green'
    if percentage_value >= 60:
        return 'orange'
    if percentage_value >= 30:
        return 'red'
    
    return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    check_result = temperature * neutrons_produced_per_second

    if check_result < (threshold * 0.9):
        return 'LOW'
    if check_result >= (threshold * 0.9) and check_result <= (threshold * 1.1):
        return 'NORMAL'
    
    return 'DANGER'
