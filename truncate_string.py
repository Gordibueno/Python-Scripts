# Truncate a String

def truncate(string, number):
    if len(string) > number:
        print string[0:number+1] + "..."
        print "String is " + str(len(string)) + " characters in length"
    else:
        print "String is Less Than or Equal to %d" % number