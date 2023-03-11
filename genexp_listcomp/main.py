text = 'First second : third 12345'
elements = text.split()
suspend = (e for e in range(1000_000))

if __name__ == '__main__':
    print([e.capitalize() for e in elements])
    print(1000_000)