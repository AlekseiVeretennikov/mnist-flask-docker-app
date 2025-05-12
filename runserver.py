# -*- coding: utf-8 -*-
"""
This script runs the MnistFlaskDockerApp application using a development server.
"""

# Импортируем объект 'app' из вашего пакета приложения (папки MnistFlaskDockerApp)
from MnistFlaskDockerApp import app 

if __name__ == '__main__':
    # Запускаем встроенный сервер Flask
    # host='0.0.0.0' - делает сервер доступным с любого IP-адреса машины (важно для Docker и доступа по сети)
    # port=5000     - стандартный порт для веб-разработки, используется в нашем Docker-конфиге
    # debug=True    - включает режим отладки (сервер перезагружается при изменении кода, показывает ошибки в браузере)
    #                 ВАЖНО: Не используйте debug=True в реальной продакшн-среде!
    app.run(host='0.0.0.0', port=5000, debug=True) 