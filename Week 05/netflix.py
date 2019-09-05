from operator import itemgetter

netflix_list_file = open("netflix.csv", "r")
netflix_list = []
for line in netflix_list_file:
    netflix_list.append(line.strip().split(","))


def get_max_column_width(column_number, table):
    max_width = 0
    for row in table:
        current_width = len(row[column_number])
        if current_width > max_width:
            max_width = current_width
    return max_width + 5


def display_netflix_list(netflix_list):
    netflix_list.sort(key=itemgetter(0))
    string_formatter = "{} {}. {:{}} Seasons: {:1}"
    title_column_width = get_max_column_width(0, netflix_list)
    print(title_column_width)
    for i in range(0, len(netflix_list)):
        complete = " "
        if netflix_list[i][-1] == "c":
            complete = "*"
        print(string_formatter.format(complete, i + 1, netflix_list[i][0], title_column_width, netflix_list[i][1]))
