# min-llm-bot
LLM chat bot to use CrewAI


## 1. 프로젝트 세팅
- VSC
- Github 연동

## 2. 프로젝트 구성
- 가상환경 설정 => Docker Container 개념 (공간을 분리해서 따로 관리)
- python 3.8 열심히 개발을 함 -> 근데 배포할 서버가 3.3 버전의 phyton -
- > 3.8 함수에만 있고 3.3에는 없는 함수 -> 오류 -> 배포 후 앎 
=> 로컬에서 작업하는 환경과 호스트 서버에서 작업하는 환경을 일치시켜 주기 위함
=> Docker(Virtual Machine)  // venv 모듈을 사용해서 환경 설정을 해줌 

- 명령어 (같은 폴더에 있는 상태에서) : 
>python3.10 -m venv .venv
(lib 폴더에서 python3.10인거 확인 가능)


- 가상환경 container 안으로 이동 (activate)
>source .venv/bin/activate (mac)
>.venv/Scripts/activate (win)



## 3. 프로젝트
###3-1. Ollama 모델 + CrewAI
- 언어 모델 다운 -> CrewAI 설치해서 챗봇 시스템 만들기

(1) ollama 다운로드
(2) ollama 통해서 모델 다운로드
> ollama pull llama3.1
> ollama run llama3.1

> ollama pull phi3:3.8b
> ollama run phi3:3.8b

(3) CrewAI 설치 
- 언어 모델의 API 관리를 편리하게 도와주는 라이브러리
- 모델 - 클로드, 잼미니, GPT3.5, GPT4o, ... => import OpenAI // 언어마다 SDK 다운받아야 함 
=> CrewAI, LangChain이 이미 다 SDK 구현을 끝내놓음  
- LangChain 대신 CrewAi를 사용하는 이유 : 러닝 커브가 낮아서 가벼움 

- CrewAI 설치 
> pip install crewai crewai-tools
> pip install langchain-ollama


###3-2. Flask 사용해서 기본적인 챗봇  