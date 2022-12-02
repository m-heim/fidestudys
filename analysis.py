import csv
import numpy
import os


def main():
    if not os.path.isfile("data.npy"):
        with open('players_list.csv', newline='\n') as csvfile:
            data = csv.reader(csvfile, delimiter=' ', quotechar='|')
            arr = numpy.array([row for row in data])
            numpy.save("data.npy", arr, allow_pickle=True)
    data = numpy.load("data.npy", allow_pickle=True)
    #for row in data:
    #    print(row)
    print("\n".join([str(list(item)) for item in enumerate(data[0])]))
    names = data[1:]
    print(names)


if __name__ == '__main__':
    main()