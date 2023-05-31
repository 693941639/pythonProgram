import concurrent.futures

def test(n):
    return sum(i * i for i in range(n))

numbers = [10000000 + x for x in range(20)]

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        rel = executor.map(test, numbers)

    print(list(rel))

if __name__ == '__main__':
   main()
