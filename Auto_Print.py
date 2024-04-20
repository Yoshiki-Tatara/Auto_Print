import os
import subprocess

# 印刷するファイルが保存されているフォルダのパス
folder_path = 'C:\\path\\to\\your\\folder'

# サポートされているファイル形式
supported_formats = ['.pdf', '.png']

def print_file(file_path):
    try:
        # Windowsの場合、startコマンドを使用してファイルを印刷
        subprocess.run(['start', '/min', file_path, '/t', 'Microsoft Print to PDF', '/m'], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error printing {file_path}: {e}")

def main():
    # 指定されたフォルダ内のファイルを探索
    for filename in os.listdir(folder_path):
        # ファイルの拡張子をチェック
        if any(filename.endswith(ext) for ext in supported_formats):
            file_path = os.path.join(folder_path, filename)
            print(f"Printing {file_path}...")
            print_file(file_path)

if __name__ == '__main__':
    main()
