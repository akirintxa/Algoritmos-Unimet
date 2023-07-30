def count_to_number(start, end):
    if start <= end:
        print(start)
        start += 1
        count_to_number(start, end)

def start():
    end = int(input("Introduza el número final: "))
    count_to_number(1, end)

#main()