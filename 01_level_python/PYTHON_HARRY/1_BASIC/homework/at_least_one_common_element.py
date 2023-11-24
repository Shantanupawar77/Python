from unittest import result


def common_list(L1,L2):
    return False

    for x in L1:
        for y in L2:
            if x==y:
                result= True

                return result
                break
    return result
a=[2,3,45,67,673]
b=[2,3,45,67,673]
print(common_list(a,b))

