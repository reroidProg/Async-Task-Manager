from checker import PingChecker
import asyncio

def print_banner():
    print("\n")
    print("=" * 30)
    print("Async Task Manager")
    print("=" * 30)
    print("1. Проверить сайт\n2. Выйти\n")

async def main():
    checker = PingChecker()
    
    while True:
        print_banner()
        choice = input("Ответ: ")
        
        if choice == '2':
            print("Выход из программы...")
            break
        elif choice == '1':
            web_name = input("URL: ")
            print("\n")
            result = await checker.ping(web_name)
            print(f"Result: Ping - {result[0]} Status - {result[1]}")
            input("Нажмите Enter для продолжения...")
        else:
            print("Неверный выбор, попробуйте снова.\n")

if __name__ == "__main__":
    asyncio.run(main())
