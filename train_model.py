# -*- coding: utf-8 -*- 
import joblib
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression # Вариант 1
from sklearn.svm import SVC # Вариант 2 (часто дает лучше качество на digits)
from sklearn.metrics import accuracy_score

# 1. Загрузка данных
digits = load_digits()
X, y = digits.data, digits.target

# Нормализация данных (важно для многих моделей)
# Пиксели имеют значения от 0 до 16
X = X / 16.0 

# 2. Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Выбор и обучение модели
# model = LogisticRegression(max_iter=1000) # Вариант 1
model = SVC(gamma=0.001) # Вариант 2
    
print("Начинаем обучение модели...") # <-- ИСПРАВЛЕНО
model.fit(X_train, y_train)
print("Обучение завершено.") # <-- ИСПРАВЛЕНО

# 4. (Опционально) Проверка качества на тестовой выборке
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
# Используем f-строку для вывода, она проще
print(f"Точность на тестовой выборке: {accuracy:.4f}") # <-- ИСПРАВЛЕНО

# 5. Сохранение обученной модели
model_filename = 'model.joblib'
joblib.dump(model, model_filename)
# Используем f-строку
print(f"Модель сохранена в файл: {model_filename}") # <-- ИСПРАВЛЕНО