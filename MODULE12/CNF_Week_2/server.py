import socket
import csv
# def readFile():

    

def respondClient():
    rollnumber = []
    secretquestion =[]
    secretanswer = []

    with open('data.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            rollnumber = row[0]
            secretquestion = row[1]
            secretanswer = row[2]
            # print(secretanswer)

    csvFile.close()


    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        if (data == 'MARK_ATTENDANCE'):
                if data not in rollnumber:
                    print("ROLLNUMBER-NOT FOUND")
                else :
                    c.send(secretquestion.encode())
        

def main():
    host = '10.2.137.32'
    port = 1558
    
    s = socket.socket()
    s.bind((host, port))


    s.listen(10)
    print("Server connected")

    while True:
        c, addr = s.accept()
        print("connection from: " + str(addr))
        rollnum = c.recv(1024).decode()
        threading.Thread(target = respondClient, args =(c, addr)).start()
        # if (rollnum == "")

    # s.close()



if __name__ == '__main__':
    main()
