try:
    f = open('testfile', 'w')
    f.write("Write a test file")

except TypeError:
    print ("There was a type error!")    
except OSError:
    print ("OS Error occurred")
except:
    print ("All other exceptions")

finally:
    f.close()    
