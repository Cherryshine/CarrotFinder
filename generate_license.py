from cryptography.fernet import Fernet
import base64

def generate_license_key(plan):
    # 고정된 Fernet 키 생성 (실제 배포 시 이 키를 변경하세요)
    key = b'dL-KXsbXFQGheP6ckh1OlZE4YWxOGxjqh0ZsO-2JYpM='  # 올바른 형식의 Fernet 키
    cipher = Fernet(key)
    encrypted = cipher.encrypt(plan.encode())
    return base64.b64encode(encrypted).decode()

def get_plan_from_input():
    while True:
        try:
            print("라이센스 종류를 선택하세요:")
            print("1: 1개월")
            print("3: 3개월")
            print("6: 6개월")
            print("0: 영구")
            print("T: 20초 테스트")
            
            months = input("선택: ").upper()
            if months not in ['0', '1', '3', '6', 'T']:
                print("잘못된 입력입니다. 1, 3, 6, 0(영구), T(테스트) 중에서 선택하세요.")
                continue
            
            if months == '0':
                return "cherrypermanent"
            elif months == 'T':
                return "cherry20sec"
            else:
                return f"cherry{months}month"
                
        except ValueError:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 메인 실행
if __name__ == "__main__":
    plan = get_plan_from_input()
    key = generate_license_key(plan)
    print(f"\n생성된 라이센스 키: {key}")
    input("\n아무 키나 눌러서 종료...") 