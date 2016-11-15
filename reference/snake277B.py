from pygame import*;d=display;y,D,S=s=[15,16,17];n,p,x=D,99,d.set_mode([225]*2).fill
while s.count(S)%2*S%n*(S&240):
 for e in event.get(2):D=(-1,-n,n,1)[e.key&3]
 s=s[p!=S:]+[S+D];x(-1)
 if p==S:p=s[0]
 for i in[p]+s:x(0,((i-1)%n*y,(i-n)/n*y,y,y))
 d.flip();S+=D;time.wait(99)