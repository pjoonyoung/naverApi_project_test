import urllib.request
import json

client_id= 'HGZc6HyAGt2A5c0Vnag_'
client_secret= 'lDhVQzxIZr'

def getRequestUrl(url):
    req = urllib.request.Request(url) # 네이버 서버에 보낼 요청객체를 생성
    req.add_header("X-Naver-Client-Id",client_id) # 위에서 만들어진 요청객체에 client_id를 포함시킴
    req.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(req) # 네이버서버에 요청객체 req를 전달하여 응답을받아 reponse에 저장
    if response.getcode() == 200: # 응답코드가 200이면 정상호출
        print('호출성공!!')
        ret = response.resd().decode('utf-8')
        return ret
    else:
        print('호출에러-호출에러코드:',response.getcode())
        print('에러발생 주소:',url)
        return None


def getNaverSearch(node, srcText, start, display):
    baseUrl = "https://openapi.naver.com/v1/search" # 네이버 기본 api 주소
    node = "/%s.json" % node
    param = "?query=%s" % srcText
    api_url = baseUrl + node + param # "https://openapi.naver.com/v1/search/news.json?query="
    reponseDecode = getRequestUrl(api_url)  # 호출성공시 디코딩된 응답 데이터를 저장

def main():
    node = 'news' # 검색카테고리를 news로 설정
    srcText = input("원하시는 검색어를 입력하세요:") # 검색어를 입력
    jsonResponse = getNaverSearch(node, srcText, 1, 100) # news 카테고리에서 입력된 검색어가 들어간 뉴스를 1~100 추출하여 응답

    for post in jsonResponse: # 응답된 json 에서 기사를 추출
        pass

    with open('파일이름', 'w', encoding='utf-8') as outfile:
        jsonFile = json.dumps()
        outfile.write(jsonFile)

if __name__ == '__main__':
    main()