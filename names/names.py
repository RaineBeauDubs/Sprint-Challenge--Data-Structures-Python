import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# original code, ran in 15.5 seconds:
#for name_1 in names_1:
    #for name_2 in names_2:
        #if name_1 == name_2:
            #duplicates.append(name_1)


def find_diff(l1, l2):
    dupes = [i for i in l1 + l2 if i in l1 and i in l2]
    dupe_list = []
    for i in dupes:
        if i not in dupe_list:
            dupe_list.append(i)
    return dupe_list


duplicates = find_diff(names_1, names_2)

# runtime between 4.8 seconds and 5.5 seconds! *hands_party* I don't think it was exactly how I was supposed to do it, but it works!



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

