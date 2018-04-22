#~ syntax:
#~ {<var>:<var> for <var> in <sequence>}
#~ {<var>:<var> for <var> in <sequence> if <var with condition>}

print {"A"+str(x):x for x in range(10)}
print {x:x for x in range(10) if x>5}