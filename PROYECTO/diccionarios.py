lista_usuarios = []


dict_acumuladores = [{
"usuarios_con_amigos" : 0,
"id_usuario" : 1000,
"cantidad_usuarios": 0,
"acumulador_edad" : 0,
"max_presupuesto_pc_alta" : 0,
"cantidad_recomendaciones" : 0
}]

# agregado, cambiar el main para guarde aca las estadisticas
lista_estadisticas_generales = [{
    "promedio_edad" : 0,
    "porcentaje_usuarios_con_amigos" : 0,
    "edad_maxima" : 0, 
    "edad_minima" : 101,
    "hay_pc_alta" : False,
    "flag_case2" : True
}]

lista_puntos_genero_juegos = [{
"genero_juego" : "accion",
"puntos" : 0
},
{
"genero_juego" : "historia",
"puntos" : 0
},{
"genero_juego" : "estrategia",
"puntos" : 0
}]

lista_estadisticas_genero = [
{
"genero" : "masculino",
"puntos" : 0,
"porcentaje" : 0,
"promedio" : 0,
"presupuesto" : 0
},{
"genero" : "femenino",
"puntos" : 0,
"porcentaje" : 0,
"promedio" : 0,
"presupuesto" : 0
},{
"genero" : "no binario",
"puntos" : 0,
"porcentaje" : 0,
"promedio" : 0,
"presupuesto" : 0
}]
