Families = {
    'charley': {
        'sam': {'Boxy', 'Rosy'},
        'Nila': {'pepsi'}
    },
    'Devi': {
        'Tommy': {'Tony'},
        'Timmy': {'Hamster'},
        'Tammy': {'Hamster'}
    },
    'Carlos': {
        'Diego': 'Cat',
        'ferret': 'Fox'
    }
}

for parent, children in Families.items():
    print(f"{parent} has {len(children)} kid(s):")
    print(", and ".join([str(child) for child in [*children]]))
