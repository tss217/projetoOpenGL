from PIL import Image
import os

def convert_texture_to_png(mtl_file_path):
    # Obtém o diretório do arquivo MTL
    mtl_dir = os.path.dirname(mtl_file_path)

    # Abre o arquivo MTL para leitura
    with open(mtl_file_path, 'r') as mtl_file:
        lines = mtl_file.readlines()

        # Procura por linhas que contenham a referência à textura
        for line in lines:
            if line.startswith('map_Kd'):
                # Obtém o caminho da textura
                texture_path = line.split()[1]
                
                # Obtém o caminho absoluto da textura
                absolute_texture_path = os.path.join(mtl_dir, texture_path)

                # Carrega a imagem
                texture_image = Image.open(absolute_texture_path)
                
                # Gera o novo caminho para a textura PNG
                png_texture_path = os.path.join(mtl_dir, texture_path.replace('.mlt', '.png'))
                
                # Salva a imagem como PNG
                texture_image.save(png_texture_path, format='PNG')
                
                print(f'Texture converted to PNG: {png_texture_path}')
                return

if __name__ == "__main__":
    mtl_file_path = "C:/Users/ts217/Documents/provaVC/Creeper.mtl"
    convert_texture_to_png(mtl_file_path)
