#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    dir_name = dir(hidden_4)
    for i in range(len(dir_name)):
        if dir_name[i][:2] != '__':
            print(dir_name[i])
