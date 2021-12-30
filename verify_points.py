def reachDestination(sx,sy,dx,dy):
    
    while dx >= sx and dy >= sy:
        if dx >= sx :
            sx,sy=sx,sy+sx
            if dy >= sy:
                sx,sy=sx+sy,sy
            else:
                return sx,sy
        else:
            return sx,sy
          
if sx==dx and sy==dy:
    print('True')
else:
  print('False')
    
