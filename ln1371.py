def throws():
    return 5/1


try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except Exception :
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup'
)