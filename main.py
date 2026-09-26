from database import DataBase
from checker import PingChecker
import asyncio

def print_banner():
    print("\n")
    print("=" * 30)
    print("Async Task Manager")
    print("=" * 30)
    print("1. Проверить один сайт\n2. Проверить сайты (Пустая строка для завершения)\n3. Посмотреть DB\n4. Выйти\n")

async def main():
    checker = PingChecker()
    data_base = DataBase()
    await data_base.init()
    
    while True:
        print_banner()
        choice = input("Ответ: ")
        
        if choice == '4':
            print("Выход из программы...")
            break
        elif choice == '1':
            web_name = input("URL: ").strip()
            if not web_name:
                continue
            print("\n")
            result = await checker.ping(web_name)
            if result:
                # порядок в save: url, status_code, time, ok
                await data_base.save(result[0], result[2], result[1], result[3])
                print(f"Result: Ping - {result[1]}ms | Status - {result[2]}")
            input("Нажмите Enter для продолжения...")
        elif choice == '2':
            print("Введите URL (пустая строка для старта проверки):")
            urls = []
            while True:
                webs_name = input("URL: ").strip()
                if webs_name == "":
                    break
                urls.append(webs_name)
                
            if urls:
                print("\n")
                async with asyncio.TaskGroup() as tg:
                    tasks = [tg.create_task(checker.ping(url)) for url in urls]

                for task in tasks:
                    result = task.result()
                    if result:
                        await data_base.save(result[0], result[2], result[1], result[3])
                        print(f"Result: URL - {result[0]} | Ping - {result[1]}ms | Status - {result[2]}")
                input("Нажмите Enter для продолжения...")

        elif choice == '3':
            print(await data_base.fetch())
            input("Нажмите Enter для продолжения...")
        else:
            print("Неверный выбор, попробуйте снова.\n")

if __name__ == "__main__":
    asyncio.run(main())
