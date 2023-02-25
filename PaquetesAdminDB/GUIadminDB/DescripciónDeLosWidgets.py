#1ero definimos los subdicts por tipo de widgets:
#Para el el subcuerpo superior:
variableDeControlCuerpoSuperior = {'pathBD':{'tipoWidget':'controlvar', 'tipoVar':'texto'}, 'tipoBD':{'tipoWidget':'controlvar', 'tipoVar':'texto'}, 'tabla':{'tipoWidget':'controlvar', 'tipoVar':'texto'}} #,...y así para el resto de variables de control. Note que las claves del diccionario contenedor o externo, conformarán los nombres de
# dichos objetos widgets o variables de control creados con el atributo método, setattr(), en la función crearWidgetsYsusVarControlEnBaseAdescrip() del módulo Crear.py.

infoEntrysCuerpoSup = {'txtBox_PathBD':{'tipoWidget':'entry', 'ancho':'2', 'varcontrol':'pathBD', 'col':2, 'fila':1, 'sticky':'nsew', 'columnspan':2}}

infoComboboxCuerpoSup = { 'comboBox_tipoBD':{'tipoWidget':'combobox', 'ancho':9, 'col':2, 'fila':2, 'varcontrol':'tipoBD','sticky':'ew', 'columnspan':1}, 'comboBox_Tablas':{'tipoWidget':'combobox', 'ancho':14, 'col':2, 'fila':3, 'varcontrol':'tabla','sticky':'', 'columnspan':1}}

infoLabelsCuerpoSup = {'etiqPathBD':{'tipoWidget':'label', 'texto':'PathBaseDeDatos', 'col':1, 'fila':1, 'sticky':'', 'columnspan':1}, 'etiqTipoBD':{'tipoWidget':'label', 'texto':'TipoBaseDeDatos', 'col':1, 'fila':2, 'sticky':'', 'columnspan':1}, 'etiqTablas':{'tipoWidget':'label', 'texto':'Tablas', 'col':1, 'fila':3, 'sticky':'e', 'columnspan':1}}

infoButtonCuerpoSup = { 'botón_conectarBD':{'tipoWidget':'botón', 'ancho':8, 'col':3, 'fila':2, 'sticky':'w', 'texto':'Conectar', 'comando': '', 'columnspan':1}} 

#Finalmente concatenamos para hacer un diccionario global con la descripción de todos lo widgets:
descripWidgetsCuerpoSuperior = {**variableDeControlCuerpoSuperior, **infoEntrysCuerpoSup, **infoLabelsCuerpoSup, **infoComboboxCuerpoSup, **infoButtonCuerpoSup} 
#Ojo, el orden importa: primero **variableDeControl, puesto que los textvariable no dependen de la existencia de los entrys, más no así el caso contrario.

#Otros datos constantes:
BaseDeDatosTipos = ('postgresql', 'sqlite')

