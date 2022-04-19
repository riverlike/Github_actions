# Base Image를 python3.8로 설정
FROM python:3.8
# 필요한 라이브러리인 tensorflow 설치, python:3.8이미지에 설치하는 것임
RUN pip install tensorflow
RUN pip install argparse
# 정의한 train.py를 도커 컨테이너 내 루트 디렉토리에 추가, python:3.8 이미지 루트 폴더에 안에  train.py추가
ADD test_train.py /
# "python /train.py" 명령어 실행
# $python train.py --hidden_units 512 
CMD ["python", "/test_train.py", "--hidden_units", "512"]
