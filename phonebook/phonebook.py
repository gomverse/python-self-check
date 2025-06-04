"""
sqlite를 이용한 전화번호부 프로그램

사용자의 입력을 받아 찾기, 추가 및 수정, 삭제, 모두 출력의 기능을 수행한다
"""

import sqlite3 as sq

conn = sq.connect("phonebook.db")
phonebook = conn.cursor()


def db_search() -> None:
    """
    사용자 이름을 입력받고 해당 이름에 해당하는 데이터를 읽어서 출력
    """

    name = input("이름을 입력해주세요: ")
    phonebook.execute(
        "SELECT * FROM my_contacts WHERE Name = ?", (name,)
    )  # 이름에 해당하는 정보를 찾아 출력
    result = phonebook.fetchone()  # SQL 쿼리 결과에서 행을 꺼내옴

    if result:
        print(*result)
    else:  # 가져올 행이 없다면 출력
        print("해당하는 이름이 없습니다")


def db_add_or_modify() -> None:
    """
    이름, 휴대폰 번호, 이메일을 입력받아서 DB에 추가
    """
    name = input("이름을 입력하세요: ")
    phone = input("전화번호를 입력하세요: ")
    email = input("이메일을 입력하세요: ")

    phonebook.execute(
        "INSERT OR REPLACE INTO my_contacts (name, phone, email) VALUES (?, ?, ?)",
        (name, phone, email),
    )  # 해당 이름이 없다면 추가하고, 이름이 있다면 수정
    print(f"{name} 추가/수정 완료")
    conn.commit()


def db_del():
    """
    이름을 입력받고 해당 이름의 데이터를 삭제
    """
    name = input("삭제할 이름을 입력하세요: ")

    phonebook.execute("DELETE FROM my_contacts WHERE Name=?", (name,))
    if phonebook.rowcount == 0:  # 마지막으로 실행한 명령이 영향을 준 행이 없다면
        print("해당하는 이름이 없습니다. ")
    else:
        print(f"{name} 삭제 완료")
        conn.commit()


def db_print_all():
    """
    DB를 모두 출력
    """
    for info in phonebook.execute("SELECT * FROM my_contacts"):
        print(*info)


func_map = {
    "1": db_search,
    "2": db_add_or_modify,
    "3": db_del,
    "4": db_print_all,
}  # 명령을 사전형태로 저장

while True:
    choice = input("(1)찾기 (2)추가/변경 (3)삭제 (4)모두보기 (5)종료: ")
    if choice == "5":
        conn.close()
        print("종료합니다.")
        break
    elif choice in func_map:
        func_map[choice]()  # 해당 명령에 해당하는 함수를 실행
    else:
        print("잘못된 명령입니다.")
