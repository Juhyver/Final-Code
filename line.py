def get_line(x1, y1, x2, y2):
    xi = int(x1)
    xf = int(x2)
    yi = int(y1)
    
    points = []
    slope = abs((y2-y1)/(x2-x1))
    c = y1-x1*slope
    if xi <=xf:
        while xi <= xf:
            y = int(slope* xi + c)
            points.append((y, xi))
            xi += 1
    else:
        while xf <= xi:
            y = int(slope* xi + c)
            points.append((y, xi))
            xf += 1
        
    
    print(slope)
    print(points)
    return points

get_line(0,0,4,4)
