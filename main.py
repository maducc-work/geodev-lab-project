import pandas as pd

def main():
    table = pd.read_csv("states.csv")
    print(table)

if __name__ == "__main__":
    main()
