import pickle

"""
객체지향으로 구현한 전화번호부
"""


# 사람의 정보를 가지고 있는 클래스
class Person:
    # 사람에 대한 정보를 추가
    def __init__(self, name, phone, email, memo=""):
        self.name = name
        self.phone = phone
        self.email = email
        self.memo = memo

    # 연산자 오버로딩으로 print를 구현
    def __str__(self):
        return f"{self.name} {self.phone} {self.email} {self.memo}"


# 전화번호부 클래스
class Phonebook:

    FILENAME = "my_phonebook.pkl"

    # 만약 저장된 파일이 있다면 불러오고 없다면 Person을 담을 리스트를 생성
    def __init__(self):
        try:
            with open(self.FILENAME, "rb") as f:
                self.contact_list = pickle.load(f)
            print("저장된 데이터를 불러왔습니다.")
        except FileNotFoundError:
            self.contact_list: list[Person] = []
            print("저장된 데이터가 없습니다")

    # len 오버로딩으로 저장된 데이터의 개수를 반환
    def __len__(self) -> int:
        return len(self.contact_list)

    # 이름을 입력받아서 해당 이름의 정보를 반환
    def search(self):

        input_name = input("찾으실 이름을 입력하세요: ")
        for person in self.contact_list:
            if person.name == input_name:
                # 그 이름이 몇 번째에 있는지 순서도 알려줌
                print(self.contact_list.index(person) + 1, end=" ")
                print(person)
                break
        else:
            print(f"{input_name}을/를 찾지 못했습니다")

    # 이름을 입력받고 만약 이름이 존재한다면 정보를 수정하고 존재하지 않는다면 정보를 추가
    def add_or_update(self):
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        email = input("이메일을 입력하세요: ")

        for person in self.contact_list:
            if person.name == name:
                person.phone = phone
                person.email = email
                print(f"{name}의 정보가 변경되었습니다")
                break
        else:
            self.contact_list.append(Person(name, phone, email))
            print(f"{name}을/를 추가했습니다")

    # 이름을 입력받아서 해당 이름의 정보를 삭제
    def delete_info(self):

        input_name = input("삭제할 이름을 입력하세요: ")
        for person in self.contact_list:
            if person.name == input_name:
                self.contact_list.remove(person)
                print(f"{input_name} 삭제됐습니다")
                break
        else:
            print("해당하는 연락처가 없습니다")

    # 저장된 모든 데이터를 총 인원과 각 인덱스를 포함해서 출력
    def show_all(self):
        print(f"총 인원: {len(self)}명")
        if self.contact_list:
            for person in self.contact_list:
                print(self.contact_list.index(person) + 1, end=" ")
                print(person)
        else:
            print("현재 등록된 연락처가 없습니다")

    # 원하는 이름에 메모를 추가할 수 있음
    def memo(self):

        input_name = input("메모를 저장할 이름을 입력하세요: ")
        input_memo = input("메모를 입력하세요: ")
        for person in self.contact_list:
            if person.name == input_name:
                person.memo = input_memo
                print("메모가 추가되었습니다. ")
                break
        else:
            print("해당하는 이름이 없습니다")

    # 프로그램이 종료될 때 리스트에 들어있는 정보를 바이너리 파일로 저장
    def save(self):
        with open(self.FILENAME, "wb") as f:
            pickle.dump(self.contact_list, f)
            print("데이터를 저장했습니다.")


# 사용자가 기능을 선택할 수 있음
def user_select() -> int:
    while user_input := input(
        "(1) 찾기 (2) 추가/변경 (3) 삭제 (4) 모두 보기 (5) 메모 (6) 종료 : "
    ):
        if user_input in ("1", "2", "3", "4", "5", "6"):
            return int(user_input)
        else:
            print("잘못된 명령입니다")


# 사용자의 입력에 따라 그에 맞는 함수를 실행
def main(phonebook):

    menu = {
        1: phonebook.search,
        2: phonebook.add_or_update,
        3: phonebook.delete_info,
        4: phonebook.show_all,
        5: phonebook.memo,
    }

    while (selected := user_select()) != 6:
        menu[selected]()
    else:
        phonebook.save()
        print("종료합니다")


# 프로그램 실행부
if __name__ == "__main__":

    my_phonebook = Phonebook()

    main(my_phonebook)
