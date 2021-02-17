class pup() :
    def __init__(self , a):
        self.name = '나는'
        print(a)
    def __del__(self):
        print(f'{self.name} 갑니다' )
# aa.name = '아이듀' 
aa = pup('생성자에 a받았을때')
aa.name = '남그녛ㅇ'
print(aa.name)

class Faker():
    def __init__(self,a):
        