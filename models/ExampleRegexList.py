#!/usr/bin/env python3
regexList = {
    'mail': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'name': 'name',
    
}
if 'mail' in regexList:
    print(regexList['mail'])
else:
    print("c'est faux")
