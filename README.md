# 👧나이 성별 예측 프로그램👨
<h3>사진, 비디오에서 얼굴을 감지하고 분석하는 애플리케이션으로</h3> <p>실시간 비디오 스트림에서 얼굴을 감지하고 해당 얼굴의 성별과 나이를 분석하며, 분석 결과를 저장하는 스냅샷 기능을 제공합니다.</p>

<h2>팀 구성</h2>
+ 3명 ( [김연수] [손지연] [안유진] )

<h2>구현 기능</h2>
<ul>
<li>얼굴 감지: OpenCV의 DNN(Dependency Neural Network) 모듈을 사용하여 얼굴을 감지합니다.</li>
<li>성별 분석: 사전 훈련된 gender_net.caffemodel 모델을 사용하여 얼굴의 성별을 분석합니다.</li>
<li>나이 추정: 사전 훈련된 age_net.caffemodel 모델을 사용하여 얼굴의 나이를 추정합니다.</li>
<li>결과 표시: 감지된 얼굴 주변에 사각형 박스를 그리고, 해당 얼굴의 성별과 나이를 텍스트로 표시합니다.</li>
<li>스냅샷 저장: 스냅샷 버튼을 클릭하여 현재 프레임을 이미지 파일로 저장하고, 얼굴 분석 결과를 CSV 파일로 저장합니다.</li>
</ul>

<h2>사용 기술 및 환경</h2>
+언어: Python
+컴퓨터 비전 라이브러리: OpenCV
+딥러닝 프레임워크: Caffe
+모델: opencv_face_detector, age_net, gender_net
+의존성 관리: pip
+운영 체제: Windows, macOS

<h2>설치 방법</h2>
<ul>
   <li>OpenCV</li>
	   pip install opencv-python
   <li>argparse</li>
	   pip install argparse

<h2>의존성</h2>
<ul>
   <li>OpenCv</li>
   <li>추 가 예 정</li>
<ul>

<h2>사용 방법</h2>
<ul>
  <li>웹캠</li>
	python <실행 파일명>
  	python main.py
</ul>
<ul>
 <li>사진</li>
  	python <실행 파일명> --image <이미지 파일>
	python main.py --image girl1.jpg
</ul>
<p>중단 방법: <b>Ctrl + C </b></p>

<h2>라이선스 및 연락처</h2>
<h3>라이선스</h3>
<p></p>
<h3>연락처</h3>
<p>손지연, sjy7392@naver.com</p>
