
import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/imprimir', methods=['POST'])
def index():
    try:
        data = request.get_json()
       
        printer_name = data.get('printer', '')
        content = data.get('content', [])  

        if printer_name == '' or not content:
            return jsonify({'error': 'Nome da impressora ou conteúdo ausente na solicitação.'}), 400 

        # Cria um arquivo temporário com o conteúdo a ser impresso
        # tmp_file_path = 'temp_print.txt'
        # with open(tmp_file_path, 'w') as tmp_file:
        #     for line in content:
        #         tmp_file.write(line + '\n')    

        # notepad_path = os.path.join( "C:", "Windows",  "notepad.exe" ) 
       
        # print_command = f'{notepad_path} /p "{tmp_file_path}"'
        # os.system(print_command)


        tmp_file_path = 'temp_print.txt'
        with open(tmp_file_path, 'wb') as tmp_file:
            # tmp_file.write(b'\x1B\x40')  # Reinicia a impressora
            # tmp_file.write(b'\x1B\x61\x30')  # Alinha o texto à esquerda
            
            for line in content:
                tmp_file.write(line.encode('utf-8') + b'\n')
                # tmp_file.write(b'\x1B\x61\x31')  # Alinha o texto ao centro
                # tmp_file.write(line.encode('utf-8') + b'\n')
                # tmp_file.write(b'\x1B\x61\x32')  # Alinha o texto à direita
                # tmp_file.write(line.encode('utf-8') + b'\n')
     

            
            
        # Comando para imprimir o arquivo usando o Bloco de Notas
        print_command = f'notepad /p "{tmp_file_path}"'
        os.system(print_command)  


        return jsonify({'message': 'Impressão enviada com sucesso para a impressora.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Remove o arquivo temporário após a impressão
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


   