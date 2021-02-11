import json

class makeText(object):
    """
    이 클래스는 apiCaller.py의 API 호출값 XML을 전처리하여 만든 JSON파일로 텍스트를 만들어 반환합니다.
    
    1) makeText(self)
    텍스트 만들어 반환하는 메소드입니다.
    
    """
    def __init__(self):
        with open('Datas/smtpSendDatas.json') as w:
            self.data = json.load(w)
    
    def makeText(self):
        completedText = '{} 코로나19 정보\n\n\n총 확진자 수 : {}명\n전체 사망자 수 : {}명\n전일대비 확진자 증가 수 :{}명\n전일대비 사망자 증가수 : {}명\n누적확진률 : {}%\n\n\n<최신 보건복지부 브리핑>\n{} : {}\n{} : {}\n\n\n\n\n\n\n\n데이터 제공 : 대한민국 행정안전부 공공데이터 포털\n서비스 제공자 : Hoplin (https://github.com/J-hoplin1)'.format(self.data["dataDate"],self.data["data"]["totalDecidedPatient"],self.data["data"]["totalDeath"],self.data["data"]["todayDecidedPatient"],self.data["data"]["increasedDeath"],self.data["data"]["CumulatedConfirmPercentage"],self.data["data"]["mainBrief1"][0],self.data["data"]["mainBrief1"][1],self.data["data"]["mainBrief2"][0],self.data["data"]["mainBrief2"][1])
        return completedText
