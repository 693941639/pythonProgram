import concurrent.futures

def test(n):
    return sum(i * i for i in range(n))

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(test, [1, 2, 3])

if __name__ == '__main__':
   main()