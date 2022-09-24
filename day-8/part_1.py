msg = open('input.txt').read().splitlines()[0]

count = 999999999
top_layer = 0
layer_count = 0
layer_size = 25 * 6
while True:
    if layer_count * layer_size >= len(msg):
        break
    layer = msg[layer_size * layer_count:layer_size * (layer_count + 1)]
    layer_count += 1
    num_0 = layer.count('0')
    if num_0 < count:
        count = num_0
        top_layer = layer

print(top_layer.count('1') * top_layer.count('2'))