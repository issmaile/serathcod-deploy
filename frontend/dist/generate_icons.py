import struct, zlib

def create_png(width, height):
    """Create a valid PNG with a cyan centered square on black background."""
    def chunk(chunk_type, data):
        c = chunk_type + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    
    header = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
    
    raw = b''
    for y in range(height):
        raw += b'\x00'
        for x in range(width):
            margin = width // 6
            if margin <= x < width - margin and margin <= y < height - margin:
                raw += bytes([0, 240, 255])
            else:
                raw += bytes([0, 0, 0])
    
    idat = chunk(b'IDAT', zlib.compress(raw))
    iend = chunk(b'IEND', b'')
    return header + ihdr + idat + iend

for size, name in [(192, 'icon-192.png'), (512, 'icon-512.png'), (512, 'icon-512-maskable.png')]:
    with open(name, 'wb') as f:
        f.write(create_png(size, size))
    print(f'Created {name} ({size}x{size})')
