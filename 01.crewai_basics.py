from crewai import Crew, Agent, Task 
from langchain_ollama import ChatOllama

from langchain_ollama import ChatOllama
from openai import OpenAI

llm = ChatOllama(
    model = 'phi3:3.8b',
    base_url='http://127.0.0.1:11434'       # cmd + 링크 클릭 : Ollama is running
)

# Crew : 러닝크루 => N명 (조직)
# Agent : 요원 => 1명 (조직원)
# Task : 미션 

# 쇼핑몰 
# 챗봇 기능 - 

user_question = input("편하게 질문해주세요 :)")

book_agent = Agent(
    role = '책 구매 어시스턴트',
    goal = '고객이 어떤 상황인지 설명을 하면 해당 상황에 맞는 우리 서점에 있는 책을 소개합니다.', 
    backsotry = '당신은 우리 서점의 모든 책 정보를 알고 있으며, 사람들의 상황에 맞는 책을 소개하는 전문가입니다.', 
    llm = llm
)

recommend_first_task = Task(
    #description = '고객의 상황에 맞는 최고의 추천 도서 제안하기', 
    description = user_question,
    expected_output= '고객의 상황에 맞는 5권의 도서를 추천해주고, 해당 책을 추천한 이유를 알려줘',
    agent = book_agent, 
    output_file='recommend_book_task.md'
)


review_agent = Agent(
    role = '책 리뷰 어시스턴트',
    goal = '추천받은 책들의 도서에 대한 리뷰를 제공하고, 해당 도서에 대한 심도있는 평가를 제공합니다.', 
    backsotry = '당신은 우리 서점의 모든 책 정보를 알고 있으며, 사람들의 상황에 맞는 책을 소개하는 전문가입니다.', 
    llm = llm
)

review_task = Task(
    description = '고객이 선택한 책에 대한 리뷰를 제공합니다.', 
    expected_output= '고객이 선택한 책에 대한 리뷰를 제공합니다.',
    agent = book_agent, 
    output_file='review_book_task.md'
)


# 요원과 미션 관리 
crew = Crew(
    agents=[book_agent, review_agent],
    tasks=[recommend_first_task, review_task],
    verbose=2
)

result = crew.kickoff()

print(result)

# RAG 