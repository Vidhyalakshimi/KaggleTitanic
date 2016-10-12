import csv as csv
import numpy as np

test_file = open('test.csv','rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()

prediction_file = open('genderclassmodel.csv','wb')
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow("PassengerId", "Survived")

for row in test_file_object:
	for j in 