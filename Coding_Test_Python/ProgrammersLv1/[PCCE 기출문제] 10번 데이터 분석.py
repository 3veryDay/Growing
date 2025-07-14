def solution(data, ext, val_ext, sort_by):
    lst = []
    dic= {}
    dic["code"] = 0
    dic["date"] = 1
    dic["maximum"] = 2
    dic["remain"] = 3
    
    for da in data :
        if int(da[dic[ext]]) < val_ext :
            lst.append(da)
    answer = lst.sort(key = lambda x : x[dic[sort_by]])
    return lst
