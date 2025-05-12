# -*- coding: utf-8 -*-
"""
This script runs the MnistFlaskDockerApp application using a development server.
"""

# ����������� ������ 'app' �� ������ ������ ���������� (����� MnistFlaskDockerApp)
from MnistFlaskDockerApp import app 

if __name__ == '__main__':
    # ��������� ���������� ������ Flask
    # host='0.0.0.0' - ������ ������ ��������� � ������ IP-������ ������ (����� ��� Docker � ������� �� ����)
    # port=5000     - ����������� ���� ��� ���-����������, ������������ � ����� Docker-�������
    # debug=True    - �������� ����� ������� (������ ��������������� ��� ��������� ����, ���������� ������ � ��������)
    #                 �����: �� ����������� debug=True � �������� ��������-�����!
    app.run(host='0.0.0.0', port=5000, debug=True) 