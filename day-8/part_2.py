msg = open('input.txt').read().splitlines()[0]

w = 25
h = 6
layer_size = w * h
image = [i for i in msg[:layer_size]]
layer_index = 1
while True:
    if layer_index * layer_size >= len(msg):
        break
    layer = msg[layer_size * layer_index:layer_size * (layer_index + 1)]
    layer_index += 1
    for index, px in enumerate(layer):
        if image[index] == '2' and px != '2':
            image[index] = px

for i in range(len(image) // w):
    print(['.' if i == '0' else 'X' for i in image[w * i:w * (i + 1)]])
