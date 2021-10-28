
# LINE Notify API 를 사용해서 알림을 전송 받기


outbound IP 정보를 LINE 메신저를 통해 전달받는다.

## LINE notify API 활용 글 
1) 커맨드 라인에서 LINE에 메시지를 보낼 수 있는 LINE Notify   
https://engineering.linecorp.com/ko/blog/using-line-notify-to-send-messages-to-line-from-the-command-line/   

2) LINE Notify에 스티커 송신 기능과 이미지 업로드 기능 추가   
https://engineering.linecorp.com/ko/blog/using-line-notify-to-send-stickers-and-upload-images/   

## LINE ACCESS TOKEN 관리자 페이지
https://notify-bot.line.me/my/

## LINE notify API docs
https://notify-bot.line.me/doc/en/

<br/><br/>
## 1. 개발 언어
Python 연습을 위해, Python 으로 구현했다.
<br/><br/>
## 2. 개발 환경
리눅스(우분투), VisualStudio Code 를 통한 날코딩
<br/><br/>
## 3. 실행방법
실행 스크립트(bash)를 만들고, cronjob 으로 실행

<pre><code>
################################################################################
# notifyOutboundIP_LINE.sh
# outbound IP 를 LINE 으로 보낸다.
################################################################################
00 09 * * * /home/colaman/WORKS/WORKS_COLAMAN/pythonWorks/notifyOutboundIP_LINE/shell/notifyOutboundIP_LINE.sh
00 21 * * * /home/colaman/WORKS/WORKS_COLAMAN/pythonWorks/notifyOutboundIP_LINE/shell/notifyOutboundIP_LINE.sh
</code></pre>

<br/><br/>
## 후속계획
1. 발송 모듈을 표준화하여, 다른 APP 에서도 범용적으로 가져다 쓸 수 있도록 개선하자.

<br/><br/>
## -- 끝 --
