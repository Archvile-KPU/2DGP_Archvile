# 2D GAME   PROGRAMMING
Written by: Minkyu Ham(함민규)
Korea Polytechnic University
Department of Game Engineering 2019180044
GitHub: Archvile-KPU
Repository URL: https://github.com/Archvile-KPU/2DGP_Archvile.git
Contact: archvile@kpu.ac.kr

This document is written in order to inform anyone who is interested in this very project.

### TABLE OF CONTENT
>  I. Introduction
>  II. GameState basics
>  III. GameState details
>  IV. Required technologies

### I. INTRODUCTION
**게임의 제목: DOOM 2D**
**원본 게임의 정보:**
> First Person Shooter 장르의 기반을 다진 게임.
> 데스매치와 같은 용어부터 시작해서, 데스매치, 클리핑 등의 용어 사용의 시초가 되고 게임 모드(MOD) 개발의 초석이 된 게임으로, 93년 첫 시리즈 발매 이후로 2020년에도 신작(DOOM Eternal)이 발매된 베스트셀링 프랜차이즈.
게임 스크린샷:
> ![enter image description here](https://raw.githubusercontent.com/Archvile-KPU/TEMP/51532226e537c29fd9e1fb874f1e2a738f8d472b/d3bpppr-7b7d8be0-5168-4e55-bb7e-67a7b6d2f346.png)

**게임의 목적:**
> 악마들을 쓰러트리며 죽지 않고 스테이지를 클리어하는 것이 목적. 각 스테이지마다 Exit(또는 레벨 종료 트리거)이 한 개 이상 있다. 이 때 클리어 스크린에 클리어에 걸린 시간, 획득한 아이템, 발견한 비밀(Secret)의 개수를 표시하여 스피드런 등에 활용한다.
### II. GAMESTATE BASICS
 GameState의 수: estimated to be 12
GameState 종류: 
 - ## Game Lobby
 - #### Create New Game
> - Choose Episode
> - Choose Difficulty
>> - NIGHTMARECHECK
>> - GAME_MAIN
>> - GAME_ENDSCREEN
>> - GAME_YOU_ARE_HERE
>> - GAME_EPILOGUE
 - #### Game Options
 - #### Load Game
 > - // sub states are same as Create New Game
 - #### Save Game
 - #### Read This!
 - #### Quit Game
> - AreYouSure?

### III. GAMESTATE DETAILS
#### 한줄 설명:
 - ## Game Lobby: 게임 로비,로고 출력, 데모 스크린 출력(if possible.)
 - #### Create New Game: 새로운 게임 시작, 에피소드와 난이도 선택
> - Choose Episode: 에피소드 선택창
> - Choose Difficulty: 난이도 선택창
>> - NIGHTMARECHECK: NIGHTMARE! 난이도 선택 시 확인 창 디스플레이
>> - GAME_MAIN: 실제 게임이 구동되는 환경
>> - GAME_ENDSCREEN: 스테이지 종료 시 킬 카운트, 아이템 퍼센티지, 시크릿 퍼센티지 출력
>> - GAME_YOU_ARE_HERE: 에피소드 내 게임 진척도 표시
>> - GAME_EPILOGUE: 에피소드 종료 시 모노로그 출력
 - #### Game Options: 게임 설정창
 - #### Load Game: 저장된 게임 불러오기
 > - // sub states are same as Create New Game
 - #### Save Game: 게임 저장
 - #### Read This!: 디폴트 설정 매뉴얼 출력 및 개발 노트 출력
 - #### Quit Game: 게임 종료
> - AreYouSure?: 게임 종료 전 확인 및 짜증나는 메세지 출력

#### 필요 객체 목록:
Game Lobby
> DOOM logo
> Menu selections
> Game Demo screen(if possible.)
> Cursor Skull

Create New Game
> Choose Episode
>> Which Episode?
>> Menu Selections
>> Cursor Skull
>
> Choose Difficulty
>> Which Difficulty?
>> Menu Selections
>> Cursor Skull
>
>NIGHTMARECHECK
>> Are you sure?
>> Menu Selections
>> Cursor Skull
>

GAME_MAIN
> HUD(Head-Up Display)
>> Ammo
>> Health
>> Arsenal
>> Armor
>> Ammo_t
>> Face_Indicator
>
> Monsters
>> ZombieMan, Imp, Pinkie etc..,
>
> Doors
> Walls
> Switches
>> Exit
>> DoorSwitches
>>Event_trigger
>
> Secret_Trigger
> ItemPickups
>> Weapon
>> Ammo
>> Health
>> Powerup
>> Key
>
> Entities

GAME_ENDSCREEN
> KillCount
> ItemCount
> SecretCount
> PAR
> ElapsedTime

GAME_YOU_ARE_HERE
> Current Position
> Episode Map

GAME_EPILOGUE
> Text formed storyline - NOT SIGNIFICANT! - John Carmack

Game Options
> Graphics Options
> Controls
> Brutality Control

Load Game
> Save Files
> Cursor Skull

Read This!
> Default Controls
> Credits

Quit Game
> AreYouSure?
>> Message 

#### 처리할 키/마우스 이벤트
- ## Game Lobby: 윈도우의 X버튼을 누르면 종료, 마우스나 키로 로비 메뉴 선택
 - #### Create New Game: 
> - Choose Episode: 마우스로 선택, esc로 이전 단계
> - Choose Difficulty: 마우스로 선택, esc로 이전 단계 
>> - NIGHTMARECHECK: NIGHTMARE!: y로 ok, n으로 이전 단계
>> - GAME_MAIN: WASD 컨트롤, LMB 사격, RMB 상호작용, NUM키로 무기 선택, ESC로 로비 출력
if possible: CHEAT CODES(IDDQD)
>> - GAME_ENDSCREEN: 클릭으로 다음 단계
>> - GAME_YOU_ARE_HERE: 클릭으로 다음 단계
>> - GAME_EPILOGUE: 클릭으로 다음 단계
 - #### Game Options: 파라미터를 마우스로 조정, esc로 이전 단계
 - #### Load Game: 세이브 파일을 마우스로 선택, esc로 이전 단계
 > - // sub states are same as Create New Game
 - #### Save Game: 세이브 파일 위치를 마우스로 선택, esc로 이전 단계 만약 빈 세이브파일에 저장하고자 한다면 세이브 파일 이름을 키보드로 입력
 - #### Read This!:  esc로 이전 단계
 - #### Quit Game: 
> - AreYouSure?: y로 게임 종료, n으로 이전 단계

State 전환:
위 키 처리 메소드에 조금 설명되어 있으나 보충하자면, 메뉴 선택(클릭)으로 하위 state에 진입하며, esc로 상위 state에 진입한다. Hierarchy는 위 리스트를 따른다.

### IV. REQUIRED TECHNOLOGIES
#### 다른 과목에서 배운 기술:
> OpenGL 수업에서 그래픽 처리와 충돌 처리에 대해 일부 배움
> OSSW 수업에서 프로젝트에 도움이 될 Git 사용법을 익힘
> C Programming에서의 기본적인 프로그래밍 개념
> C++ Programming에서의 OOP 및 클래스 개념

#### 이 과목에서 배울 것으로 기대되는 기술
> 게임 프로젝트 객체
> 게임 렌더링
> Python Programming
> Visual Studio 및 ViM 외 타 개발 환경에 대한 Orientation
> Pico2D를 이용한 2D Game Programming
> 그래픽 버퍼링

#### 다루지 않아 다루어 달라고 요청할 기술
> 투사체 및 객체 충돌 처리
> 히트스캔 처리 방식
> 게임 세이브 & 로드
> 윈도우 풀스크린

### END OF DOCUMENT

