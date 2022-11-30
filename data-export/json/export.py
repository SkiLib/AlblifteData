import json

def export(outfile):
    alblifte = []
    with open('../../data/_ID.json', 'r')  as f:
        IDs = json.load(f)

    for ID in IDs:
        with open(f'../../data/{ID["ID"]}.json', 'r') as f:
            data = json.load(f)
            lift = {}
            lift['ID'] = ID['ID']
            lift['Name'] = ID['Name']
            lift['Ort'] = data['Ort']
            lift['Infrastruktur'] = data['Infrastruktur']
            lift['SocialMedia'] = data['SocialMedia']
            alblifte.append(lift)

    with open(outfile, "w") as write_file:
        json.dump(alblifte, write_file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    export('Alblifte.json')

# EOF
