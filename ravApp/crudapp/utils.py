import httpx


async def download_large_file(url):
    downloads_folder = 'downloads/'
    file_name = url.split('/')[-1]
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", url) as response:
            if response.status_code == 200:
                with open(downloads_folder + file_name, 'wb') as file:
                    async for chunk in response.aiter_bytes():
                        file.write(chunk)
                return f'Файл {file_name} успешно загрежен'
            else:
                return f"Ошибка при загрузке файла, статус: {response.status_code}"
