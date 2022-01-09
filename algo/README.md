ใส่ wordList โดยแยกด้วย space 
ex. ถ้าอยากได้ list ["ab","bc","cd"] ให้พิมพ์ ab bc cd
ใส่ target 
ex. abcd

#Code Explanation
def solve(wordList,target) :
    wordList.sort()
    for i in wordList :
        if i == target[:len(i)] :
            tmp = target[len(i):]
            if wordList[bisect.bisect_left(wordList,tmp)] == tmp :
                return (i,tmp)
    return

โค้ดเริ่มจากการ sort wordList เพื่อให้ใช้ bisect ได้ โดยเราจะไล่ทุกตัวใน wordList ใช้เวลา n แล้วในแต่ละลูป จะเช็คว่า i เป็นส่วนหน้าของ target มั้ย ถ้าใช่ก็จะไปใช้ bisect เพื่อหาว่าใน wordList มีส่วนหลังของ target มั้ย ซึ่งใช้เวลา log n

time complexity : O(n log n)