try:
    # Open file simple and w as the second param(write/save)
    f = open("simple.txt", "w")  # r for read  w=write/save
    f.write("test write to simple text!")
except:
    print("error: Could not find file or read data!")
finally:    # FINALYL STILL RUNS IT EVEN IF ERROR HAS OCCURED!*******
    print("I always work!") # WILL WORK NO MATTER WHAT


# else:
#     print("success!")
#     f.close()
# print("hello world")


    # HOW TO OPEN AND WRITE TO FILES!
