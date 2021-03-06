from cx_Freeze import setup, Executable
# Referência: https://civcomunb.wordpress.com/2016/08/28/criando-executaveis-com-cx_freeze/'
# 'Compilar' programa: python setup.py build

# executable options
script = 'main.py'                                                       # nome do arquivo principal .py a ser compilado
base = None                                                           # usar 'Win32GUI' para gui's e 'None' para console
# icon = 'balao.png'                                                          # nome (ou diretório) do icone do executável
targetName = 'Robo de consulta.exe'                                                       # nome do .exe que será gerado

# build options
packages = ['selenium']                                                         # lista de bibliotecas a serem incluídas
includes = []                                                                       # lista de módulos a serem incluídos
include_files = []                           # lista de outros arquivos a serem incluídos (imagens, dados...)

# shortcut options
shortcut_name = 'Robo de consulta'                            # nome do atalho que será criado no processo de instalação

# bdist_msi options
company_name = 'Igor Alberte'                  # nome da pasta em 'Arquivos de Programas' onde o software será instalado
product_name = 'Robo de consulta'                                    # nome da subpasta em que o software será instalado
upgrade_code = '{66620F3A-DC3A-11E2-B341-002219E9B01E}'                      # código para upgrade de versão do programa
add_to_path = False                                                                      # adicionar o programa ao path?

# setup options
name = 'Robo de consulta'                                                       # Nome do programa na descrição
version = '0.1'                                                                        # versão do programa na descrição
description = 'Robo de consulta do controle interno'                                             # descrição do programa

"""
Edit the code above this comment.
Don't edit any of the code bellow.
"""

msi_data = {'Shortcut': [
    ("DesktopShortcut",         # Shortcut
     "DesktopFolder",           # Directory_
     shortcut_name,      # Name
     "TARGETDIR",               # Component_
     "[TARGETDIR]/{}".format(targetName),  # Target
     None,                      # Arguments
     None,                      # Description
     None,                      # Hotkey
     None,                      # Icon
     None,                      # IconIndex
     None,                      # ShowCmd
     "TARGETDIR",               # WkDir
     ),

    ("ProgramMenuShortcut",         # Shortcut
     "ProgramMenuFolder",           # Directory_
     shortcut_name,      # Name
     "TARGETDIR",               # Component_
     "[TARGETDIR]/{}".format(targetName),  # Target
     None,                      # Arguments
     None,                      # Description
     None,                      # Hotkey
     None,                      # Icon
     None,                      # IconIndex
     None,                      # ShowCmd
     "TARGETDIR",               # WkDir
     )
    ]
}

opt = {
    'build_exe': {'packages': packages,
                  'includes': includes,
                  'include_files': include_files
                  },
    'bdist_msi': {'upgrade_code': upgrade_code,
                  'add_to_path': add_to_path,
                  'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
                  'data': msi_data
                  }
}

exe = Executable(
    script=script,
    base=base,
    # icon=icon,
    targetName=targetName,
    # shortcutName=shortcut_name,
    # shortcutDir='DesktopFolder'
)

setup(name=name,
      version=version,
      description=description,
      options=opt,
      executables=[exe]
      )
