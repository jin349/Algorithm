#단일 함수

def count_word(word_list):
    #print(word_list)
    cnt=0
    for i in word_list:
        for j in i:
            cnt+=1

    return cnt

if __name__ == '__main__':
    mylst = ['Hello']
    result = count_word(mylst)
    print(result)
