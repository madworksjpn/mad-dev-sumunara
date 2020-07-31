import json

def lambda_handler(event, context):
    people = event['people']
    amount = event['amount']
    result = amount / people
    
    return {
        'people': people,
        'amount': amount,
        'result': result
    }
#         print('割り勘日本語ver')

# amount = int(input('金額を入力>>'))

# people = int(input('人数を入力>>'))

# pay = int(amount / peo)

# print(f'割り勘すると一人あたり{pay}円です。')