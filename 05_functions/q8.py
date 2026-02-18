def print_kwags(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

print_kwags(name='shaktiman',power='lazer')
print_kwags(name='shaktiman')
print_kwags(name='shaktiman',power='lazer',enemy='Dr. jackal')
