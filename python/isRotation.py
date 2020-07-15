def is_rotation(s1,s2):
    s3 = s1*2
    if s2 in s3:
       return True
    return False

#is_rotation(s,'urabhis') = True
#is_rotation('abaa', 'baba')= False
#is_rotation('aacd', 'acda']

if __name__ == "__main__":
    print(is_rotation('surabhi','urabhis'))
    print(is_rotation('', 'blablabla'))
    print(is_rotation('abaa', 'baba'))
