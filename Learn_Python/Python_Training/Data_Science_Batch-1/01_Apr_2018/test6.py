#~ syntax = [<var> for <var> in <sequence>]
#~          {<var> for <var> in <sequence>}
tmp = [x for x in range(100) if x%2==0 and x>10 and x<20]
print tmp
#~ [<var> for <var> in <sequence> if <var>%2]