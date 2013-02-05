import gdb
class MyBreakpoint (gdb.Breakpoint):
  def __init__(self,name, kind):
    print "asasd"
    super(gdb.Breakpoint, self).__init__ (name,kind)

    
  def stop (self):
    print 'wtf'
    inf_val = gdb.parse_and_eval("$eax")
    print inf_val
    print 'stopped'
    if inf_val == 3:
      return True
    return False

MyBreakpoint("main", gdb.BP_BREAKPOINT)
