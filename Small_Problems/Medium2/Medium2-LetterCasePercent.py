def letter_percentages(s):
    percents = {'lowercase': 0, 'uppercase': 0, 'neither': 0}
    for char in s:
        if char.islower():
            percents['lowercase'] += 1
        elif char.isupper():
            percents['uppercase'] += 1
        else:
            percents['neither'] += 1

    percents['lowercase'] = f"{percents['lowercase'] * 100 / len(s):.2f}"
    percents['uppercase'] = f"{percents['uppercase'] * 100 / len(s):.2f}"
    percents['neither'] = f"{percents['neither'] * 100 / len(s):.2f}"
    return percents


expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)