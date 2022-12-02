import csv
def main():
    with open('player_list.csv', newline='\n') as csvfile:
        data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    print(data)
if __name__ == '__main__':
    main()