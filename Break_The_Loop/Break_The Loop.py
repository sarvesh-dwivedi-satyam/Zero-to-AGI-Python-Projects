def count_and_break():
    count = 1
    while count <= 100:
        if count == 15:
            break
        else:
            print(count)
        count += 1
    
if __name__ == '__main__' :
    count_and_break ()