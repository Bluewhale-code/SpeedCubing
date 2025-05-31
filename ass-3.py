from vpython import *


cube_size = 19
spacing = 20
positions = [-spacing, 0, spacing]


face_colors = {
    'U': color.white,   
    'D': color.yellow,  
    'F': color.green,  
    'B': color.blue,    
    'L': color.orange,  
    'R': color.red      
}


face_axes = {
    'U': (2, +spacing),
    'D': (2, -spacing),
    'F': (1, +spacing),
    'B': (1, -spacing),
    'L': (0, -spacing),
    'R': (0, +spacing)
}


cubelets = []  
rotating = False


def add_stickers(cubelet, x, y, z):
    stickers = []
    offset = (cube_size / 2) + 0.6
    sticker_size = cube_size * 0.92
  
    if z == spacing:
        stickers.append(box(
            pos=vector(x, y, z + offset),
            size=vector(sticker_size, sticker_size, 1),
            color=face_colors['U'],
            opacity=1
        ))

    if z == -spacing:
        stickers.append(box(
            pos=vector(x, y, z - offset),
            size=vector(sticker_size, sticker_size, 1),
            color=face_colors['D'],
            opacity=1
        ))

    if y == spacing:
        stickers.append(box(
            pos=vector(x, y + offset, z),
            size=vector(sticker_size, 1, sticker_size),
            color=face_colors['F'],
            opacity=1
        ))

    if y == -spacing:
        stickers.append(box(
            pos=vector(x, y - offset, z),
            size=vector(sticker_size, 1, sticker_size),
            color=face_colors['B'],
            opacity=1
        ))
   
    if x == -spacing:
        stickers.append(box(
            pos=vector(x - offset, y, z),
            size=vector(1, sticker_size, sticker_size),
            color=face_colors['L'],
            opacity=1
        ))

    if x == spacing:
        stickers.append(box(
            pos=vector(x + offset, y, z),
            size=vector(1, sticker_size, sticker_size),
            color=face_colors['R'],
            opacity=1
        ))
    return stickers


for x in positions:
    for y in positions:
        for z in positions:
            b = box(pos=vector(x, y, z), size=vector(cube_size, cube_size, cube_size), color=color.gray(0.15))
            stickers = add_stickers(b, x, y, z)
            cubelets.append({'box': b, 'pos': (x, y, z), 'stickers': stickers})


def get_face(face):
    axis, value = face_axes[face]
    return [c for c in cubelets if c['pos'][axis] == value]


def rotate_face(face, axis, origin):
    global rotating
    if rotating:
        return
    rotating = True
    facelets = get_face(face)
    angle = 0
    while angle < 90:
        rate(60)
        for c in facelets:
            c['box'].rotate(angle=radians(1), axis=axis, origin=origin)
            for s in c['stickers']:
                s.rotate(angle=radians(1), axis=axis, origin=origin)
        angle += 1
    rotating = False


def key_input(evt):
    key = evt.key.lower()
    if key == 'j': 
        rotate_face('U', vector(0, 0, 1), vector(0, 0, spacing))
    elif key == 's':  
        rotate_face('D', vector(0, 0, -1), vector(0, 0, -spacing))
    elif key == 'h': 
        rotate_face('F', vector(0, 1, 0), vector(0, spacing, 0))
    elif key == 'w': 
        rotate_face('B', vector(0, -1, 0), vector(0, -spacing, 0))
    elif key == 'd': 
        rotate_face('L', vector(-1, 0, 0), vector(-spacing, 0, 0))
    elif key == 'k':  
        rotate_face('R', vector(1, 0, 0), vector(spacing, 0, 0))

scene.bind('keydown', key_input)
scene.title = "VPython 3D Rubik's Cube Simulator (Colored Faces)"


