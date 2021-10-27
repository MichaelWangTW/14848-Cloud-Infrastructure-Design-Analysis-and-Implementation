def executeHadoop():
    print("Execute Apache  Hadoop")
    print("===================================")
    return
def executeSpark():
    print("Execute Apache Spark")
    print("===================================")
    return
def executeJupyter():
    print("Execute Jupyter Notebook")
    print("===================================")
    return
def executeSonarQubeSonarScanner():
    print("Execute SonarQube and SonarScanner")
    print("===================================")
    return
if __name__ == "__main__":
    while True:
        print("welcome to Big Data Processing Application")
        print("Please type the number that corresponds to which application you would like to run: ")
        print("1. Apache  Hadoop")
        print("2. Apache Spark")
        print("3. Jupyter Notebook")
        print("4. SonarQube and SonarScanner")
        print("5. Exit")
        print("Type the number heare >")
        choice = input()
        if choice == "1":
            executeHadoop()
        elif choice =="2":
            executeSpark()
        elif choice == "3":
            executeJupyter()
        elif choice == "4":
            executeSonarQubeSonarScanner()
        elif choice == "5":
            break 

            

    