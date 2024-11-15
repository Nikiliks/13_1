# Задача "Асинхронные силачи"
import  asyncio



async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power) # Задержка обратно пропорциональная силе
        print(f'Силач {name} поднял {i}' )

    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
        tasks = [
            start_strongman("Pasha", 3),
            start_strongman("Denis", 4),
            start_strongman("Apollon", 5)
        ]

        for task in tasks:
            await task

    # Запуск асинхронного основного цикла
asyncio.run(start_tournament())




