import zlib, struct, math
def make(path, N):
    bg = (26, 29, 43)
    px = [[bg] * N for _ in range(N)]
    def circle(cx, cy, r, col):
        for y in range(max(0, int(cy - r - 1)), min(N, int(cy + r + 2))):
            for x in range(max(0, int(cx - r - 1)), min(N, int(cx + r + 2))):
                if math.hypot(x + 0.5 - cx, y + 0.5 - cy) <= r:
                    px[y][x] = col
    cols = [(255,77,109),(255,159,28),(255,214,10),(124,252,0),(0,212,255),(77,124,255),(180,77,255)]
    n = 14
    r = N * 0.075
    for i in range(n):
        t = i / (n - 1)
        x = N * (0.26 + 0.48 * t)
        y = N * (0.62 - 0.22 * t + 0.07 * math.sin(t * 6.28))
        circle(x, y, r, cols[i % 7])
    hx = N * 0.74
    hy = N * (0.62 - 0.22 + 0.07 * math.sin(6.28))
    circle(hx, hy, r * 1.25, (124, 252, 0))
    for s in (-1, 1):
        circle(hx + N * 0.03, hy + s * N * 0.04, N * 0.028, (255, 255, 255))
        circle(hx + N * 0.04, hy + s * N * 0.04, N * 0.014, (0, 0, 0))
    raw = b''.join(b'\x00' + bytes(c for p in row for c in p) for row in px)
    def chunk(tag, data):
        body = tag + data
        return struct.pack('>I', len(data)) + body + struct.pack('>I', zlib.crc32(body) & 0xffffffff)
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', N, N, 8, 2, 0, 0, 0)) \
        + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b'')
    open(path, 'wb').write(png)
make('icon-192.png', 192)
make('icon-512.png', 512)
print('icons OK')
