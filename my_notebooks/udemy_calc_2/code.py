def riemann(a, b, n, f, side='l'):
  delta = (b-a)/float(n)
  if(side == 'l'):
    return sum(map(f, np.linspace(a,b-delta,n)))
  elif(side == 'r'):
    return sum(map(f, np.linspace(a, b-delta, n)+delta))
  elif(side == 'm'):
    return sum(map(f, np.linspace(a, b-delta, n)+delta/2.0))
  else:
    raise ValueError("side must be l, r or m")
