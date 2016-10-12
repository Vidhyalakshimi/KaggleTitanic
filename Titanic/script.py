import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb'))
header = csv_file_object.next()

data = []

for row in csv_file_object:
	data.append(row)

data = np.array(data)

passenger = np.size(data[0::,1].astype(np.float))
survived = np.sum(data[0::,1].astype(np.float))
proportion = survived / passenger

women_index = data[0::, 4] == 'female'
men_index = data[0::, 4] == 'male'

women = data[women_index, 1].astype(np.float)
men = data[men_index, 1].astype(np.float)

women_survivors = np.sum(women) / np.size(women)
men_survivors = np.sum(men) / np.size(men)


print passenger
print survived
print proportion
print women
print "men" + str(men)

print "women survivors %s" % women_survivors
print "men survivors " + str(men_survivors)